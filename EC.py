import os
import sys
from sodapy import Socrata
import requests 
import json
from datetime import datetime
from elasticsearch import Elasticsearch
from time import sleep
import argparse

#create index
def create_and_update_index(index_name):
    es = Elasticsearch()
    try:
        es.indices.create(index=index_name)
    except Exception:
        pass
    return es
#format data
def data_format(datafile):
    for key, value in datafile.items():
        if 'amount' in key:
            datafile[key] = float(value)
        elif 'number' in key:
            datafile[key] = int(value)            
        elif 'date' in key:
            datafile[key] = datetime.strptime(datafile[key], '%m/%d/%Y').date()
#update data
def update(datafile, es, index):
    data_format(datafile)
    id=datafile['summons_number']
    output = es.index(index=index, body=datafile, id=id)
    print(output['result'], 'Summons_# %s' % id)

DATA_URL = "data.cityofnewyork.us"
DATA_ID = 'nc67-uf89'

app_key = os.environ.get("APP_TOKEN")
client = Socrata(DATA_URL, app_key)
results_filter = str(client.get(DATA_ID, limit=1000))

ALL = int(client.get(DATA_ID, select='COUNT(*)')[0]['COUNT'])
print(ALL)

metadata = client.get_metadata(DATA_ID)
[x['name'] for x in metadata['columns']]

#call output
def get_results(page_size, num_pages = None, output = None, elastic_search = None) -> dict:

    if not num_pages:
        num_pages = ALL // page_size + 1
    if elastic_search:
        es = create_and_update_index('project1')
    try:
        
        for i in range(num_pages):
            
            records = client.get(DATA_ID, limit=page_size, offset=i*page_size)
            print(records)
            if output is not None:
                with open(output, "a") as file:
                    for j in records:
                        file.write(f"{json.dumps(j)}\n")
            if elastic_search:
                update(j, es, 'project1')
    except HTTPError as e:
        print(f"Evaluate the loops again!: {e}")
        raise

parser = argparse.ArgumentParser()
if __name__ == "__main__":

    parser.add_argument("--page_size", type=int)
    parser.add_argument("--num_pages", type=int)
    parser.add_argument("--output")
    parser.add_argument("--elastic_search", type=bool)
    args = parser.parse_args()
    get_results(args.page_size, args.num_pages, args.output, args.elastic_search)
    sleep(30)
