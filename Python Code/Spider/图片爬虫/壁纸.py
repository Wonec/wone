import requests
from lxml import etree
import concurrent.futures  # 线程池
import time  # 时间

class BiZhi:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
        }

    def get_response(self, url):
        response = requests.get(url=url, headers=self.headers)
        if response.status_code == 200:
            return response
        else:
            print('获取失败')

    def save(self, name, html_url):
        img = self.get_response(url=html_url)
        with open(f'壁纸/{name}.jpg', 'wb') as f:
            f.write(img.content)

    def main(self, html_url):
        response = self.get_response(url=html_url).text
        html = etree.HTML(response)
        img_url = html.xpath('//div[@class="list"]/ul/li/a/@href')
        for i in img_url:
            i = f'http://www.netbian.com/{i}'
            r = self.get_response(url=i).content.decode('gbk')
            h = etree.HTML(r)
            img = h.xpath('//div[@class="endpage"]/div/p/a/img/@src')
            img = img[0]
            name = h.xpath('//div/div/p/a/img/@title')
            name = name[0]
            print(f'正在保存:{name}|网址:{img}')
            self.save(name, img)

if __name__ == '__main__':
    exe = concurrent.futures.ThreadPoolExecutor(max_workers=64)  # 创建引擎对象 线程为12个
    bz =BiZhi()
    print("分类['动漫','风景','美女','游戏','唯美','汽车','动物']")
    text = input('请输入需要的分类:')
    while True:
        if text == '动漫':
            fenlei = 'dongman'
            break
        elif text == '风景':
            fenlei = 'fengjing'
            break
        elif text == '美女':
            fenlei = 'meinv'
            break
        elif text == '游戏':
            fenlei = 'youxi'
            break
        elif text == '唯美':
            fenlei = 'weimei'
            break
        elif text == '汽车':
            fenlei = 'qiche'
            break
        elif text == '动物':
            fenlei = 'dongwu'
            break
        else:
            text = input('输入错误请重新输入:')
    time_1 = time.time()
    for page in range(2, 132):  # 遍历网址
        url = f'http://www.netbian.com/{fenlei}/index_{page}.htm'
        exe.submit(bz.main, url)  # 调用引擎
    exe.shutdown()
    time_2 = time.time()
    use_time = int(time_2) - int(time_1)
    print('获取结束')
    print('总计耗时：', use_time, 's')
