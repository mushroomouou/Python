landscape = ['Yellow Stone' , 'Tian Jin' , 'Asian']
print(landscape)
landscape.sort(reverse = False)#reverse = true 可以把排序倒置  正向排列变反向排列
print(landscape)
#上述操作是永久性改变的
#一旦使用就无法复原
#下面的一种方法是暂时排序 相当于可以看看效果的那种
cars = ['bmw' , 'audi' , 'toyota' , 'subaru']
print(cars)
print(sorted(cars))
print(sorted(cars,reverse=True))#同样可以使用reverse = True 来进行反向
print(cars)

cars.reverse()#与sort一样都是永久生效
print(cars)

#列表长度
print(len(cars))

