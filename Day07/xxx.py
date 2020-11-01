names = [{'name': 'zhangsan', 'age': 18}, {'name': 'lisi', 'age': 20}]
while True:
    # 修改
    old_name = input('请输入要修改的姓名：')
    print(names)
    flag = 0
    for line in names:
        if line['name'] == old_name:
            new_name = input('请输入修改的姓名:')
            new_age = input('请输入修改的年龄:')
            line['name'] = new_name
            line['age'] = int(new_age)
            flag = True
            break
    if flag:
        print("已修改！")
    else:
        print('输入的用户不存在！')
    print(names)
