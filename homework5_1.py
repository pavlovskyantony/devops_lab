#!/usr/bin/env python

import json
from datetime import datetime
import yaml
import platform
import sys
import pip
import os
from pip._internal.operations.freeze import freeze
import site

# 1 version
py_ver = platform.python_version()

# 2 pyenv
py_env = sys.prefix

# 3 executable
py_exec = sys.executable

# 4 pip location
pip_loc = pip.__path__

# 5 path to PYTHONFILE
py_path = os.environ['PYTHONPATH'].split(os.pathsep)

# 6 Installet packets and their versions
py_pack = []
for requirement in freeze(local_only=True):
    py_pack.append(requirement)

# 7 Package locations
pack_loc = site.getsitepackages()

if __name__ == "__main__":
    py_info = {'python': []}
    py_info['python'].append({
        'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'Python version': py_ver,
        'Python environment:': py_env,
        'Python executable location:': py_exec,
        'PIP location': pip_loc,
        'PYTHONPATH': py_path,
        'Installed packages': py_pack,
        'site-packages location': pack_loc
    })
with open('PythonInfo.json', 'w+') as json_f:
    json.dump(py_info, json_f)

with open('PythonInfo.yml', 'w+') as yaml_f:
    yaml.dump(py_info, yaml_f, allow_unicode=True)
