#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: huaxichen
@Email: zc10360@126.com
@Time: 2020/6/6 16:22
@File: homework1
@Project: Hogwarts_huaxichen
"""

"""
作业一：
创建模块，模块里面创建方法，定义有参数，和无数，有返回值和无返回值 的情况，并说明 无返回值的默认返回值。
"""


# 1. 创建了模块homework1
# 2. 创建方法haveargs定义有多个参数，有返回值
def haveargs(*arg):
    result = []
    for i in arg:
        result.append(i)
    print(f"I have {len(result)} args as below : {result}")
    return result


# 3. 创建方法noarg定义无参数，无返回值，此时返回默认返回值None
def noarg():
    print("No return")


# 4. 创建方法havearg，定义有默认参数，且返回此参数
def havearg(arg="I am arg"):
    return arg


# 定义入口函数
def main():
    # 有返回值，传入参数
    print(havearg("have args and hane return"))
    # 有返回值，不传参数使用默认参数
    print(havearg())
    # 无返回值是默认返回值为None
    print(noarg())
    # 可变参数的使用
    haveargs("no1", "No2", "I am three", "Here is 4")


if __name__ == '__main__':
    main()
