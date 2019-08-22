# 实现isNum()函数，参数为一个字符串，如果这个字符串属于整数、浮点数或复数的表示，则返回True，否则返回False。
def isNum(str):
    try:
        if type(eval(str)) is int or\
            type(eval(str)) is float or\
            type(eval(str)) is complex:
            return True
    except:
        return False

def main():
    str = input('请输入字符串：')
    if isNum(str) == True:
        print('True')
    else:
        print('False')

if __name__ == '__main__':
    main()
