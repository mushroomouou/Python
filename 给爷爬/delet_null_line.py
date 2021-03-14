name:str = input("请输入你的要修改的文件名：")
with open('new_{}'.format(name),'w') as new:
    with open(name) as f:
        for line in f.readlines():
            if len(line.strip()) == 0:
                continue
            new.write(line)
print("Yes")




