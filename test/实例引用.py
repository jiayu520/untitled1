# -*- coding: utf-8 -*-
class Person:
    def __init__(self,name,age,gender):
        #构造方法，这些属性是公有的
        self.name = name
        self.age = age
        self.gender = gender

    def set_att(self,value):
        #私有属性
        self.value = value

    def eat(self):
        print(f" name:{self.name},age:{self.age},gender:{self.gender} 我在吃")
        #格式化输出
    def drink(self):
        print(f" name:{self.name},age:{self.age},gender:{self.gender} 我在喝")

    def run(self):
        print("name:%s ,age:%d,gender:%s" % (self.name,self.age,self.gender))
        #格式化输出
xiaoming = Person("xiaoming",10,"male")
xiaohong = Person("xiaohong",15,"female")
print(xiaoming.name)
xiaoming.run()

xiaoming.set_att("fit")
print(xiaoming.value)