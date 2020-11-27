#!/usr/bin/env python
import pandas as pd

counties = {
    ('Jefferson', 'Pennsylvania'),
    ('Clearfield', 'Pennsylvania'),
    ('Los Angeles', 'California'),
}


def analyze(county):
    county['new'] = county['cases'].diff()
    county['new7'] = county['cases'].diff(periods=7)
    county['new28'] = county['cases'].diff(periods=28)

    mr = county.iloc[-1]
    title = f"{mr['county']} county, {mr['state']}"
    c = mr['cases']

    def pct(n):
        return '%.2f%%' % (n / c * 100)

    print(title)
    print('='*len(title))
    print(f"As of: {mr['date']}")
    print(f"Cumulative cases: {c}")
    print(f"New cases yesterday: {mr['new']}")
    print(f"Percent of all cases yesterday: {pct(mr['new'])}")
    print(f"Percent of all cases in the last week: {pct(mr['new7'])}")
    print(f"Percent of all cases in the last 28 days: {pct(mr['new28'])}")
    print("")

def load():
    return pd.read_csv('covid-19-data/us-counties.csv')

def run():
    df = load()
    for c, s in counties:
        analyze(df[df['state'] == s][df['county'] == c])

if __name__ == '__main__':
    run()
