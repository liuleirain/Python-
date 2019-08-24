# 编写一个程序，要求能够将元素为任意Python支持的类型（包括含有半角逗号的字符串）
# 的列表转储为CSV，并能够重新正确解析为列表。
def save_csv(ls, fname):
    value = input('请向列表总添加一个元素：')
    while value != '':
        ls.append(value)
        value = input('请向列表总添加一个元素：')
    print('你输入的列表为：{}'.format(ls))

    for i in range(len(ls)):
        if ',' in ls[i]:
            ls[i] = ls[i].replace(',', '.')

    file_csv = open('{}.csv'.format(fname), 'w', encoding='utf-8')
    file_csv.write(','.join(ls) + '\n')
    file_csv.close()
    print('恭喜！已经成功保存<{}.csv>文件！'.format(fname))


def read_csv(lt, fname):
    f = open('{}.csv'.format(fname), 'r', encoding='utf-8')
    lt = f.read().strip('\n').split(',')

    for i in range(len(lt)):
        if '.' in lt[i]:
            lt[i] = lt[i].replace('.', ',')
    f.close()
    print('<{}.csv>文件读取中...'.format(fname))
    print(lt)

def main():
    ls = []
    fname = input('请将列表文件命名：')
    save_csv(ls, fname)
    lt = []
    read_csv(lt, fname)

if __name__ == '__main__':
    main()
