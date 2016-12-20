#!/usr/bin/env python3
"""Gets today's exchange rates from Yahoo Finance and saves them as CSV.

Run with --help for usage.

Find the latest version at https://gist.github.com/AnotherKamila/ef5721d911c9e898b05ef144f38a6d93
"""

import datetime
import io
import os
import tempfile
import sys

import click
from parse import parse
import requests
import tablib
import xmltodict

API_URL = 'https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote'
BASE_CURRENCY = 'USD'

def parsexml(text):
    # I love unstructured strings inside XML containers...
    doc = xmltodict.parse(text)
    for r in doc['list']['resources']['resource']:
        name, price = None, None
        for field in r['field']:
            if field['@name'] == 'name':  name  = field['#text']
            if field['@name'] == 'price': price = field['#text']
        if name == 'USD': name = 'USD/USD'  # WHY can't they make the stuff uniform?
        parsed_name = parse('{base}/{name}', name)
        if not parsed_name:
            # click.echo('{} not a currency, skipping'.format(name), err=True)
            continue
        currency = parsed_name.named
        currency['price'] = price
        yield currency

def mknone(*_, **__):
    return None

def extend_dataset(data, new_values, index=0):
    for k, v in new_values.items():
        if k not in data.headers:
            if data.height:
                data.append_col(mknone, header=k)
            else:
                data.headers.append(k)
    data.insert(index, [new_values.get(k) for k in data.headers])

##### commands ################################################################

@click.command()
@click.argument('file', type=click.Path(dir_okay=False, writable=True,
                                        resolve_path=True, allow_dash=True))
@click.option('--api-url', default=API_URL, type=str,
    help='Where to retrieve data. Must resemble the API at {}'.format(API_URL))
def run(file, api_url):
    """Gets today's exchange rates from Yahoo Finance and saves them as CSV.

    "Smart appends" the file: if it exists, it reads it, expands the set of
    columns to the union of old and new stuff, and writes everything back.
    It promises to always produce a correct CSV.
    """
    with (sys.stdout if file == '-' else open(file+'.tmp', 'w')) as writeme:
        data = tablib.Dataset()

        # copy over any old data
        if file != '-':
            try:
                old_data = data.load(open(file).read())
            except:
                pass  # lalala

        # add new data
        if not data.headers: data.headers = ['Date']
        new = {'Date': datetime.date.today().isoformat()}
        for currency in parsexml(requests.get(api_url).text):
            assert(currency['base'] == BASE_CURRENCY)  # for now we just hope...
            new[currency['name']] = currency['price']
        extend_dataset(data, new)

        # write the file and move it over the old one
        writeme.write(data.csv)
        writeme.flush()
        if file != '-': os.rename(writeme.name, file)

##### main ####################################################################

if __name__ == '__main__':
    run()
