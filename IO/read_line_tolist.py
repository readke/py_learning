'''
将文件内容读到一个列表中
'''
path = 'd:/文档/个人/随手记/py/IO/pi_million_digits.txt'

with open(path) as file_object:
    lines = file_object.readlines()

#for line in lines :
#    print(line)

#print(lines)
pi = ''

for line in lines :
    pi += line.rstrip()

#print('pi = '+pi[:52])
#print(len(pi))
birthday = input("enter your birthday , in the form mmddyy: ")
if birthday in pi:
    
    print("Your birthday appears in th first million digits of pi !")
    print(pi.index(birthday))
else:
    print("Your birthday does not appear in the first million digits of pi !")
