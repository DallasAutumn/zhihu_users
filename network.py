import networkx as nx
import json
import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt

data = []
with open('zhihu.json', 'r') as f:
    for line in f.readlines():
        data.append(json.loads(line))

start = [each.get('name') for each in data]
end = [each.get('relations') for each in data]

edges = []
for u in start:
    for v in end:
        if v:
            for each in v:
                edges.append((u, v))

print(edges)
