# 重复元素判定。编写一个函数，接收列表作为参数，如果一个元素在列表中出现了不止一次，则返回True，但不要
# 改变原来列表的值。同时编写调用这个函数和输出测试结果的程序。
def repeat(ls):
    ls = eval(ls)
    counts = dict()
    for i in ls:
        counts[i] = counts.get(i, 0) + 1
        if counts[i] > 1:
            return True
    else:
        return False

def main():
    ls = input('请输入一个列表：')
    print(repeat(ls))
    print(ls)

if __name__ == '__main__':
    main()
