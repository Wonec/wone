import requests
from lxml import etree
import os


class Biquge:

    def __init__(self):
        novel = input('请输入小说名称:')
        self.url = 'https://www.xbiquge.la/modules/article/waps.php'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
        self.data = {'searchkey': novel}

    # 发送post请求方法
    def requests_post(self):
        response = requests.post(url=self.url, data=self.data, headers=self.headers).text.encode('latin1').decode(
            'utf-8')
        return response

    # 发送get请求方法
    def requests_get(self, url):
        response = requests.get(url, headers=self.headers).text.encode('latin1').decode('utf-8')
        return response

    # html解析网页方法
    def html_parse(self, text):
        html = etree.HTML(text)
        return html

    # 当前目录创建文件夹
    def create_mkdir(self, name):
        file = os.getcwd()
        folder = f'{file}\\{name}'
        try:
            os.mkdir(folder)
        except FileExistsError:
            pass
        return folder

    def run(self):
        # 发送post请求 查找需要的书籍
        response = self.requests_post()

        html = self.html_parse(response)

        # xpath获取名称 作者 链接
        name = html.xpath('//tr/td[1]/a/text()')
        author = html.xpath('//tr/td[3]/text()')
        link = html.xpath('//tr/td[1]/a/@href')

        # 列出查找到的书
        index = 0
        for n in name:
            print(f'{index + 1}.  书籍名称:《{n}》  作者：{author[index]}')  # 书籍名称 作者
            index += 1

        # 选择书籍
        num = int(input('请选择书籍(输入数字):'))
        new_url = link[num - 1]
        book = name[num - 1]
        print(f'选择书籍为：《{book}》  链接地址：{new_url}')  # 选择书籍 地址

        print('开始获取......')

        # 创建文件夹
        folder = self.create_mkdir(book)
        print(f'保存地址为: {folder}')

        # get请求选择的书籍
        response_1 = self.requests_get(new_url)

        new_html = self.html_parse(response_1)

        # xpath获取 章节名称 章节url
        chapter = new_html.xpath("//div[@id='list']/dl/dd/a/text()")
        chapter_url_list = new_html.xpath("//div[@id='list']/dl/dd/a/@href")

        new_index = 0

        # 遍历章节url
        for chapter_url in chapter_url_list:
            print(f'《{chapter[new_index]}》')  # 章节名称
            # 拼接章节url的缺失
            chapter_url = 'https://www.xbiquge.la/' + chapter_url
            # get请求每一章
            response_2 = self.requests_get(chapter_url)
            chapter_html = self.html_parse(response_2)
            # xpath获取 正文内容
            item = chapter_html.xpath('//div[@id="content"]/text()')

            # 写入文件
            with open(f'{folder}\\{chapter[new_index]}.txt', 'w+', encoding='utf-8') as f:
                # 遍历正文内容
                for text in item:
                    # 写入内容
                    f.write(text)

            new_index += 1  # 索引每次+1

        print('获取完毕')


if __name__ == '__main__':
    # 实例化对象 调用方法
    bqg = Biquge()
    bqg.run()
