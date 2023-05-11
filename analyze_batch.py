import json

filename = 'json/trial82.json'

with open(filename, 'r') as f:
    data = json.load(f)

print(f"{data['graph']}\n")
print(f"{data['Uniform Cost Search -- cost']}\n")
print(f"{data['A* Graph Search -- cost']}\n")