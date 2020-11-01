# 现在我将进行有关于随机漫步的算法实现
# 要点 :

# 首先，我们得制造一个有关于随机漫步的类
# 1，对于随机的实现我们考虑以下着几个方面  ； 方向的随机？？  距离的随机  ？？  变量的随机   原地踏步？？？
# 2. 创建类之后如何使用，类输出的是什么
# 3. 初始值是什么

from random import choice


class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_dir = choice([-1, 1])
            x_dis = choice([1, 2, 3, 4, 5])
            x_step = x_dir * x_dis

            y_dir = choice([-1, 1])
            y_dis = choice([1, 2, 3, 4, 5])
            y_step = y_dir * y_dis

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)
