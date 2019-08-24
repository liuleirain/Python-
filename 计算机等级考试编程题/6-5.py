# 重复元素判定续。利用集合的无重复性改编上一个程序，获得一个更简洁的版本。
def repeat(list):
    if len(list) != len(set(list)):
        return True
    else:
        return False

def main():
    list = input('请输入一个列表：')
    print(repeat(list))
    print(list)

if __name__ == '__main__':
    main()
