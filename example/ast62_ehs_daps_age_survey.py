import csv
import datetime
import sys
import time

import asterix4py

# Example code which I used to do a survey of the EHS DAP age to investigate the impact of reducing
# the interrogation schedule for EHS (FSS, IAS, MHG, ..) to optimize the 1030/1090 spectrum usage
# ref. 1030/1090 Monitoring Project - Eurocontrol NSUR
# author: Filip Jonckers - skeyes
####################################################################################################

FILE = '../sample/cat062.ast'
HEADER = ["timestamp", "TSE", "lat", "lon", "x", "y", "MFL", "ADR", "ACID", "SAL", "FSS", "MHG", "IAS", "IAR", "BPS", "age_MDS", "age_MFL", "age_FSS", "age_MHG", "age_IAR", "age_BPS"]

midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
start = time.perf_counter()

with open('daps_age.csv', mode='w') as outfile:
    out = csv.writer(sys.stdout, delimiter=';')
    #out = csv.writer(outfile, delimiter=';')
    out.writerow(HEADER)

    with open(FILE, 'rb') as astfile:
        data = astfile.read(3)
        while data:
            cat = data[0]
            length = int.from_bytes(data[1:3], byteorder='big', signed=True)
            data += astfile.read(length - 3)
            decoder = asterix4py.AsterixParser(data)

            # each plot/record of a frame has a sequence number
            for nr, plot in decoder.get_result().items():
                cat = plot.get('cat')
                if cat != 62:
                    continue

                # ignore if no DAP for this plot
                if not plot.get('295') or not plot['295'].get('FSS', ''):
                    continue

                data = [
                    f"{midnight + datetime.timedelta(seconds=plot['070']['ToT']):%H:%M:%S.%f}",
                    f"{plot['080'].get('TSE', 0)}"
                ]

                if plot.get('105'):
                    data.append(f"{plot['105']['Lat']:0<10.9}")
                    data.append(f"{plot['105']['Lon']:0<10.9}")
                else:
                    data.extend([""] * 2)

                if plot.get('100'):
                    data.append(f"{plot['100']['X']}")
                    data.append(f"{plot['100']['Y']}")
                else:
                    data.extend([""] * 2)

                if plot.get('136'):
                    data.append(f"{plot['136'].get('MFL', 0)}")
                else:
                    data.append("")

                if plot.get('380'):
                    data.append(f"{plot['380'].get('ADR', 0):06X}")
                    data.append(f"{plot['380'].get('ACID', '')}".rstrip())
                    data.append(f"{plot['380'].get('SAL', 0)}")
                    data.append(f"{plot['380'].get('FSS', 0)}")
                    data.append(f"{plot['380'].get('MHG', 0)}")
                    data.append(f"{plot['380'].get('IAS', 0)}")
                    data.append(f"{plot['380'].get('IAR', 0)}")
                    data.append(f"{800 + plot['380'].get('BPS', 0)}")
                else:
                    data.extend([""] * 5)

                if plot.get('290'):
                    data.append(f"{plot['290'].get('MDS', '')}")
                else:
                    data.append("")

                if plot.get('295'):
                    data.append(f"{plot['295'].get('MFL', '')}")
                    data.append(f"{plot['295'].get('FSS', '')}")
                    data.append(f"{plot['295'].get('MHG', '')}")
                    data.append(f"{plot['295'].get('IAR', '')}")
                    data.append(f"{plot['295'].get('BPS', '')}")
                else:
                    data.extend([""] * 4)

                out.writerow(data)

            data = astfile.read(3)
