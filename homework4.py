#!/usr/bin/env python
import requests
import argparse
import getpass
import datetime

parser = argparse.ArgumentParser()
parser.add_argument("--v", help="Shows version", action="store_true")
parser.add_argument("--c", help="Number of pull requests. Default count is 5. Set --c=<number>", type=int)
parser.add_argument("--u", help="Shows information about user", action="store_true")
parser.add_argument("--w", help="Shows week number", action="store_true")
parser.add_argument("--d", help="Shows day of week", action="store_true")
parser.add_argument("--h", help="Shows hours of day", action="store_true")
parser.add_argument("--s", help="Shows state", action="store_true")

args = parser.parse_args()

usr = input("Enter the name: ")
pwd = getpass.getpass("Enter the password: ")

r = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls?per_page=123', auth=(usr, pwd))

data = r.json()

if args.v:
    print("Release version of app is 1425")
    quit()

if args.c:
    count = args.c
else:
    count = 5

counter = 1
for i in range(count):
    user = '-'
    week = '-'
    day = '-'
    state = '-'
    hours = '-'
    name = data[i]['title']
    creation = data[i]['created_at'][:10]

    if args.u:
        user = data[i]['user']['login']

    if args.w:
        week = datetime.datetime.strptime(creation, '%Y-%m-%d').isocalendar()[1]

    if args.d:
        day = datetime.datetime.strptime(creation, '%Y-%m-%d').strftime('%A')

    if args.h:
        hours = (data[i]['created_at'][11:19])

    if args.s:
        state = data[i]['state']

    print("-----------------------")
    print("Number: {0}".format(counter))
    print("Request name: {0}".format(name))
    print("Request state: {0}".format(state))
    print("User: {0}".format(user))
    print("Creation time: {0}".format(creation))
    print("Number of week: {0}".format(week))
    print("Name week day: {0}".format(day))
    print("Hours of creation: {0}".format(hours))
    print('-----------------------')
    counter += 1
