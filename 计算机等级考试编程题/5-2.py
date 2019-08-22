# 实现isPrime()函数，参数为整数，要有异常处理。如果整数是质数，返回True，否则返回False。
def isPrime(int):
    if int == 1:
        return True
    for i in range(2, int):
        if int % i == 0:
            return False
            break
    else:
        return True

def main():
    while True:
        try:
            int = eval(input('请输入一个整数：'))
            if isPrime(int) == True:
                print('是质数！')
            else:
                print('不是质数！')
            break
        except:
            print('你输入的不是整数！')
            print('-'*20)

if __name__ == '__main__':
    main()
