# 编写一个函数，参数为一个整数n。利用递归获取斐波那契数列中的第n个数并返回。
def Febonacci(n):
    if n <= 1:
        return n
    return Febonacci(n-1) + Febonacci(n-2)

def main():
    n = eval(input('请输入一个整数：'))
    print(Febonacci(n))

if __name__ == '__main__':
    main()
