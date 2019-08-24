# 英文字符频率统计。编写一个程序，对给定字符串中出现的a～z字母的频率进行分析，忽略大小写，采用降序方式输出。
string = input('请输入英文字符串：')
str_count = dict()
for i in string:
    if i.isalpha():
        i.lower()
        str_count[i] = str_count.get(i, 0) + 1
result = list(str_count.items())
result.sort(key=lambda x:x[0], reverse=True)
for i in range(len(result)):
    letter, count = result[i]
    print('{:<5}{:>5}'.format(letter, count))
