import csv 
import json
def csv_to_json(csv_path, json_path):
    data = []
    #read csv
    with open(csv_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    #write json
    with open(json_path, mode= "w") as json_file:
        json.dump(data, json_file, indent=4)
csv_to_json("/home/mirafra/Desktop/python_learnings/practice_prep/csv.csv", "products.json")