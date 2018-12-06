import requests
import arae 


    #url='https://geo.datav.aliyun.com/areas/bound/100000.json'
    
def create_file(url,content):
    with open(url,'w',encoding='utf-8') as file:
        
        file.write(content)

def handler():
    list = arae.getList()
    url_perfix='https://geo.datav.aliyun.com/areas/bound/'
    url_suffix='.json'
    save_path_perfix = "d:/json/"
    for str in list:
        url = url_perfix + str[0] + url_suffix
        req = requests.get(url)
        content = req.text
        save_path = save_path_perfix + str[0]+'_'+str[1] + '.json'
        create_file(save_path,content)

handler()    