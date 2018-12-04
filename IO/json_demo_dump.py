import json
numbers = [2,3,4,5,6,8,9]

filename="d:/文档/个人/随手记/py/IO/json_demo.json"

with open(filename,'w',encoding='utf-8') as file:
    json.dump(numbers,file)