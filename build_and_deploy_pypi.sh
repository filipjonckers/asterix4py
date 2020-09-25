#!/bin/zsh
# requires: pip install twine
rm -fr dist ;
rm -fr *.egg-info ;

python setup.py sdist ;
if twine check dist/* ; then
  if [ "$1" = "--test" ] ; then
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
  else
    twine upload dist/* ;
  fi
fi
