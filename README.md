# asterix4py

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
[![GitHub release](https://img.shields.io/github/release/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/releases/)
[![GitHub contributors](https://img.shields.io/github/contributors/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/issues/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)




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
