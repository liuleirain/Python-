# 假设有一个英文文本文件，编写一个程序读取器内容并将里面的大写字母变成小写字母，小写字母变成大写字母。
def swithTxt(fname):
    file = fname + '.txt'
    tmp_file = open(file, 'r', encoding='utf-8')
    new_file = open('{}转换后.txt'.format(fname), 'w', encoding='utf-8')
    for line in tmp_file:
        for i in line:
            if i in 'abcdefghijklmnopqrstuvwxyz':
                i = i.upper()
            elif i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                i = i.lower()
            new_file.write(i)
    tmp_file.close()
    new_file.close()


def main():
    fname = input('请输入文件名：')
    swithTxt(fname)


if __name__ == '__main__':
    main()
