# 参考最后一个实例，尝试将不同标签中的内容分门别类地提取出来，在想想如何提取可以更为准确。
def get_html_lines(input_file):
    f = open(input_file, 'r', encoding='utf-8')
    ls = f.readlines()
    f.close()
    return ls

def extract_image_urls(html_lines):
    img_urls = list()
    href_urls = []
    for line in html_lines:
        if 'img' in line:
            url = line.split('src=')[-1].split('"')[1]
            if 'http' in url:
                img_urls.append(url)
        if '<a' in line:
            url = line.split('href=')[-1].split('"')[1]
            if 'http' in url:
                href_urls.append(url)
    return img_urls, href_urls

def show_result(urls, name):
    count =1 
    for url in urls:
        print('{}标签第{:2}个URL：{}'.format(name,count, url))
        count += 1

def save_result(output_file, image_urls):
    f = open(output_file, 'w')
    for url in image_urls:
        f.write(url + '\n')
    f.close()

def main():
    input_file = '../ngchina.html'
    output_file = '../ngchina_urls.txt'
    html_lines = get_html_lines(input_file)
    img_urls, a_urls = extract_image_urls(html_lines)
    show_result(img_urls, 'img')
    show_result(a_urls, 'a')
    urls = img_urls + a_urls
    save_result(output_file, urls)

if __name__ == '__main__':
    main()
