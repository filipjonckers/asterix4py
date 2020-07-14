import datetime

import asterix4py

b = open('../sample/cat062.ast', 'rb').read()
decoder = asterix4py.AsterixParser(b)
print('decode: ', decoder.get_result())

midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

for cat, plotlist in decoder.get_result().items():
    for plot in plotlist:
        print(
            f"cat{cat:03d}"
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
                f" s:{plot['380'].get('ADR'):06X}"
                f" acid:{plot['380'].get('ACID')}"
                f" fss:{plot['380'].get('FSS')}"
                f" gsp:{plot['380'].get('GSP')}"
                f" ias:{plot['380']['IAS']}"
            , end='')

        if plot.get('390'):
            print(
                f" cs:{plot['390'].get('ADR')}"
                f" type:{plot['390'].get('TYPE')}"
                f" wtc:{plot['390'].get('WTC')}"
                f" adep:{plot['390'].get('DEP')}"
                f" ades:{plot['390'].get('DES')}"
                f" cfl:{plot['390'].get('CFL')}"
            , end='')
        print('')