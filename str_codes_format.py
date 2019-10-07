#!/usr/bin/env python
# coding=utf-8

# ord() to 得到一个Unicode码字符对应的整型值
print("the val of 'A' is", ord("A"))
print("the val of 'A' is", ord('A'))
print("the val of '中' is", ord('中'))
print("the val of '中' is", ord("中"))

# chr() to 得到一个整型值对应的Unicode码字符
print("the str of 66 is", chr(66))
print("the str of 25991 is", chr(25991))

# use \u
print("this is '\u4e2d\u6587'")

# use b to present bytes type,这样可以在传输、保存时使得每个字节只占用1个byte
x = b'ABC' # or b"ABC"
print("x =", x)

# encode() 将str编码为指定的bytes
print("'ABC' in ascii =", "ABC".encode("ascii"))
print("'中文' in utf-8 =", "中文".encode("utf-8"))

# decode() 则是将获取到的bytes以指定的编码格式转换为 str
# 如果 Bytes 中只有一小部分无效的字节,可以传入 errors='ignore' 忽略错误
print(" b'ABC' decode ascii =", b'ABC'.decode("ascii"))
print(" b'\\xe4\\xb8\\xad\\xe6\\x96\\x87' decode utf-8 =",
        b'\xe4\xb8\xad\xe6\x96\x87'.decode("utf-8", errors='ignore'))

# len() 计算 str 的字符数
# len() 也可以将其换算成 bytes, 即计算字节数
print(" in bytes, b'ABC' len =", len(b'ABC'))
print(" in bytes, '中文' len =", len("中文".encode("utf-8")))
print(" in bytes, b'\\xe4\\xb8\\xad\\xe6\\x96\\x87' len =", len(b'\xe4\xb8\xad\xe6\x96\x87'))

print(" 'ABC' len =", len("ABC"))

# 格式化输出
# 不能 有 ',' 号, 否则无法解释
# print(" Student1's name = %s, age = %d, weight = %f kg", %("Tom", 12, 50.3))
print(" Student1's name = %s, age = %d, weight = %f kg" %("Tom", 12, 50.3))
# 如果不确定是何种格式, %s 总是有效...它会把任何数据类型转换为字符串
print(" Student1's name = %s, age = %s, weight = %s kg" %("Tom", 12, 50.3))

# %% 表示一个 %
print(" rate = %d %%" %10)
print(" rate = %d %%" %(10))

# format(),用传入的参数依次替换字符串内的占位符{0}、{1}...不过这种比%要麻烦
print("Hello, {0}, rate {1} %".format("Tom", 25.123))
print("Hello, {0}, rate {1:.1f} %".format("Tom", 25.123))
print("Hello, {0}, rate {1:.2f} %".format("Tom", 25.123))

s1 = 72
s2 = 100
rate = (s2 - s1) / s1 * 100
print('rate = %.1f %%' %(rate))
print('rate = %.2f %%' %(rate))



