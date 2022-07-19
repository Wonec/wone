# 导入模块
import hashlib
import requests
import json


class fy_spider(object):
    """创建爬虫类"""

    def __init__(self, query_str):
        self.query_str = query_str
        # 初始翻译路径
        sign = (hashlib.md5(("6key_cibaifanyicjbysdlove1" + self.query_str).encode('utf-8')).hexdigest())[0:16]
        url = 'https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba'
        self.url = url + '&sign=' + sign
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
        }
        # 获取请求体数据
        self.data = self.get_data()

    def get_data(self):
        """获取请求体数据"""
        data = {
            'from': 'auto',
            'to': 'auto',
            'q': self.query_str
        }
        return data

    def get_data_fromurl(self):
        """从服务器获取数据 并且解析返回"""
        response = requests.post(self.url, headers=self.headers, data=self.data)
        if response.status_code == 200:
            return response.content.decode()
        else:
            print('请求失败')

    def paser_data(self, json_str):
        dict_data = json.loads(json_str)
        result = dict_data['content']['out']
        print('翻译后的结果是:{}'.format(result))

    def run(self):
        # 1. 获取url 请求头 请求体
        # 2. 发送请求获取响应数据
        json_str = self.get_data_fromurl()
        # 3. 提取数据
        self.paser_data(json_str)


# 调用程序
if __name__ == '__main__':
    while True:  # 循环调用
        query_str = input('请输入要翻译的内容(输入q退出):')
        if query_str == 'q':
            print('已退出')
            break
        spider = fy_spider(query_str)
        spider.run()
