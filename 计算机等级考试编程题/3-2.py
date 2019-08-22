# 获得用户输入的一个字符串，将字符串按照空格分隔，然后逐行打印出来。
str = input('请输入一个带空格的字符串：')
ls = str.split()
for i in range(len(ls)):
    print(ls[i])