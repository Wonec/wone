import requests
from lxml import etree

class ZongHeng:
    def __init__(self):
        self.url = 'http://book.zongheng.com/showchapter/672340.html'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
        }

    def get_response(self, url):
        response = requests.get(url=url, headers=self.headers)
        if response.status_code == 200:
            return response.content.decode()
        else:
            print('获取失败')

    def save(self,url):
        response = self.get_response(url)
        html = etree.HTML(response)
        text = html.xpath('//div/p/text()')
        title = html.xpath('//div/div[@class="title_txtbox"]/text()')
        for t in title:
            print(f'正在保存{t}')
            with open(f'{t}.txt', 'w') as f:
                for i in text:
                    i = '\t' + i + '\n'
                    f.write(i)

    def main(self):
        # // div[2] / ul / li / a / @ href 网址xpath
        response = self.get_response(self.url)
        html = etree.HTML(response)
        xs_url = html.xpath('//div[2]/ul/li/a/@href')
        for url in xs_url:
            self.save(url)

if __name__ == '__main__':
    zh = ZongHeng()
    zh.main()

