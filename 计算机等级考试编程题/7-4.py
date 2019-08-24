# 编写一个程序，读取一个python源代码文件，将文件中所有除保留字外的小写字母换成大写字母，
# 生成后的文件要能够被Python解释权正确执行。
import keyword


kw = keyword.kwlist
kw.append('print')
kw.append('range')
kw.sort(key=lambda i:len(i), reverse=True)
print(kw)

def upper_word(fname_tem, num, keep):
    file_tem = open('{}.py'.format(format(fname_tem)), 'r', encoding='utf-8')
    file_new = open('{}_changed.py'.format(format(fname_tem)), 'w', encoding='utf-8')

    for line in file_tem:
        for word in kw:
            if word in line:
                num += 1
                keep['编号%s'%str(num)] = word
                line = line.replace(word, '编号%s'%str(num))
            else:
                continue
        line = line.upper()
        for key in keep.keys():
            if key in line:
                line = line.replace(key, keep[key])
        file_new.write(line)
    file_tem.close()
    file_new.close()

def main():
    num = 100
    keep = {}
    fname_tem = input('请输入Python源代码文件名：')
    upper_word(fname_tem, num, keep)

if __name__ == '__main__':
    main()
