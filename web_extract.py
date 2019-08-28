def get_html_lines(input_file):
    f = open(input_file, 'r', encoding='utf-8')
    ls = f.readlines()
    f.close()
    return ls

def extract_image_urls(html_lines):
    urls = list()
    for line in html_lines:
        if 'img' in line:
            url = line.split('src=')[-1].split('"')[1]
            if 'http' in url:
                urls.append(url)
    return urls

def show_result(urls):
    count = 0
    for url in urls:
        print('第{:2}个URL：{}'.format(count, url))
        count += 1

def save_result(output_file, image_urls):
    f = open(output_file, 'w')
    for url in image_urls:
        f.write(url + '\n')
    f.close()

def main():
    input_file = 'ngchina.html'
    output_file = 'ngchia_urls.txt'
    html_lines = get_html_lines(input_file)
    image_urls = extract_image_urls(html_lines)
    show_result(image_urls)
    save_result(output_file, image_urls)

if __name__ == '__main__':
    main()
