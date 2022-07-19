import re
import requests  # 导入模块

# 设置小说主地址
url = 'https://www.jianlaixiaoshuo.net/'

# 设置头部访问权限
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}

# 获取网页内容
response = requests.get(url=url, headers=headers)
# print(response.text)

# 正则表达式获取想要的内容
titles = re.findall('title="(.*?) 字数', response.text)
xs_url = re.findall('<a href="(.*?)" title=', response.text)

num = 0
# 设置循环爬取内容
for x in xs_url:
    t = titles[num]
    num += 1

    # 设置头部
    headers_1 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    # 获取网页内容
    response1 = requests.get(url=x, headers=headers_1)
    # print(response1.text)

    # 正则表达式获取想要的内容
    txt = re.findall('<p>(.*?)</p>', response1.text)
    print('获取内容:', t)
    print('获取网址', x)
    for item in txt:
        # 保存文件
        with open(t + '.txt', 'a+') as f:
            i = '\t' + item + '\n' + '\n'
            f.write(i)
    print('获取成功\n')
