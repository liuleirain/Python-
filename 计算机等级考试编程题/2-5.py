# 下面这段代码能够获得用户输入的一个整数N，计算并输出1到N相加的和。然而，这段代码存在多处语法错误，请指出错误所在并纠正。
n = eval(input('请输入整数N：'))
sum = 0
for i in range(n+1):
    sum += i
print('1到N求和结果：{}'.format(sum))