# 利用random库生成一个包含10个0~100之间随机整数的列表。
import random


ls = []
for i in range(10):
    ls.append(random.randint(0,101))
print(ls)
