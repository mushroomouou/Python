# 切片使用
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[: 5])
print(players[0:])
#未注明初始值或者末端值时打印到最后
#同时忽略前后索引值则会造成复制列表的功能
print(players[0: 3])
# 使用规范   列表[初始索引值: 终止索引值]

for player in players[1: 4]:
    print(player.title() + ' ', end='')
print()
print(players[0: 2])
#反向索引值-1为最后一个
print('=========================================')

favorite_foods = ['apple', 'pear', 'pineapple', 'watermelon']
friend_foods = favorite_foods[:]
#注意赋值给予地址址  而非变换成两个列表  所以复制不能使用  =   去赋值
favorite_foods.append('strawberry')
friend_foods.append('peach')
print('my favorite foods are:')
print(favorite_foods)
print("my friend's favorite foods are:")
print(friend_foods)