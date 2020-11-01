#本python文件将完成所有有关列表的作业习题
# name_list = ['huang xing jie' , 'li si mao' , 'lao wu']
# print(name_list)#3-1✔
# print(name_list[0])
# print('Hello!' + '\nHow are you ?' +  ' ' +name_list[1])#3-2✔
#
# to_school_method = ['bus' , 'bike' , 'subway']
# print('I like attending school' + ' ' + 'by ' + to_school_method[0] + '!')#3-3✔

#晚宴邀请流程
initial_guest = ['lao zhang' , 'lao wang' , 'lao li' , 'lao huang']
print('I am inviting you' + ',' + initial_guest[0].title() + ',' + ' to come my dinner party!')
print('I am inviting you' + ',' + initial_guest[1].title() + ',' + ' to come my dinner party!')
print('I am inviting you' + ',' + initial_guest[2].title() + ',' + ' to come my dinner party!')
print('I am inviting you' + ',' + initial_guest[3].title() + ',' + ' to come my dinner party!')

print("\nBut lao zhang couldn't come here" + ' ' + 'So i invite lao mi to come with us!')
initial_guest.remove('lao zhang')
initial_guest.insert(0,'lao mi')
print('\nAll the invited guests are blow')
print('========================================')
for guest in initial_guest:
    print(guest.title())
print('========================================')
print('I am inviting you' + ',' + initial_guest[0].title() + ',' + ' to come my dinner party!')
print('I am inviting you' + ',' + initial_guest[1].title() + ',' + ' to come my dinner party!')
print('I am inviting you' + ',' + initial_guest[2].title() + ',' + ' to come my dinner party!')
print('I am inviting you' + ',' + initial_guest[3].title() + ',' + ' to come my dinner party!')

print()

print('Wait!' + 'I have just found a bigger dinning-table.' + "\ntThat's say we can invite more friends!")

initial_guest.insert(0,'冬泳怪鸽')
initial_guest.insert(2, '欧拉')
initial_guest.append('kuaizero')
print('I am inviting you' + ',' + initial_guest[0].title() + ',' + ' to come my dinner party!')
print('I am inviting you' + ',' + initial_guest[1].title() + ',' + ' to come my dinner party!')
print('I am inviting you' + ',' + initial_guest[2].title() + ',' + ' to come my dinner party!')
print('I am inviting you' + ',' + initial_guest[3].title() + ',' + ' to come my dinner party!')
print('I am inviting you' + ',' + initial_guest[4].title() + ',' + ' to come my dinner party!')
print('I am inviting you' + ',' + initial_guest[5].title() + ',' + ' to come my dinner party!')
print('I am inviting you' + ',' + initial_guest[6].title() + ',' + ' to come my dinner party!')
print(len(initial_guest))
print()
print()
print()
print('I am very sory to say that we may do not have enough tablewares')
print(initial_guest)
i = 0
while i < 6:
    print('I am sorry.' + '\nI will invite you next time.' + ' ' + initial_guest[0])
    initial_guest.pop(0)
    print()
    i += 1
    pass
#循环中每次对列进行操作时都会使得索引值发生变化  一定要注意
print(len(initial_guest))
final_guest = initial_guest
print('==========================================')
print('Guest list')
for guest in final_guest:
    print(guest)
    pass
print('==========================================')
print('I am waiting for your coming!')
#remove 是针对具体的量来运算的