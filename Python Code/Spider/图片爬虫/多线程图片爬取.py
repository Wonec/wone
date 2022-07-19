# 导入模块
import requests  # 请求
import re  # 正则表达式
import concurrent.futures  # 线程池
import time  # 时间


# 请求方法
def get_response(html_url):
    """发送请求"""
    headers = {  # 请求体
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'Referer': 'http://imgfzone.tooopen.com/'
    }
    response = requests.get(url=html_url, headers=headers, timeout=0.1)  # 发送请求
    return response  # 返回数据


def save(name, img_url):
    """保存数据"""
    img = get_response(img_url)  # 发送请求存储数据
    with open(f'美女/{name}.jpg', 'wb') as f:
        f.write(img.content)  # 以二进制写入文件
    print(f'正在保存:{name} | 网址:{img_url}')


def main(html_url):
    """
    主引擎 用来调用方法
    """
    response = get_response(html_url)  # 请求网址
    img_url = re.findall('img src="(.*?)"', response.text)  # 正则表达式寻找图片地址
    name = re.findall('<span>(.*?)</span>', response.text)  # 正则表达式寻找图片名称
    index = 0
    for img_index_url in img_url:  # 遍历数据
        img_name = name[index]
        index += 1
        save(img_name, img_index_url)  # 存储数据


if __name__ == '__main__':
    """调用引擎"""
    time_1 = time.time()
    exe = concurrent.futures.ThreadPoolExecutor(
        max_workers=12)  # 创建引擎对象 线程为12个
    for page in range(1, 76):  # 遍历网址
        url = f'http://desk.tooopen.com/meinv_3_{page}.html'
        exe.submit(main, url)  # 调用引擎

    time_2 = time.time()
    use_time = int(time_2) - int(time_1)
    print('获取结束')
    print('总计耗时：', use_time, 's')
    # 10个线程总计时18秒
    # 12个线程总计时13秒
    # 16个线程总计时21秒
    # 32个线程总计时9秒
    # 64个线程总计时7秒
