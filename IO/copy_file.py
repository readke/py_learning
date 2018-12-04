'''
复制文件
'''

source_path = 'd:/文档/个人/随手记/py/IO/message.txt'
target_path = 'd:/文档/个人/随手记/py/IO/message_bak.txt'

with open(source_path) as source_object:
    lines = source_object.readlines()


with open(target_path,'w') as target_object:
    target_object.writelines(lines)
