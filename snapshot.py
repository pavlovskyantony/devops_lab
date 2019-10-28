#!/usr/bin/env python

from mymodules import ServerPerformance as S
from datetime import datetime
import configparser
import json
import time

Server = S.ServerPerformance

config = configparser.ConfigParser()
config.read('config.ini')


def runsnapshot():
    interval = int(config['common']['interval']) * 60
    while True:
        if config['common']['output'] == 'txt':
            with open("metrics.txt", "a+") as out:
                out.write("Timestamp: {0} \n\n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                out.write("Hostname: {0} \n".format(Server().overallinfo()[1]))
                out.write("System/OS: {0} \n".format(Server().overallinfo()[0]))
                out.write("Platform: {0} \n".format(Server().overallinfo()[2]))
                out.write("CPU numbers: {0} \n".format(Server().cpu()[0]))
                out.write("Per CPU load: {0} \n".format(Server().cpu()[1]))
                out.write("Overall physical memory: {0} \n".format(Server().Memory()))
                out.write("Overall virtual memory usage: {0} \n".format(Server().VirtualMemory()))
                out.write("Total disk space (Gb): {0} \n".format(Server().IOinf()[0]))
                out.write("Usage disk space (Gb): {0} \n".format(Server().IOinf()[1]))
                out.write("Free disk space (Gb): {0} \n".format(Server().IOinf()[2]))
                out.write("Amount of recieved pkts: {0} \n".format(Server().Network()[0]))
                out.write("Amount of sent pkts: {0} \n".format(Server().Network()[1]))

        elif config['common']['output'] == 'json':
            metrics = {'server': []}
            metrics['server'].append({
                'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'Hostname': Server().overallinfo[1],
                'System/OS:': Server().overallinfo()[1],
                'Platform:': Server().overallinfo()[1],
                'CPU numbers': Server().cpu[0],
                'per CPU load': Server().cpu()[1],
                'Overall physical memory': Server().Memory(),
                'Overall virtual memory usage': Server().VirtualMemory(),
                'Total disk space (Gb)': Server().IOinf()[0],
                'Usage disk space (Gb)': Server().IOinf()[1],
                'Free disk space (Gb)': Server().IOinf()[2],
                'Amount of recieved pkts': Server().Network()[0],
                'Amount of sent pkts': Server().Network()[1]
            })
            with open('metrics.json', 'a+') as json_f:
                json.dump(metrics, json_f)
        time.sleep(interval)


if __name__ == "__main__":
    runsnapshot()
