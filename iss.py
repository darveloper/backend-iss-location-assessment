#!/usr/bin/env python

import requests
import json

__author__ = 'Darlyze Calixte'
def part_a():
    r = requests.get('http://api.open-notify.org/astros.json')
    data = r.text
    parsed = json.loads(data)
    name = parsed["people"][1]["name"]
    spacecraft = parsed["people"][1]["craft"]
    totalnum = parsed["number"]
    print(name + " " + spacecraft + " " + str(totalnum))

def part_b():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    data = r.text
    parsed = json.loads(data)
    coordinates = parsed["iss_position"]
    timestamp = parsed["timestamp"]
    print(coordinates)
    print(timestamp)

def main():
    part_a()
    part_b()


if __name__ == '__main__':
    main()
