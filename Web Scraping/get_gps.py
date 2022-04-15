import csv
import requests
import urllib.parse
from tqdm import tqdm

api_key = input("API access key for positionstack.com: ")

with open('features_no_gps.csv', newline='') as csvfile:
    rows = [i for i in csv.reader(csvfile)]
colnames = rows[0] + ['latitude', 'longitude']
data_rows = rows[1:]

for i in tqdm(data_rows):
    params = urllib.parse.urlencode({
        'access_key': api_key,
        'query': i[1],
        'country': "SG",
        'limit': 1
    })
    r = requests.get("http://api.positionstack.com/v1/forward?{}".format(params))
    if r.status_code == 200:
        r_results = r.json()['data']
        if r_results:
            r_result = r_results[0]
            i.append(r_result['latitude'])
            i.append(r_result['longitude'])

print(data_rows[0])

with open('../Data/features.csv', mode='w', newline="", encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(colnames)
    writer.writerows(data_rows)