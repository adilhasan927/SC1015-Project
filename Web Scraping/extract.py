import os
import os.path
from bs4 import BeautifulSoup as bs
import json
from tqdm import tqdm
import csv

#where our restaurant pages reside
path_start = r"websites\sg.openrice.com\en\singapore\\"
#get the path of each index.html file
filepaths = [path_start + i + '\index.html' for i in os.listdir(path_start)\
    if os.path.exists(path_start + i + '\index.html')]

colnames = ['name', 'street_address', 'price', 'cuisine', 'rating']
rows = []
for i in tqdm(filepaths):
    with open(i, 'r', encoding='utf-8') as file:
        try:
            soup = bs(file, features="html.parser")
            rating = val.string.strip() if ((val := soup.find(itemprop='ratingValue')) != None)\
                else None
            other_stuff = json.loads(soup.find(type="application/ld+json").string)
            vals = [other_stuff['name'],
                    other_stuff['address']['streetAddress'],
                    other_stuff['priceRange'],
                    other_stuff['servesCuisine'],
                    rating]
            rows.append(vals)
        except Exception as err:
            print("file could not be parsed: {}\nError: {}".format(i, err))

with open('features_no_gps.csv', mode='w', newline="", encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(colnames)
    writer.writerows(rows)