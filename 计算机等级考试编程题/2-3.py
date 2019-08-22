# 获得用户输入的一个合法算式，例如：1.2+3.4，输出运算结果。
Formula = input('请输入一个算式：')
print('{}算式的运算结果是{}'.format(Formula, eval(Formula)))