#set() 函数是python内置函数的其中一个，属于比较基础的函数。创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
#set()  括号内赋上列表  集合  以获得不重复的集合


#嵌套
#没啥好说的  就是一点要注意  当字典里面嵌套字典是  要注意  使用for循环时  第一个变量有关字典名  第二个变量则为该字典的代替


country = {'japen': {'measure': 300,
                     'location': 'ocean'},
            'china': {'measure': 960,
                      'location': 'land'}}
for c, rep in country.items():
    print('\n国家名:' + c)
    print('地址:' + rep['location'])
    print('国土面积:' + str(rep['measure']))
