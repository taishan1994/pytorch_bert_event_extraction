import os
import json
from collections import defaultdict

labels = []
rolelabels = []
querylabels = {}
labels2rolelabels = defaultdict(list)
with open('event_schema.json', 'r') as fp:
    event_schema_data = fp.read().strip()
    for line in event_schema_data.split('\n'):
        line = eval(line)
        labels.append(line['event_type'])
        querylabels[line['event_type']] = ("找出和{}".format(line['event_type'])+"相关的属性")
        for role in line['role_list']:
          rolelabels.append(line['event_type']+'-'+role['role'])


with open('../final_data/labels.txt','w') as fp:
    for label in labels:
        fp.write(label + '\n')

with open('../final_data/rolelabels.txt','w') as fp:
    for rolelabel in rolelabels:
        fp.write(rolelabel + '\n')

with open('../final_data/labels2query.json','w') as fp:
    fp.write(json.dumps(querylabels, ensure_ascii=False))

for label in labels:
  for rolelabel in rolelabels:
    if label in rolelabel:
      labels2rolelabels[label].append(rolelabel)
with open('../final_data/labels2rolelabels.json','w') as fp:
    fp.write(json.dumps(labels2rolelabels, ensure_ascii=False))   
