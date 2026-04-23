# /home/mirafra/Desktop/python_learnings/practice_prep/csv/json_demo.json
import json
from datetime import date
def update_config(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    #modification
    data['settings']['theme'] = 'dark'
    data['last_updated'] = str(date.today()) 
    #updating
    with open (filename, 'w') as file:
        json.dump(data, file, indent =4 )  
# update_config("/home/mirafra/Desktop/python_learnings/practice_prep/csv/json_demo.json")
update_config("json_updated_data.json")    
 