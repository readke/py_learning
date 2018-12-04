'''
    文件后添加内容
'''

filename = 'd:/文档/个人/随手记/py/IO/message.txt'

with open(filename,'a') as file_object:
    file_object.write("I like java , it is preciseness.\n")
    file_object.write("I like python too, because it is succinct.\n")