# 输入一个文件和一个字符，统计该字符在文件中出现的次数。
def countStr(fname, a_str, count):
    file = fname + '.txt'
    fo = open(file, 'r', encoding='utf-8')
    for line in fo:
        for i in line:
            if i == a_str:
                count += 1
    print('"{}"字符早《{}》中出现的次数是：{}次'.format(a_str, fname, count))


def main():
    fname = input('请输入文件名：')
    a_str = input('请输入字符：')
    count = 0
    countStr(fname, a_str, count)


if __name__ == '__main__':
    main()
