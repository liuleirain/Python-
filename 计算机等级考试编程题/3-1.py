# 获得用户输入的一个整数，输出该整数百位及以上的数字

num = input('请输入一个整数：')
if len(num) > 2:
    print('这个整数百位以上是：{}'.format(num[:-2]))
else:
    print('请输入三位及以上的整数！')