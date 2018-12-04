file = "d:/文档/个人/随手记/py/IO/file/Breaking the Wilderness.txt"
#Breaking the Wilderness.txt

try:
    with open(file,'r',encoding= 'utf-8') as file_object :
        contents = file_object.read()
except FileNotFoundError:
    print("file not found, please check the path")
else:
    words = contents.split()
    num_words = len(words)
    print("the file" + file + " has about " + str(num_words) + " words.")