import json

load_dict=None

with open("D:/文档/code/python/trade/goods_info/static/goods/data/world.json","r") as f:
    load_dict = json.load(f)
    print("加载入文件完成...")

clist = load_dict['features']

namelist = []
for c in clist:
    namelist.append(c['properties']['name'])

print(namelist)
