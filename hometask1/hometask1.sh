#!/bin/bash 

py2='2.7.0'
py3='3.7.0'
pyenv install $py2
pyenv install $py3

pyenv virtualenv testenv_$py2
pyenv virtualenv testenv_$py3
