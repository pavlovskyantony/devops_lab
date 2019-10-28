DevOps Lab 2019 (September-December)

Homework3 snapshot app

install:
- You need copy required files (setup.py, snapshot.py, config.ini, LICENSE)
- Make .whl build file (command: python setup.py bdist_wheel)
- .whl file will compiled in dist folder
- Install this .whl file by using pip install dist/snapshot-0.0.1-py3-none-any.whl
- Run this application (python && import snapshot && snapshot.runsnapshot)
- For terminate. you need press "Ctrl + D"
- App collects metrics every 5 minutes by default. You may change this interval in config.ini file
- All collected metrics by this app will putted in metrics.txt or metrics.json file. You may change format in config.ini file
- metrics.txt or metrics.json will locate in directory where you run the snapshot App

uninstall:
- pip uninstall snapshot
