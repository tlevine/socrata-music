#!/usr/bin/env python2
import os
import string
import csv
import json
from unidecode import unidecode

DATA = 'data'
OUTPUT_FILE = open('socrata.csv', 'w')
OUTPUT_FIELDS = [
    # Identity
    u'portal',
    u'id',
    u'name',
    u'description',

    # Dates
    u'createdAt',
    u'publicationDate',
    u'viewLastModified',
    u'rowsUpdatedAt',

    # Structure
    u'displayType',
    u'viewType',
    u'columns',

    # Usage
    u'viewCount',
    u'numberOfComments',
    u'totalTimesRated',
    u'downloadCount',
    u'averageRating',

    # Provenance
    u'rowsUpdatedBy',
    u'attribution',
    u'tableAuthor.roleName',
    u'owner.displayName',
    u'owner.screenName',
    u'owner.roleName',
    u'tableAuthor.screenName',

    # Location
    u'northWest.long',
    u'northWest.lat',
    u'southEast.long',
    u'southEast.lat',

    # Other
    u'category',
    u'state',
    u'tags',
]

def main():
    'IO ()'
    if not os.path.isdir(DATA):
        print 'I expect a data directory containing the files from'
        print 'https://github.com/tlevine/socrata-download'
        exit(1)

    c = csv.DictWriter(OUTPUT_FILE, OUTPUT_FIELDS)

    for portal in portals()[:3]:
        view_dir = os.path.join(DATA, portal, u'views')
        for view_id in os.listdir(view_dir):
            row = read_view(os.path.join(view_dir, view_id))
            row[u'portal'] = portal
            for k,v in row.items():
                if isinstance(v, basestring):
                    row[k] = unidecode(v)
                elif type(v) in {dict,list}:
                    row[k] = json.dumps(v)
            c.writerow(row)

    OUTPUT_FILE.close()

def portals():
    'IO () -> [unicode]'
    return filter(lambda d: d[0] in string.ascii_letters, os.listdir(DATA))

def read_view(view_path):
    handle = open(view_path, 'r')
    view = _flatten(json.load(handle))

    # Limit fields
    for key in view.keys():
        if key not in OUTPUT_FIELDS:
            del(view[key])

    return view


def _nested_dict_iter(nested, sep):
    for key, value in nested.iteritems():
        if hasattr(value, 'iteritems'):
            for inner_key, inner_value in _nested_dict_iter(value, sep):
                yield key + sep + inner_key, inner_value
        else:
            yield key, value

def _flatten(nested, sep = '.'):
    '''
    dict -> dict
    Flatten a dictionary, replacing nested things with dots.
    '''
    return dict(_nested_dict_iter(nested, sep))

if __name__ == '__main__':
    main()
