file_name = 'pi_number.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.replace(' ',''),end='')

