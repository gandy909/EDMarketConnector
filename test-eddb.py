#!/usr/bin/env python

import argparse
import requests
import csv
import json

parser = argparse.ArgumentParser(description='Utilises eddb.io data files to produce... FIXME')
parser.add_argument('-S', '--systems-file', help="Specify a local file copy of eddb.io's systems.csv")
parser.add_argument('-s', '--stations-file', help="Specify a local file copy of eddb.io's stations.json")
args = parser.parse_args()

def load_file(filename):
    if filename == 'systems.csv' and args.systems_file:
        print('load_file: systems.csv from local file')
        return open(args.systems_file, newline='')
    elif filename == 'stations.json' and args.stations_file:
        print('load_file: stations.json from local file')
        stations = []
        with open(args.stations_file) as jsonl_file:
            for l in jsonl_file:
                stations.append(json.loads(l))
        return stations
    else:
        raise AssertionError('load_file called with unsupported filename')

if args.systems_file:
	systems = { int(s['id']) : {
    	'name'          : s['name'],
    	'x'            : float(s['x']),
    	'y'            : float(s['y']),
    	'z'            : float(s['z']),
    	'is_populated' : int(s['is_populated'])
	} for s in csv.DictReader(load_file('systems.csv')) }

if args.stations_file:
	# station_id by (system_id, station_name)
	stations = load_file('stations.json')    # let json do the utf-8 decode
	station_ids = {
    		(x['system_id'], x['name']) : x['id']   # Pilgrim's Ruin in HR 3005 id 70972 has U+2019 quote
    		for x in stations if x['max_landing_pad_size']
	}

