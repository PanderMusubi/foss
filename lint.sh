#!/usr/bin/env sh

echo '* CHECKBASHISMS'
checkbashisms *.sh

. .venv/bin/activate
FILES=*.py
echo '* PYDOCSTYLE'
pydocstyle --convention=numpy $FILES
echo '* FLAKE8'
flake8 --ignore E501 $FILES
echo '* PYLINT'
pylint $FILES
echo '* PYFLAKES3'
pyflakes $FILES
echo '* PYRIGHT-ALRIGHT'
pyright-alright $FILES
echo '* MYPY'
mypy $FILES
