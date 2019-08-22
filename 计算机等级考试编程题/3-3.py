# 程序读入一个表示星期几的数字（1-7），输出对应的星期字符串名称。例如：输入3，返回“星期三”
weeks = eval(input('请输入数字（1-7）：'))
if weeks == 1:
    print('星期一')
elif weeks == 2:
    print('星期二')
elif weeks == 3:
    print('星期三')
elif weeks == 4:
    print('星期四')
elif weeks == 5:
    print('星期五')
elif weeks == 6:
    print('星期六')
elif weeks == 7:
    print('星期日')
else:
    print('请输入（1-7）之间的数字。')