# 导入模块
import requests
from lxml import etree
import datetime
import csv


# 创建微博热搜类
class WbHotSearch(object):

    # 初始化属性
    def __init__(self):
        self.url = 'https://s.weibo.com/top/summary'  # 网页地址
        # 请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Mobile Safari/537.36'
        }
        # 获取当前日期
        now_time = f'{datetime.datetime.now().year}年{datetime.datetime.now().month}月{datetime.datetime.now().day}日{datetime.datetime.now().hour}时'

        self.f = open(f'微博热搜\{now_time}微博热搜.csv', 'w',
                      newline='')  # 创建csv文件 newline=''去掉空行
        self.writer = csv.writer(self.f)  # csv写入到创建的csv文件中

    # 1.请求数据
    def get_response(self):
        response = requests.get(url=self.url, headers=self.headers)  # 请求数据
        if response.status_code == 200:  # 判断响应是否成功
            return response  # 成功则返回数据
        else:
            print('获取失败')

    # 2.解析提取数据
    def extract_response(self):
        response = self.get_response().content.decode(
            'gb2312')  # 接收get_response()方法返回的数据
        html = etree.HTML(response)  # 解析数据变为可使用xpath语法的格式
        # 提取数据
        resou_url = html.xpath(
            '//html/body/div/section/ul/li/a/@href')  # 热搜的链接
        resou = html.xpath(
            '//html/body/div/section/ul/li/a/span/text()')  # 热搜内容
        resou_pl = html.xpath(
            '//html/body/div/section/ul/li/a/span/em/text()')  # 热搜评论数量
        # 删除空数据
        while ' ' in resou:
            resou.remove(' ')
        # 创建一个字典 存获取到的数据
        data = {
            'title': resou,
            'pl': resou_pl,
            'url': resou_url
        }
        return data  # 返回字典

    # 3.保存写入数据
    def save(self, title, pl, url):
        self.writer.writerow([title, pl, url])  # 写入csv数据

    # 4.调用方法
    def main(self):
        self.get_response()
        data = self.extract_response()  # 接收extract_response()方法返回数据
        self.save('排行榜', '评论人数', '网址')  # 写第一行的表头
        index = 1
        del data['url'][0]  # 删除不需要的置顶内容
        for url in data['url']:  # 遍历字典中'url'中内容到url
            url = 'https://s.weibo.com/' + url  # 补上缺少的网址信息
            title = data['title'][index]
            try:
                pl = data['pl'][index - 1]
            except IndexError:
                pass
            print(f'正在保存--热搜第{index}:{title}|评论人数{pl}|网址:{url}')
            self.save(title, pl, url)
            index += 1
            if index == len(data['title']):  # 判断索引是否超出范围
                self.f.close()  # 关闭文件
                print('保存完成')
                break  # 结束循环


if __name__ == '__main__':
    wb = WbHotSearch()  # 实例化类
    # 调用main()
    wb.main()
