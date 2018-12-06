def getList():
    url = 'area.txt'

    with open(url,'r',encoding='utf-8') as file:
        lines= file.readlines()
    list = []    
    for line in lines:
        str = line.rstrip().split(",")
        list.append(str)

    return list

