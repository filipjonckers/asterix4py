import datetime
import time

import asterix4py

FILE = '../sample/cat062.ast'

midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
start = time.perf_counter()

with open(FILE, 'rb') as astfile:
    data = astfile.read(3)
    while data:
        cat = data[0]
        length = int.from_bytes(data[1:3], byteorder='big', signed=True)
        data += astfile.read(length - 3)
        # print('hex: ', ['{:02X}'.format(i) for i in memoryview(data).tolist()])
        decoder = asterix4py.AsterixParser(data)
        # print('decode: ', decoder.get_result())

        # each plot/record of a frame has a sequence number
        for nr, plot in decoder.get_result().items():
            cat = plot.get('cat')
            if cat != 62:
                continue

            print(
                f"{nr:d} cat{cat:03d}"
                f" tot:{midnight + datetime.timedelta(seconds=plot['070']['ToT']):%H:%M:%S.%f}"
                , end='')

            if plot.get('105'):
                print(
                    f" lat:{plot['105']['Lat']:0<10.9}"
                    f" lon:{plot['105']['Lon']:0<10.9}"
                , end='')

            if plot.get('060'):
                print(
                    f" a:{plot['060']['Mode3A']}"
                , end='')

            if plot.get('380'):
                print(
                    f" s:{plot['380'].get('ADR', 0):06X}"
                    f" acid:{plot['380'].get('ACID', '')}"
                    f" fss:{plot['380'].get('FSS', 0)}"
                    f" gsp:{plot['380'].get('GSP', 0)}"
                    f" ias:{plot['380'].get('IAS', 0)}"
                , end='')

            if plot.get('390'):
                print(
                    f" cs:{plot['390'].get('CS', '')}"
                    f" type:{plot['390'].get('TYPE', '')}"
                    f" wtc:{plot['390'].get('WTC', '')}"
                    f" adep:{plot['390'].get('DEP', '')}"
                    f" ades:{plot['390'].get('DES', '')}"
                    f" cfl:{plot['390'].get('CFL', 0)}"
                , end='')
            print('')

        data = astfile.read(3)

end = time.perf_counter()
print(f">>> processing time: {end - start:0.4f} secs.")
