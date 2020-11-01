#If 如果语句
cars = ['audi', 'bmw', 'subaru', 'toyuya']
for car in cars:
    if car == 'bmw':
        print(car.upper())
        pass
    else:
        print(car.title())
        pass
if 'bmw' not in cars:# 有not in 这一说
    print('false')
    pass
else:
    print('true')