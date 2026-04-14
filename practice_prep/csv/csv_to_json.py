import csv
import json

def csv_to_json(csv_file, json_file):
    data = []

    with open (csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            data.append(row)
    with open (json_file, mode = 'w') as file:
        json.dump(data, file,indent=4)
csv_to_json("/home/mirafra/Desktop/python_learnings/csv.csv","data.json")




 