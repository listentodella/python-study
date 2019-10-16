#!/usr/bin/env python
# coding=utf-8

# tuple 与 list 相似,不过它一旦初始化后就不可更改

classmates = ("tom", "jerry", "bob")
print("classmates =", classmates)

# 正因为不可更改,因此没有 append pop等方法

# 只有一个元素的 tuple
T1 = (1)
print("T1 =", T1)
# 由于 () 本身是一个数学运算符,因此没有特别修饰的话,这种表达看作是一个普通变量
# 而不是一个 tuple!!! , 自然也不能提供 len() 方法
# print("T1 =", T1, "len =", len(T1))

T2 = (1,)
print("T2 =", T2, "len =", len(T2))

# 空 tuple
Tvoid = ()
print("this is void tuple =", Tvoid, "len =", len(Tvoid))

# 不可更改 其实只针对它指向的元素的类型, 比如 1, 2本身是常量,是read-only,就不可变
# 但是 list 本身是可变的,当然它作为 T3的一个元素,再怎么变也只是个 list
# 因此要初始化一个内容也不可变的tuple, 必须保证tuple的每一个元素是 read-only
T3 = (1, 2, ["tom", "jerry"],)
T4 = (1, 2, classmates)
print("T3 =", T3, "T4 =", T4)

T3[2][1] = "hello"
T3[2].append("world")
T3[2].pop(0)
# T4[2][1] = "world"
print("T3 =", T3, "T4 =", T4)











