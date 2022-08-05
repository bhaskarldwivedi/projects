import csv
import json
import requests
import pandas as pd
from csv import DictReader
from pprint import pprint

Num_of_rows = len(pd.read_csv('Firewall.csv'))
# print(Num_of_rows)

with open("FirewallL3rules.txt", "a") as file1:
    file1.write("""
{"rules":
[""")
    file1.write("\n")
with open('Firewall.csv', 'r') as read_obj:
    # pass the file object to DictReader() to get the DictReader object

    i = 0
    csv_dict_reader = DictReader(read_obj)
    # iterate over each line as a ordered dictionary
    for row in csv_dict_reader:
        # row variable is a dictionary that represents a row in csv
        with open("FirewallL3rules.txt", "a") as file1:
            file1.write(json.dumps(row))

            if i != Num_of_rows - 1:
                file1.write(""",""")
                file1.write("\n")
        i = i + 1
    with open("FirewallL3rules.txt", "a") as file1:
        file1.write("""
]
}""")
file1.close()
