import numpy as np


def save_txt(low, high, file_txt):
    a = np.random.randint(low, high, (10, 10))
    np.savetxt('{}.txt'.format(file_txt), a, fmt='%d')
    print('已经保存{}.txt文件成功！'.format(file_txt))


def save_csv(file_txt, file_csv):
    b = np.loadtxt('{}.txt'.format(file_txt))
    np.savetxt('{}.csv'.format(file_csv), b, fmt='%d', delimiter=',')
    print('已经保存{}.csv文件成功！'.format(file_csv))


def main():
    low, high = eval(input('请输入数字最小值最大值：<low, high>'))
    file_txt = input('请输入txt文件名：')
    save_txt(low, high, file_txt)
    file_csv = input('请输入csv文件名：')
    save_csv(file_txt, file_csv)


if __name__ == '__main__':
    main()
