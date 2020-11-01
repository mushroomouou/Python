# sandwich_orders = ['培根披萨', '素披萨', '水果披萨']
# finished_sandwich = []
# for sandwhich in sandwich_orders:
#     print('你的' + sandwhich + '好了！' + '\n请及时取餐。')
#     print()
#     finished_sandwich.append(sandwhich)
# i = 0
# while i < len(finished_sandwich):
#     if i == 0:
#         print('当前完成餐点：' + '\n\t' + finished_sandwich[i])
#         pass
#     else:
#         print('\t' + finished_sandwich[i])
#         pass
#     i += 1

import random

print('这是一张有关你最爱旅游城市的调查问卷。')
interviewee = {}
flag = True
while True:
    name = input('请问你叫什么？\n')
    answer = input('请描述下你最爱的城市\n')
    interviewee.setdefault(name,answer)
    ending = input('是否结束？（是\否）\n')
    if ending == '是':
        break
        pass
    pass
print(interviewee)
A = random.sample(interviewee.keys(), 1)     # random.simple( , )是针对随机列表的选择方法  返回值是  列表  ！！！！！！！！！
ranperson = A[0]
rananswer = interviewee[ranperson]
print(ranperson + '最爱去的城市是' + rananswer + '!!')





