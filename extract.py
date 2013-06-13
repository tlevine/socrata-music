#!/usr/bin/env python2
import os
import string
import csv

DATA = 'data'
OUTPUT_FILE = open('socrata.csv', 'w')
OUTPUT_FIELDS = ['portal', 'id']

def main():
    'IO ()'
    if not os.path.isdir(DATA):
        print 'I expect a data directory containing the files from'
        print 'https://github.com/tlevine/socrata-download'
        exit(1)

    c = csv.DictWriter(OUTPUT_FILE, OUTPUT_FIELDS)

    for portal in portals()[:3]:
        view_dir = os.path.join(DATA, portal, 'views')
        for view_id in os.listdir(view_dir):
            row = read_view(os.path.join(view_dir, view_id))
            row['portal'] = portal
            c.writerow(row)

    OUTPUT_FILE.close()

def portals():
    'IO () -> [unicode]'
    return filter(lambda d: d[0] in string.ascii_letters, os.listdir(DATA))

def read_view(view_path):
    return {'id':'abcd-efgh'}


if __name__ == '__main__':
    main()
