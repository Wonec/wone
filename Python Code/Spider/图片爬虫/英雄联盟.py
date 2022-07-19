# 导入模块
import requests
import json
import concurrent.futures  # 线程池
import time

class Yxlm:

    def __init__(self):
        """初始化属性"""
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
        }

    def get_response(self, url):
        """发送请求返回数据的方法"""
        response = requests.get(url=url, headers=self.headers)
        if response.status_code == 200:
            return response
        else:
            print('获取失败')

    def save(self, name, url, img):
        """保存数据的方法"""
        with open(f'英雄联盟/{name}.jpg', 'wb') as f:
            f.write(img)

    def id(self):
        """提取出需要的id数据"""
        hero_list_url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
        response = self.get_response(hero_list_url)
        data = json.loads(response.text)
        id = []
        for h in data['hero']:
            id.append(h['heroId'])
        return id

    def run(self, url):
        """运行程序"""
        response = self.get_response(url)
        hero = json.loads(response.text)
        img_url = []
        hero_name = []
        index = 0
        for i in hero['skins']:
            img_url.append(i['mainImg'])
            hero_name.append(i['name'])
        hero = {
            'img_url': img_url,
            'hero_name': hero_name
        }
        for url in hero['img_url']:
            url_1 = hero['img_url'][index]
            if url_1 == '':
                index += 1
            else:
                img = self.get_response(url=url_1).content
                print(f"存储中--《{hero['hero_name'][index]}》\nURL:{url_1}")
                self.save(hero['hero_name'][index], url, img)
                index += 1


if __name__ == '__main__':
    '''实例化对象 调用方法'''
    yx = Yxlm()
    id = yx.id()
    time_1 = time.time()
    exe = concurrent.futures.ThreadPoolExecutor(max_workers=10)
    for page in id:
        url = f'https://game.gtimg.cn/images/lol/act/img/js/hero/{page}.js'
        exe.submit(yx.run, url)
    exe.shutdown()
    time_2 = time.time()
    use_time = int(time_2) - int(time_1)
    print(f'总计时:{use_time} S')
    print('=====存储结束=====')