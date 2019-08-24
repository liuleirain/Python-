# 随机密码生成。编写程序在26个字母大小写和9个数字组成的列表中随机生成10个8位数密码。
import random
string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
s_list = list(string)
for i in range(10):
    a = ''
    for i in range(8):
        a += random.choice(s_list)
    print(a)
