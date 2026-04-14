car = { "brand": "Ford", "model" : "Mustang", "year" : 2024}

print(car.get("model")) #print(car["model"])
car["color"] = "red"
car.pop("brand")
print(car)