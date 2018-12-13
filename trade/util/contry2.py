from __future__ import unicode_literals
import json

surl = 'd:/en_zh.json'
turl = 'd:/en.json'
with open(turl,'r',encoding='utf-8') as f:
    tc = json.load(f)

with open(surl,'r',encoding='utf-8') as f2:
    sc = json.load(f2)

result={}
for key in tc.keys() :
    if key  in sc :
        #print( key +","+sc[key])
        result[key] = sc[key]
print(result)
resulturl = 'd:/result.json'


with open(resulturl,'w',encoding='utf-8') as fr:
    json.dump(result,fr,ensure_ascii=False)

result_not={}
for key in tc.keys():
    if key not in sc:
        result_not[key] = ''
result_not_in_url = 'd:/result_not_in.json'

with open(result_not_in_url,'w',encoding='utf-8') as fr:
    json.dump(result_not,fr,ensure_ascii=False)