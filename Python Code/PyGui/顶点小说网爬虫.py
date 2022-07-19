# 导入模块
import requests
import re
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox
import webbrowser


# 定义函数爬取内容
def get():
    print('\n开始获取:')
    # 设置访客信息获取访问权限
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
    # 网址组合
    url = 'https://www.dingdiann.net/ddk' + var.get() + '/' + var1.get() + '.html'
    # 判断用户是否输入内容
    if var.get():
        print('小说编号:', var.get())
        if var1.get():
            print('章节编号:', var1.get())
            if var2.get():
                print('文件名称:', var2.get())
                # 测试代码
                try:  # 正常状态下执行下面代码
                    print('-----获取中-----')
                    # 获取网页内容
                    r = requests.get(url, headers=headers)
                    # 对获取内容以text形式进行解码转换为字符串模式赋值给变量html
                    html = str(BeautifulSoup(r.text, 'html.parser'))
                    # 正则表达式寻找需要的内容赋值给msg
                    msg = re.findall(f'\u3000\u3000(.*?)<script>', html, re.S)
                    for item in msg:  # 遍历msg中内容赋值给item
                        # 将item中的<br/>转换为换行符\n
                        item = item.replace('<br/>', '\n')
                    if item:  # 如果item中有内容执行下面代码
                        for i in range(200):
                            print(item[i], end='')
                        print('\n......')
                        print('获取成功\n')
                        # 以写入的模式打开指定路径的文件(没有文件的情况下在指定目录创建文件)赋值给f，var2.get()为用户输入内容
                        f = open('C:/Users/wone/Desktop/' +
                                 var2.get() + '.txt', 'w')
                        # 写入item到f
                        f.write(item)
                        # 弹出消息窗口title窗口名称message窗口提示内容
                        messagebox._show(title='获取', message='获取成功')
                except UnboundLocalError:  # 出现错误执行下面代码
                    print('获取失败,网站输入错误\n')
                    # 弹出消息窗口
                    messagebox.showerror(
                        title='错误', message='获取失败,找不到此网址,请检查输入内容')

            # 用户没输入内容执行下面代码
            else:
                print('缺少保存文件名称,获取失败\n')
                # 弹出消息窗口
                messagebox.showerror(title='错误', message='请输入保存文件名称')
        # 用户没输入内容执行下面代码
        else:
            print('缺少章节编号,获取失败\n')
            # 弹出消息窗口
            messagebox.showerror(title='错误', message='请输入章节编号')

    # 用户没输入内容执行下面代码
    else:
        print('缺少小说编号,获取失败\n')
        # 弹出消息窗口
        messagebox.showerror(title='错误', message='请输入小说编号')

# 定义函数清理


def clean_1():
    # 判断用户输入内容的长度
    # 如果长度为0那么执行下面代码
    if len(var.get()) == 0:
        print('小说内容已为空')
        # 弹出消息窗口
        messagebox._show(message='输入框已为空')
    else:
        print('清理小说名')
        # 设置内容为空
        var.set('')

# 定义函数清理


def clean_2():
    # 判断用户输入内容的长度
    # 如果长度为0那么执行下面代码
    if len(var1.get()) == 0:
        print('章节内容已为空')
        # 弹出消息窗口
        messagebox._show(message='输入框已为空')
    else:
        print('清理章节名')
        # 设置内容为空
        var1.set('')

# 定义函数清理


def clean_3():
    # 判断用户输入内容的长度
    # 如果长度为0那么执行下面代码
    if len(var2.get()) == 0:
        print('文件名已为空')
        # 弹出消息窗口
        messagebox._show(message='输入框已为空')
    else:
        print('清理文件名')
        # 设置内容为空
        var2.set('')

# 定义函数打开网站


def open_web():
    print('\n打开网站')
    # 用webbrowser模块中的open方法打开指定网站
    webbrowser.open('https://www.dingdiann.net/ddk_1/')

# 定义函数,设置输入框内容


def jianlai():
    var.set('92482')  # 设置内容
    var2.set('剑来')  # 设置内容
    print('设置小说剑来')

# 定义函数设置窗口置顶


def ckzd():
    if var3.get() == 1:
        root.wm_attributes('-topmost', True)
        messagebox._show(message='窗口置顶')
        print('窗口置顶')
    else:
        root.wm_attributes('-topmost', False)
        messagebox._show(message='取消窗口置顶')
        print('取消窗口置顶')


def tmd(v):
    print('透明度:', v)
    root.attributes("-alpha", v)


# 设置窗口
root = tk.Tk()  # 创建窗口赋值给root
root.title('wone')  # 设置窗口名称
root.geometry('350x250+750+350')  # 设置窗口大小
root.iconbitmap('wone.ico')  # 设置窗口图标
root.minsize(350, 250)  # 设置最大窗口尺寸
root.maxsize(350, 250)  # 设置最小窗口尺寸
# 设置标签
label = tk.Label(root, text='推荐小说剑来:ddk92482',
                 font=('宋体', 14)).place(x=70, y=15)
label1 = tk.Label(root, text='输入ddk后数字:', font=('宋体', 10)).place(x=20, y=45)
label2 = tk.Label(root, text='输入最后数字:', font=('宋体', 10)).place(x=20, y=75)
label3 = tk.Label(root, text='输入保存文件名称:', font=('宋体', 10)).place(x=20, y=105)
# 输入框内容
var = tk.StringVar()
var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.IntVar()
# 输入框设置
entry = tk.Entry(root, textvariable=var).place(x=140, y=45)
entry2 = tk.Entry(root, textvariable=var1).place(x=140, y=75)
entry3 = tk.Entry(root, textvariable=var2).place(x=140, y=105)
# 按钮设置
button = tk.Button(root, text='获取', padx=30, pady=7, command=get,
                   bg='orange', fg='white').place(x=130, y=135)
button1 = tk.Button(root, text='清空', command=clean_1).place(x=290, y=40)
button2 = tk.Button(root, text='清空', command=clean_2).place(x=290, y=70)
button3 = tk.Button(root, text='清空', command=clean_3).place(x=290, y=100)
button4 = tk.Button(root, text='顶点小说网', command=open_web,
                    bg='orange', fg='blue').place(x=250, y=140)
button_jl = tk.Button(root, text='剑来', command=jianlai,
                      bg='orange', fg='yellow').place(x=40, y=140)
c1 = tk.Checkbutton(root, text='置顶', variable=var3, onvalue=1, offvalue=0,
                    command=ckzd).place(x=5, y=5)
s = tk.Scale(root, label='透明度', from_=0.2, to=1, orien=tk.HORIZONTAL,
             length=200, showvalue=0, tickinterval=0.2, resolution=0.1,
             command=tmd, sliderrelief='flat', troughcolor='orange', width=8).place(x=5, y=190)
# 刷新界面
root.mainloop()
