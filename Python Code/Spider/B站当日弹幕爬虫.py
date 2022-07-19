import re
import datetime
import requests
import wordcloud

# 获取当日日期 到天数
day_time = datetime.datetime.now()
date = str(day_time)[0:10]

# 获取oid
id = input('请输入视频oid:')
# 拼接url
url = f'https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid={id}&date={date}'
print(url)
headers = {
    "cookie": "_uuid=7AD40315-1C04-7B2F-1ACA-3ED670886F1B12162infoc; buvid3=CC43CCD4-951B-4B63-BADB-978A4AC1A09618535infoc; buvid_fp=CC43CCD4-951B-4B63-BADB-978A4AC1A09618535infoc; SESSDATA=4ce49562%2C1630080824%2Ca096f%2A31; bili_jct=6a51621163644278f80113c434d62c7f; DedeUserID=284677141; DedeUserID__ckMd5=e5258068f64a9a44; sid=jdu11pgz; rpdid=|(k|kmu)Rl)m0J'uYuRlk))Ju; CURRENT_FNVAL=80; blackside_state=1; fingerprint3=1fef990800b09c2e3d0d625f339772ac; fingerprint=930a00b9f69c998a2cfd461935dc6f85; fingerprint_s=4b8d519ec7954d68de61bbf26e16d0fa; buvid_fp_plain=CC43CCD4-951B-4B63-BADB-978A4AC1A09618535infoc; CURRENT_QUALITY=112; bsource=search_baidu; bfe_id=6f285c892d9d3c1f8f020adad8bed553; PVID=1",
    "origin": 'https://www.bilibili.com',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url=url, headers=headers)  # 发送请求获取弹幕数据

data = re.findall('.*?([\u4e00-\u9fa5]+).*', response.text)  # 正则获取中文内容

# 存放弹幕内容的列表
danmo_list = []
# 遍历正则到的数据存放到列表
for _ in data:
    # print(_)
    danmo_list.append(_ + '\n')

# 把列表中数据转换为字符串
danmo = "".join(danmo_list)

# 创建文件写入字符串内容 覆盖写入
with open('danmo.txt', 'w', encoding='utf-8') as f:
    f.write(danmo)

# 词云图属性 字体 背景色 宽高
w = wordcloud.WordCloud(font_path="msyh.ttc", background_color='white', width=1200, height=600)
# 读取创建的文件内容
f = open('danmo.txt', encoding='utf-8')
text = f.read()
# 生成词云图 内容为读取内容
w.generate(text)
# 输入到当前目录
w.to_file('danmo.png')
