# 编写一个函数，打印200以内的所有素数，以空格分割。
def isPrime(n):
    if n == 1:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
            break
    else:
        return True

def main():
    for i in range(1, 200):
        if isPrime(i) == True:
            print(i, end=' ')

if __name__ == '__main__':
    main()
