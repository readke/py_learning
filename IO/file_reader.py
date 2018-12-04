path = 'd:/文档/个人/随手记/py/IO/pi_digits.txt'

with open(path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())