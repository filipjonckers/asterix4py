import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '1.0.1'
PACKAGE_NAME = 'asterix4py'
AUTHOR = 'Filip Jonckers'
AUTHOR_EMAIL = 'jof@skeyes.be'
URL = 'https://github.com/filipjonckers/asterix4py'
LICENSE = 'MIT License'
DESCRIPTION = 'Pure python library for decoding Eurocontrol Asterix binary data'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'gzip',
      'json'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )

