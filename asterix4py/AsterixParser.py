from xml.dom import minidom

try:
    import importlib.resources as pkg_resources
except ImportError:  # try backwards compatibility python < 3.7
    import importlib_resources as pkg_resources

from . import config

astXmlFiles = {
    1: 'asterix_cat001_1_1.xml',
    2: 'asterix_cat002_1_0.xml',
    8: 'asterix_cat008_1_0.xml',
    10: 'asterix_cat010_1_1.xml',
    19: 'asterix_cat019_1_2.xml',
    20: 'asterix_cat020_1_7.xml',
    21: 'asterix_cat021_1_8.xml',
    23: 'asterix_cat023_1_2.xml',
    30: 'asterix_cat030_6_2.xml',
    31: 'asterix_cat031_6_2.xml',
    32: 'asterix_cat032_7_0.xml',
    48: 'asterix_cat048_1_14.xml',
    62: 'asterix_cat062_1_18.xml',
    63: 'asterix_cat063_1_3.xml',
    65: 'asterix_cat065_1_3.xml',
    242: 'asterix_cat242_1_0.xml',
    252: 'asterix_cat252_7_0.xml'
}


class AsterixParser:
    """Decode bytearray of asterix data"""

    def __init__(self, bytesdata):
        self.bytes = bytesdata
        self.length = 0
        self.p = 0

        self.decoded_result = {}

        cat = int.from_bytes(self.bytes[0:1], byteorder='big', signed=True)
        self.p += 1

        try:
            xml = pkg_resources.read_text(config, astXmlFiles[cat])
            self.cat = minidom.parseString(xml)

            category = self.cat.getElementsByTagName('Category')[0]
            self.dataitems = category.getElementsByTagName('DataItem')
            uap = category.getElementsByTagName('UAP')[0]
            self.uapitems = uap.getElementsByTagName('UAPItem')
        except:
            print('cat %d not supported now' % cat)
            return

        self.decoded_result[cat] = []

        self.length = int.from_bytes(
            self.bytes[self.p:self.p + 2], byteorder='big', signed=True)
        self.p += 2

        while self.p < self.length:
            self.decoded = {}
            self.decode()
            self.decoded_result[cat].append(self.decoded)

    """get decoded results in JSON format"""
    def get_result(self):
        return self.decoded_result

    def decode(self):
        # ------------------ FSPEC -------------------------------
        fspec_octets = 0
        fspec_octets_len = 0
        while True:
            _b = self.bytes[self.p]
            self.p += 1
            fspec_octets = (fspec_octets << 8) + _b
            fspec_octets_len += 1
            if _b & 1 == 0:
                break
        # ------------------ FSPEC bits to uapitem id --------------------------
        itemids = []  # dataitems
        # mask is 0b1000000000...
        mask = 1 << (8 * fspec_octets_len - 1)

        for i in range(0, 8 * fspec_octets_len):
            if fspec_octets & mask > 0:
                itemid = self.uapitems[i].firstChild.nodeValue
                if itemid != '-':
                    itemids.append(itemid)

            mask >>= 1

        # ------------------ decode each dataitem --------------------------
        for itemid in itemids:
            for dataitem in self.dataitems:
                if dataitem.getAttribute('id') == itemid:
                    dataitemformat = dataitem.getElementsByTagName('DataItemFormat')[0]
                    for cn in dataitemformat.childNodes:
                        r = None
                        if cn.nodeName == 'Fixed':
                            r = self.decode_fixed(cn)
                        elif cn.nodeName == 'Repetitive':
                            r = self.decode_repetitive(cn)
                        elif cn.nodeName == 'Variable':
                            r = self.decode_variable(cn)
                        elif cn.nodeName == 'Compound':
                            r = self.decode_compound(cn)

                        if r:
                            self.decoded.update({itemid: r})

    def decode_fixed(self, datafield):
        results = {}
        length = int(datafield.getAttribute('length'))
        bitslist = datafield.getElementsByTagName('Bits')

        _bytes = self.bytes[self.p: self.p + length]
        self.p += length

        data = int.from_bytes(_bytes, byteorder='big', signed=False)

        for bits in bitslist:
            bit_name = bits.getElementsByTagName('BitsShortName')[
                0].firstChild.nodeValue

            bit = bits.getAttribute('bit')
            if bit != '':
                bit = int(bit)
                results[bit_name] = ((data >> (bit - 1)) & 1)

            else:
                from_ = int(bits.getAttribute('from'))
                to_ = int(bits.getAttribute('to'))

                if from_ < to_:  # swap values
                    from_, to_ = to_, from_
                mask = (1 << (from_ - to_ + 1)) - 1
                results[bit_name] = ((data >> (to_ - 1)) & mask)

                if bits.getAttribute('encode') == 'signed':
                    if results[bit_name] & (1 << (from_ - to_)):  # signed val
                        results[bit_name] = - (1 << (from_ - to_ + 1)) + results[bit_name]

                BitsUnit = bits.getElementsByTagName("BitsUnit")
                if BitsUnit:
                    scale = BitsUnit[0].getAttribute('scale')
                    results[bit_name] = results[bit_name] * float(scale)

        return results

    def decode_variable(self, datafield):
        results = {}

        for fixed in datafield.getElementsByTagName('Fixed'):
            r = self.decode_fixed(fixed)
            results.update(r)
            assert 'FX' in r
            if r['FX'] == 0:
                break

        return results

    def decode_repetitive(self, datafield):
        rep = self.bytes[self.p]
        self.p += 1

        results = []
        fixed = datafield.getElementsByTagName('Fixed')[0]
        for i in range(rep):
            r = self.decode_fixed(fixed)
            results.append(r)

        return results

    def decode_compound(self, datafield):
        # first variable field is indicators of all the subfields
        # all subfield indicators
        # --------------------------get indicators-------------
        indicator_octets = 0
        indicator_octetslen = 0
        while True:
            _b = self.bytes[self.p]
            self.p += 1
            indicator_octets = (indicator_octets << 8) + _b
            indicator_octetslen += 1

            if _b & 1 == 0:  # FX is zero
                break

        indicators = []
        mask = 1 << (8 * indicator_octetslen - 1)
        indicator = 1
        for i in range(0, 8 * indicator_octetslen):
            if i % 8 == 7:  # i is FX
                continue

            if indicator_octets & (mask >> i) > 0:
                indicators.append(indicator)

            indicator += 1

        # --------------------decode data------------------------
        results = {}
        index = 0
        for cn in datafield.childNodes:
            if cn.nodeName not in ['Fixed', 'Repetitive', 'Variable', 'Compound']:
                continue

            if index not in indicators:
                index += 1
                continue

            if cn.nodeName == 'Fixed':
                r = self.decode_fixed(cn)
            elif cn.nodeName == 'Repetitive':
                r = self.decode_repetitive(cn)
            elif cn.nodeName == 'Variable':
                r = self.decode_variable(cn)
            elif cn.nodeName == 'Compound':
                r = self.decode_compound(cn)

            index += 1
            results.update(r)

        return results
