import json

def load_profile(filename):
    try:
        with open(filename,'r') as file:
            data = json.load(file)
        name = data.get("Name", "User")
        age = data.get("Age", "unknown")
        city = data.get("City", "an unknown city")

        print(f" hello {name}, you are {age} years old and live in {city} ")
    except FileNotFoundError:
        print("error the file {filename} was not found")
    except json.JSONDecodeError:
        print("error the file was not found")
load_profile("user_profile.json")