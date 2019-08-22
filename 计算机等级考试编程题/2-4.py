# 获得用户输入的一个小数，提取并输出其整数部分。
Decimal = input('请输入一个小数：')
print('{}'.format(Decimal.split('.')[0]))