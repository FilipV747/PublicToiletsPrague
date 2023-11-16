import json
path = 'toilets_data.json'
with open(path, encoding='UTF-8') as soubor:
    data = json.load(soubor)
    unique_otevreno = set()
    for feature in data['features']:
        otevreno = feature['properties']['OTEVRENO']
        unique_otevreno.add(otevreno)

for schedule in unique_otevreno:
    print(schedule)

print(len(unique_otevreno))