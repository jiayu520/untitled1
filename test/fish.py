# -*- coding: utf-8 -*-
# import random
#
#
# class Fish:
#     def __init__(self):
#         self.x = random.randint(0,10)
#         self.y = random.randint(0,10)
#
#
#     def move(self):
#         self.x -= 1
#         print("我的位置是：",self.x,self.y)
#
#
# class Goldfish(Fish):
#     pass
# class Carp(Fish):
#     pass
# class Salmon(Fish):
#     pass
# class Shark(Fish):
#     def __init__(self):
#         self.hungry = True
#
#     def eat(self):
#         if self.hungry:
#             print("吃货的梦想就是天天有的吃")
#             self.hungry = False
#         else:
#             print("吃不下了")
#
# fish = Fish()
# fish.move()
# print(dir(fish))

class  Person():
    name ="noname"
    def get_name(self):
        return self.name#调用类的属性
print(Person.name)
p = Person()#实例化一个对象
print(p.name)
print(p.get_name())#t调用方法
p.name = "lili"#修改类属性，注意只是修改了这个实例的属性，类属性并没有被修改
print(p.name)
print(Person.name)

p.name ='xiaoming'
Person.name = 'lili'#修改类的属性，注意先修改了实例属性，在修改类属性，这时已经不能影响实例属性了

print(p.name)#结果还是xiaoming

Person.name = 'jia'
p.name = 'yu'
print(p.name)#这是结果为yu