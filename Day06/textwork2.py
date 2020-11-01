#有关字典的相关练习

python_methods = {'.title():': '无需参数，直接使用的一种方法，可以将英文字母首字母大写以达到突出主体的目的。',
                  '.max():': '可以将数组完全求取最大值。',
                  '.values():':'可以将字典中的值输出。'}
for v, information in python_methods.items():
    print('方法名：' + v +
          '\n定义：' + information)
    pass
for v in python_methods.keys():
    print(v)
    pass
will_person = {'hua', 'ou', 'xixi', 'hahaha', 'ouou'}
favorite_languages = {'ou': 'C',
                      'hua': 'Python',
                      'xixi': 'C++',
                      'haha': 'C++'}
for person in will_person:
    if person in favorite_languages.keys():
        print('\nThanking for you participation!' + person)
        pass
    else:print('\nAlthough you have not take part in this,' + 'but i will invite you, ' + person)
    pass
#明天要学习的是嵌套  列表与字典的嵌套