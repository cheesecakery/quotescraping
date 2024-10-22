import json 

with open('quotesData.json') as json_data:
    jsonData = json.load(json_data)

authors = []
authors = list(map(lambda a: a["author"], jsonData))

counts = dict()
for i in authors:
    counts[i] = counts.get(i, 0) + 1

topQuoters = sorted(counts, key=counts.get, reverse=True)[:3]
print(topQuoters)
print(len(jsonData))