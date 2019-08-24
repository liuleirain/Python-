# 中文字符频率统计。编写一个程序，对给定字符串中出现的全部（含中文字符）频率进行分析，采用降序方式输出。
def is_chinese(word):
    if '\u4e00' <= i <= '\u9fa5':
        return True
    else:
        return False

word = input('请输入字符串：')
word_counts = dict()
for i in word:
    if is_chinese(i) == True:
        word_counts[i] = word_counts.get(i, 0) + 1
result = list(word_counts.items())
result.sort(key=lambda x:x[0], reverse=True)
for i in range(len(result)):
    word, count = result[i]
    print('{:>5}{:>5}'.format(word, count))
