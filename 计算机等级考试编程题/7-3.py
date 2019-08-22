# 编写一个程序， 生成一个10X10的随机矩阵并保存为文件（空格分隔行向量、换行分割列向量），在写程序
# 将刚才保存的矩阵文件另存为CSV格式，用EXCEL或文本编辑器打开看看结构对不对。
import random


def save_txt(low, high, file_txt):
    file = open('{}.txt'.format(file_txt), 'w', encoding='utf-8')
    for row in range(10):
        a = ''
        for col in range(10):
            b = str(random.randrange(start=low, stop=high))
            a = a + b + ' '
        file.write(a + '\n')
    file.close()
    print('{}.txt文件保存完成'.format(file_txt))


def save_csv(file_txt, file_csv):
    file_tmp = open('{}.txt'.format(file_txt), 'r', encoding='utf-8')
    file_new = open('{}.csv'.format(file_csv), 'w', encoding='utf-8')
    for line in file_tmp:
        line = line.replace(' ', ',')
        file_new.write(line)
    file_new.close()
    print('{}.csv文件保存完成。'.format(file_csv))


def main():
    low, high = eval(input('请输入随机数的最小值和最大值：<low, high>'))
    file_txt = input('请输入txt文件名：')
    save_txt(low, high, file_txt)
    file_csv = input('请输入csv文件名：')
    save_csv(file_txt, file_csv)


if __name__ == '__main__':
    main()
