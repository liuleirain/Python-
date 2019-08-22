# 输入一个年份，输出是否为闰年。
# 闰年条件：能被4整除但不能被100整除，或者能被400整除的年份都是闰年。
year = eval(input('请输入年份：'))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('是闰年！')
else:
    print('不是闰年！')