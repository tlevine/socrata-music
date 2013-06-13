#!/usr/bin/env python2
import os

def main():
    if not os.path.isdir('data'):
        print 'I expect a data directory containing the files from'
        print 'https://github.com/tlevine/socrata-download'
        exit(1)
