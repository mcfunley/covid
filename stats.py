#!/usr/bin/env python
from csv import DictReader
from collections import defaultdict


def analyze(cases):
    title = f"{cases[0]['county']}, {cases[0]['state']}"
    print(title)
    print('='*len(title))




counties = {
    ('Jefferson', 'Pennsylvania'),
    ('Clearfield', 'Pennsylvania'),
    ('Los Angeles', 'California'),
}

data = defaultdict(list)
with open('covid-19-data/us-counties.csv', 'r') as f:
    for d in DictReader(f):
        c = (d['county'], d['state'])
        if c in counties:
            data[c].append(d)

for c in counties:
    analyze(data[c])
