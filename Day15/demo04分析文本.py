file_name = 'User.txt'

with open(file_name,'r') as file_object:
    file = file_object.read()
    list = file.split()
    print('共有' + str(len(list)) + '个单词！')