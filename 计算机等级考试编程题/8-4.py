# 参考第6张最后一个例子，按照8.2接中的方法重新实现一个有较好的函数封装的《Hamlet》文本词频
# 统计程序。
def get_text():
    text = open('hamlet.txt', 'r').read()
    text = text.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        text = text.replace(ch, ' ')
    return text

def word_count(text):
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

def convent_list(counts):
    items = list(counts.items())
    items.sort(key=lambda x:x[1], reverse=True)
    return items

def show_result(items, n):
    for i in range(n):
        word, count = items[i]
        print('{:10}{:5}'.format(word, count))

def main():
    n = eval(input('请输入显示多少出现最多的词：'))
    text =  get_text()
    counts = word_count(text)
    items = convent_list(counts)
    show_result(items, n)
    
if __name__ == '__main__':
    main()
