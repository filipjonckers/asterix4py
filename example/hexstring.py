import asterix4py

hex = '15004EFF9FB35B83E40001080001014CFBA315CD2A4A0EAF0AE69555250757D74CFB330005554CFBA31189374B4CFB3319CAC08341C60A00500C000000F500004CFBB3414175D75820006A06D901'
b = bytearray.fromhex(hex)
print('dec: ', memoryview(b).tolist())
print('hex: ', ['{:02X}'.format(i) for i in memoryview(b).tolist()])

decoder = asterix4py.AsterixParser(b)
print('decode: ', decoder.get_result())
