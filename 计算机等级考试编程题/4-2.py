# 最大公约数计算。获得两个整数，求出这两个整数的最大公约数和最小公倍数。最大公约数的计算一般使用辗转相除法，最小公倍数则
# 使用两个数的乘积除以最大公约数。
def gcd(num1, num2):
    while num1 != 0:
        num1, num2 = num2 % num1, num1
    return num2

int1 = eval(input('请输入第一个整数：'))
int2 = eval(input('请输入第二个整数：'))
print('最大公约数为：{}，最小公倍数为：{}'.format(gcd(int1,int2), int1 * int2 / gcd(int1, int2)))