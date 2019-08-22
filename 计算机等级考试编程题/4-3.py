# 统计不同字符个数。用户从键盘键入一行字符，编写一个程序，统计并输出其中英文字符、数字、空格和其他字符的个数。
char = input('请输入一段字符：')
english, digital, empty, other = 0, 0, 0, 0
for i in char:
    if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        english += 1
    elif i in '1234567890':
        digital += 1
    elif i == ' ':
        empty += 1
    else:
        other += 1
print('英文字符：{}，数字：{}，空格：{}，其他：{}'.format(english, digital, empty, other))
