import csv
import requests
m=['car','automobile','brand','vehicle','vehicles']
S = requests.Session()
d=[]
f = open('newbrand.csv', 'a')
with f:
    fnames = ['Part_Brand_id', 'Part Brand Name','Part_Brand_name_Tags','desc','Part_Brand_Type','Oem_id']
    writer = csv.DictWriter(f, fieldnames=fnames)
    writer.writeheader()
    f.close()
with open('brand.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    #writer = csv.DictWriter(csvfile)
    for row in reader:
        print(row['Part Brand Name'])
        d.append(row['Part Brand Name'])
        URL = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles="
        R = S.get(url=URL+row['Part Brand Name'])
        DATA = R.json()
        key = list(DATA['query']['pages'].keys())[0]
        if 'extract' in DATA['query']['pages'][key].keys():
            for i in m:
                if i in DATA['query']['pages'][key]['extract']:
                    #row['desc'] = DATA['query']['pages'][key]['extract']
                    print(DATA['query']['pages'][key]['extract'])
                    f = open('newbrand.csv', 'a')
                    with f:
                        fnames = ['Part_Brand_id', 'Part Brand Name','Part_Brand_name_Tags','desc','Part_Brand_Type','Oem_id']
                        writer = csv.DictWriter(f, fieldnames=fnames)
                        writer.writerow({'Part_Brand_id': row['Part_Brand_id'], 'Part Brand Name': row['Part Brand Name'],'Part_Brand_name_Tags':row['Part_Brand_name_Tags'],'desc':DATA['query']['pages'][key]['extract'],'Part_Brand_Type':row['Part_Brand_Type'],'Oem_id':row['Oem_id']})
                    f.close()
                    #writer.writerow({row['desc']:DATA['query']['pages'][key]['extract'] })
                    print(DATA['query']['pages'][key]['extract'])
                    break
