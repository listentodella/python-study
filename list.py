#!/usr/bin/env python
# coding=utf-8

## list
## list 类似 C数组,准确来说更像是C++的vector
## 不能越界,而且有从尾部往前游标的方法


classmates = ["tom", "jerry", "bob"]
# 回忆一下 "," "%", 格式化输出的细节
print("%s, %s, %s,", classmates[0], classmates[1], classmates[2])
print("%s, %s, %s,"  %(classmates[0], classmates[1], classmates[2]))
# 从后往前,同样不可越界
print("%s, %s, %s,"  %(classmates[-1], classmates[-2], classmates[-3]))

# 计算长度 len(), 但是它只能计算出该list有几个元素(若其元素也是个list,
# 那么这个list被看作一个元素)
print("classmates list len =", len(classmates))

# 追加
print("before append, classmates = ", classmates)
classmates.append('Adam')
print("after append, classmates = ", classmates, "len =", len(classmates))

# 删除 pop()
# 默认删除 尾元素, pop(i) 删除指定索引的元素
print("before append, classmates = ", classmates)
classmates.pop() # 此外,这条语句执行完返回值为 尾元素
print("pop element =", classmates.pop()) # 因此这里是新的 尾元素
print("after append, classmates = ", classmates) # 确实是pop了两个
classmates.pop(0)
print("pop first element, classmates =", classmates)

# list 也允许 不同类型的元素
L1 = ["a", "b", 1, 2]
print("L1 =", L1)

L2 = ["a", "b", [123, 456, "c"]]
print("L2 =", L2, ", L2[2][1] =", L2[2][1])

L3 = [L1, L2,]
print("L3[0] =", L3[0], "L3[1] =", L3[1], "len1 =", len(L3[0]), "len2 =", len(L3[1]))


# 空 list
Lvoid = []
print("this is void list = ", Lvoid, "len =", len(Lvoid))

# 只有一个元素的 list
Lone = [1]
print("this is one list =", Lone, "len =", len(Lone))


















