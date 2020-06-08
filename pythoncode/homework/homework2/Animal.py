#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: huaxichen
@Email: zc10360@126.com
@Time: 2020/6/8 23:37
@File: Animal
@Project: Hogwarts_huaxichen
"""
import yaml

"""
创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）

创建子类【猫】，继承【动物类】，
- 复写父类的__init__方法，继承父类的属性，
- 添加一个新的属性，毛发=短毛，
- 添加一个新的方法， 会捉老鼠，
- 复写父类的‘【会叫】的方法，改成【喵喵叫】

创建子类【狗】，继承【动物类】，
- 复写父类的__init__方法，继承父类的属性，
- 添加一个新的属性，毛发=长毛，
- 添加一个新的方法， 会看家，
- 复写父类的【会叫】的方法，改成【汪汪叫】

创建一个猫猫实例
- 调用捉老鼠的方法
- 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。

创建一个狗狗实例
- 调用【会看家】的方法
- 打印【狗狗的姓名，颜色，年龄，性别，毛发】。
4、使用 yaml 来管理实例的属性
5、提交代码到自己的github仓库， 贴到作业贴上
"""


# 创建一个类（Animal）【动物类】，
class Animal:
    # 类里有属性（名称，颜色，年龄，性别）
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    # 类方法（会叫）
    def howl(self):
        print(f"{self.name} can howl.")

    # 类方法（会跑）
    def run(self):
        print(f"{self.name} can run.")


# 创建子类【猫】，继承【动物类】
class Cat(Animal):
    # 复写父类的__init__方法，继承父类的属性,添加一个新的属性，毛发=短毛
    def __init__(self, name, color, age, gender, hair="short hair"):
        super().__init__(name, color, age, gender)
        self.hair = hair

    # 添加一个新的方法， 会捉老鼠
    def catch_mice(self):
        print(f"{self.name} can catch mice.")

    # 复写父类的‘【会叫】的方法，改成【喵喵叫】
    def howl(self):
        print(f"{self.name} can meow.")


# 创建子类【狗】，继承【动物类】
class Dog(Animal):
    # 复写父类的__init__方法，继承父类的属性,添加一个新的属性，毛发=长毛
    def __init__(self, name, color, age, gender, hair="long hair"):
        super().__init__(name, color, age, gender)
        self.hair = hair

    # 添加一个新的方法， 会看家
    def watch_house(self):
        print(f"{self.name} can watch house.")

    # 复写父类的【会叫】的方法，改成【汪汪叫】
    def howl(self):
        print(f"{self.name} can woof.")


# 创建一个猫猫实例
yingduan = Cat("miaomiao", "gray", "2", "female")
yingduan.catch_mice()
print(f"The cat is called {yingduan.name}, it is {yingduan.color}, {yingduan.age} years old, \n"
      f"has {yingduan.hair}, and it caught a mouse.\n")

# 创建一个狗狗实例
jinmao = Dog("JiaWang", "Gloden", "2", "male")
jinmao.watch_house()
print(f"The dog is called {jinmao.name}, it is {jinmao.color}, {jinmao.age} years old,\n"
      f"and it is {jinmao.gender} with {jinmao.hair}.\n")

# 使用 yaml 来管理实例的属性
with open("animal.yaml") as f:
    animals = yaml.safe_load(f)
jumao = animals["Cat"]
print(f"The cat is called {jumao['name']}, it is {jumao['color']}, {jumao['age']} years old, \n"
      f"has {jumao['hair']}, and it caught a mouse.\n")
samoye = animals["Dog"]
print(f"The dog is called {samoye['name']}, it is {samoye['color']}, {samoye['age']} years old,\n"
      f"and it is {samoye['gender']} with {samoye['hair']}.\n")
