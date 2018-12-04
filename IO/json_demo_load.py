import json

filename="d:/文档/个人/随手记/py/IO/json_demo.json"

with open(filename,'r',encoding='utf-8') as file:
    numbers = json.load(file)

print(numbers)