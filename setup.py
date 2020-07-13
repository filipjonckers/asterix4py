import pathlib
import shutil

from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '1.0.1'
PYTHON_REQUIRES = '>=3.7'
PACKAGE_NAME = 'asterix4py'
AUTHOR = 'Filip Jonckers'
AUTHOR_EMAIL = ''
URL = 'https://github.com/filipjonckers/asterix4py'
LICENSE = 'MIT License'
DESCRIPTION = 'Pure python library for decoding Eurocontrol Asterix binary data'
KEYWORDS = 'asterix radar artas eurocontrol mode-s'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"
CLASSIFIERS = [
      'Development Status :: 3 - Alpha',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8',
      'Intended Audience :: Developers',
      'Intended Audience :: Information Technology',
      'Intended Audience :: Science/Research',
      'Operating System :: MacOS',
      'Operating System :: Microsoft :: Windows',
      'Operating System :: POSIX :: Linux',
      'License :: OSI Approved :: MIT License',
      'Topic :: Software Development',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'Topic :: Scientific/Engineering',
      'Topic :: Scientific/Engineering :: Information Analysis',
      'Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator'
]

PROJECT_URLS = {
      'Bug Reports': 'https://github.com/filipjonckers/asterix4py/issues',
      'Source': 'https://github.com/filipjonckers/asterix4py'
}

INSTALL_REQUIRES = [
]

try:
    shutil.rmtree("./build")
except(OSError):
    pass

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      keywords=KEYWORDS,
      classifiers=CLASSIFIERS,
      install_requires=INSTALL_REQUIRES,
      python_requires=PYTHON_REQUIRES,
      project_urls=PROJECT_URLS,
      platforms=['any'],
      include_package_data=True,
      zip_safe=False,
      packages=find_packages()
      )
