# 系统提示输入用户名字，并随机生成一个幸运数字，输出结果。
import random
strl = input("请输入你的名字：")
print("Hello!{}".format(strl))
print(strl[0])
guard = ord(strl[0]) % 100
print(ord(strl[0]))
print(guard)
print('你的幸运数是',random.choice(range(guard)))