import csv
import json
import requests
import pandas as pd
from csv import DictReader
from pprint import pprint

Num_of_rows = len(pd.read_csv('Firewall.csv'))
# print(Num_of_rows)

filecontent = """
{"rules":
["""

filecontent = filecontent + "\n"
with open('Firewall.csv', 'r') as read_obj:
    # pass the file object to DictReader() to get the DictReader object

    i = 0
    csv_dict_reader = DictReader(read_obj)
    # iterate over each line as a ordered dictionary
    for row in csv_dict_reader:
        # row variable is a dictionary that represents a row in csv
        filecontent = filecontent + json.dumps(row)
        if i != Num_of_rows - 1:
            filecontent = filecontent + ""","""
            filecontent = filecontent + "\n"
        i = i + 1
    filecontent = filecontent + """
]
}"""
print(filecontent)
url = "https://api.meraki.com/api/v1/networks/L_698057942242449369/appliance/firewall/l3FirewallRules"
headers = {
    'X-Cisco-Meraki-API-Key': 'fd9ddd4319105ce332da6cc0ec92f6b0df1e6767',
    'Content-Type': 'application/json',
    'Accept-Encoding': '*'}

response = requests.request(
    "PUT", url, headers=headers, data=filecontent)

print(response)
