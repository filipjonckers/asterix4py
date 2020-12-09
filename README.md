# asterix4py

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub license](https://img.shields.io/github/license/filipjonckers/asterix4py)](https://github.com/filipjonckers/asterix4py/blob/master/LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![GitHub contributors](https://img.shields.io/github/contributors/filipjonckers/asterix4py)](https://github.com/filipjonckers/asterix4py/graphs/contributors)

[![GitHub release](https://img.shields.io/github/workflow/status/filipjonckers/asterix4py/Publish%20package%20to%20PyPi?style=flat-square)](https://github.com/filipjonckers/asterix4py/releases)
[![GitHub release](https://img.shields.io/github/v/release/filipjonckers/asterix4py)](https://github.com/filipjonckers/asterix4py/releases)
[![GitHub releasedate](https://img.shields.io/github/release-date/filipjonckers/asterix4py)](https://github.com/filipjonckers/asterix4py/releases)
[![GitHub issues](https://img.shields.io/github/issues/filipjonckers/asterix4py)](https://github.com/filipjonckers/asterix4py/issues)


Pure python library for parsing/decoding EUROCONTROL ASTERIX protocol binary data.

This library tries to be an easy way to use Python as Asterix decoder without the need of a big library. Focus is currently not yet on speed but to be simple and userfriendly.
The code is based on the discontinued code from Wontor, adding missing functionalities and several bugfixes.  Some simple code examples and Asterix sample files are included for testing purposes only.

This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to contribute and/or redistribute it under certain conditions.


## Asterix

ASTERIX stands for All Purpose STructured EUROCONTROL SuRveillance Information EXchange. It is an ATM Surveillance Data Binary Messaging Format which allows transmission of harmonised information between any surveillance and automation system. ASTERIX defines the structure of the data to be exchanged over a communication medium, from the encoding of every bit of information up to the organisation of the data within a block of data - without any loss of information during the whole process. More about ASTERIX protocol you can find here: http://www.eurocontrol.int/services/asterix


## References

Based on the work of:
- Wontor - https://github.com/wontor/pyasterix
- Damir Salantic - https://github.com/CroatiaControlLtd/asterix


## Contributors
- Jake Hawkins - https://github.com/drumlight
