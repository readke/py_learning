path = 'd:/文档/个人/随手记/py/IO/pi_digits.txt'

with open(path) as file_object:
    for line in file_object:
        print(line.rstrip())