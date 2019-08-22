# 编写一个函数计算传入字符串中的数字、字母、空格以及其他字符的个数。
def str_counts(string):
    letter, digital, empty, other = 0,0,0,0
    for i in string:
        if i.isalpha():
            letter += 1
        elif i.isdigit():
            digital += 1
        elif i == ' ':
            empty += 1
        else:
            other += 1
    return letter, digital, empty, other

def main():
    string = input('请输入字符串：')
    letter, digital, empty, other = str_counts(string)
    print('字母：{}，数字：{}，空格：{}，其他字符：{}'.format(letter, digital, empty, other))

if __name__ == '__main__':
    main()
