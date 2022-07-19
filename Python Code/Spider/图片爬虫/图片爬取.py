# 导入模块
import requests
import re

index = 1  # 设置索引值

for i in range(1, 100):  # 从1 到 30 表示爬取30页
    url = f'http://desk.tooopen.com/meinv_1_{i}.html'  # 设置地址

    headers = {  # 设置头部
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'Referer': 'http://imgfzone.tooopen.com/'
    }

    r = requests.get(url, headers=headers)  # 发送get请求
    # print(r.text)

    img_url = re.findall('img src="(.*?)"', r.text)  # 正则表达式寻找图片地址
    name = re.findall('<span>(.*?)</span>', r.text)  # 正则表达式寻找图片名称
    # print(img_url)
    # print(name)

    num = 0  # 设置名称列表索引值
    print('获取第%d页:' % i)

    for img in img_url:  # 遍历图片地址
        response = requests.get(img, headers=headers)  # 发送get请求

        with open(f'美女/{name[num]}.jpg', 'wb') as f:
            f.write(response.content)  # 写入文件

        print(f'正在获取第{index}张图片,图片名称:{name[num]},图片地址:{img}')

        num += 1
        index += 1  # 索引值每次加1

    print('第%d页获取结束\n' % i + '-' * 100)

print('获取结束')
