import tkinter as tk
import re
import requests
import wordcloud
from tkinter import messagebox  # 导入模块

# 定义函数get
def Get():
    # 给变量bili赋值网址
    bili = 'https://www.bilibili.com/'
    # 把访客数据赋值给变量headers获取访问权限
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
    # 组合变量
    Bv = bili + url.get()  # get方法获取url的值
    # 获取网页内容,赋值给变量nr
    nr = requests.get(Bv, headers)

    js_str = nr.content.decode()

    name = re.findall('<span class="tit tr-fix">(.*?)</span>', nr.text)
    name1 = re.findall('<span class="tit">(.*?)</span>',nr.text)

    data = re.findall(r'"cid":[\d]*', js_str)

    data = data[0].replace('"cid":', "").replace(" ", "")

    url1 = "https://comment.bilibili.com/{}.xml".format(data)

    response1 = requests.get(url1, headers).content.decode()

    Danmu = re.findall('<d.*?>(.*?)</d>', response1)

    Danmu_str = " ".join(Danmu)

    w = wordcloud.WordCloud(font_path="msyh.ttc", background_color='white', width=1200, height=600)

    w.generate(Danmu_str)
    for n in name:
        if n:
            a = w.to_file(f'{n}.png')
            if a:
                messagebox._show(message='生成成功')
    for n1 in name1:
        if n1:
            a = w.to_file(f'{n1}.png')
            if a:
                messagebox._show(message='生成成功')



def Generated():
    if len(url.get()) == 0:
        a = messagebox.askyesno(title='是否继续生成', message='输入框内容为空,是否继续生成?')
        if a == False:
            pass
        else:
            Get()
    else:
        Get()


def Clean():
    if len(url.get()) == 0:
        messagebox.showinfo(message='输入框已为空')
    else:
        url.set('')


window = tk.Tk()
window.geometry('400x100')
window.title('wone')
window.iconbitmap('wone.ico')

label = tk.Label(window, text='输入B站BV网址:').pack()

url = tk.StringVar()
entry = tk.Entry(window, textvariable=url).pack()

button = tk.Button(window, text='生成', command=Generated).place(x=130, y=50)
button2 = tk.Button(window, text='清空', command=Clean).place(x=230, y=50)

window.mainloop()
