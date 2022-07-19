import re
import requests
import tkinter as tk
from tkinter import messagebox
import webbrowser

# 导入模块

root = tk.Tk()  # 创建窗口
root.title('wone')  # 窗口名称
root.geometry('400x200')  # 窗口大小
root.iconbitmap('wone.ico')  # 窗口图标
# root.configure(bg='black')  # 窗口背景颜色
root.minsize(400, 200)  # 最小窗口
root.maxsize(400, 200)  # 最大窗口


def get():
    # 测试代码
    try:
        url = 'https://www.jianlaixiaoshuo.net/'  # 设置网址

        headers = {  # 设置头部信息
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
        }

        response = requests.get(url=url, headers=headers)  # 获取网页信息

        # print(response.text)

        titles = re.findall('title="(.*?) 字数', response.text)  # 正则表达式获取章节名称 获取的是列表

        if var.get():  # 如果输入框有内容
            if int(var.get()) <= 178:  # 网页排版178章之后有问题 所以这里需要判断
                e = int(var.get()) + 4  # 前四章是上架感言什么的 需要的话可以输入-1 -2 -3 -4获取 赋值给变量e
                c = e - 1  # 获取的章节列表是从0开始算索引 所以要-1才能和网址对应 赋值给变量c

            elif int(var.get()) > 178 and int(var.get()) <= 230:  # 这里对排版错误的178章之后进行判断
                e = int(var.get()) + 98  # 178章之后的内容要加上98 排版多出了98页重复的章节
                c = e - 1

            elif int(var.get()) > 230 and int(var.get()) <= 455:  # 这后面的判断是总管的章节错误了 出现重复 所以这里会丢失一章小说 为了整体功能
                e = int(var.get()) + 99  # 丢失的请自行找到第二个230章进行观看
                c = e - 1

            elif int(var.get()) > 455 and int(var.get()) <= 753:  # 这里没有丢失 是多了一章的总管请假 干
                e = int(var.get()) + 100
                c = e - 1

            elif int(var.get()) > 753 and int(var.get()) <= 819:  # 这里e + 2是因为多了一章请假 所以还是总管的错
                e = int(var.get()) + 101  # +101 没发现重复章节 应该是网页排版错误
                c = e - 2

            elif int(var.get()) > 819 and int(var.get()) <= 845:  # 同样的章节重复 第二个819章 需要自行观看 为了整体功能
                e = int(var.get()) + 102
                c = e - 2

            elif int(var.get()) > 845 and int(var.get()) <= 873:  # 同样的章节重复 第二个845章 需要自行观看 为了整体功能
                e = int(var.get()) + 103
                c = e - 2

            elif int(var.get()) > 873 and int(var.get()) < 878:  # 同样的章节重复 第二个873章 需要自行观看 为了整体功能
                e = int(var.get()) + 104
                c = e - 2
            elif int(var.get()) >=878:
                e = int(var.get()) + 105
                c = e - 2

            print('剑来:')

            a = "https://www.jianlaixiaoshuo.net/book/" + str(e) + ".html"  # 指定小说指定章节网址

            response1 = requests.get(url=a, headers=headers)  # 获取指定小说章节内容

            print(f'获取章节:《{titles[c]}》')
            print(f'获取网址:{a}')

            txt = re.findall('<p>(.*?)</p>', response1.text)  # 正则表达式获取小说内容 这里获取的是列表形式

            for item in txt:  # for循环遍历列表一个个赋值给item
                with open(titles[c] + '.txt', 'a') as f:  # with open保存文件名称就是title列表的c索引
                    i = '\t' + item + '\n' + '\n'  # 直接获取的内容紧凑 加上制表符(python中是4个空格) 换行符 加强观看体验
                    f.write(i)  # 写入文件

            print('获取成功\n')
        else:
            messagebox.showerror(title='错误', message='请输入内容')  # 弹出错误窗口 提示输入内容
    except ValueError:
        messagebox.showerror(title='错误', message='请输入整数')  # 弹出错误窗口 提示输入整数
    except IndexError:
        messagebox.showerror(title='错误', message='请输入正确的章节数')  # 弹出错误窗口 提示输入正确的章节数


def get_e():
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

    num = 0  # 设置变量来当作titles的索引

    # 设置循环爬取内容
    for x in xs_url:
        t = titles[num]
        num += 1  # 每次循环加1

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

def open_web():
    webbrowser.open('https://www.jianlaixiaoshuo.net/')

var = tk.StringVar()  # 设置输入框的内容字符串格式
var.set('')  # 设置初始文本框内容

la = tk.Label(root, text='输入想获取的章数:', font=('微软雅黑', 12), fg='orange').place(x=135, y=10)

en = tk.Entry(root, textvariable=var, font=('微软雅黑', 12), fg='orange', highlightcolor='orange', relief='ridge').place(
    x=110, y=40)

bu = tk.Button(root, text='获取', command=get, font=('微软雅黑', 12), fg='orange', relief='ridge', width=8).place(x=155, y=75)

bu1 = tk.Button(root, text='获取全部', command=get_e, font=('微软雅黑', 12), fg='orange', relief='ridge', width=8).place(x=155,
                                                                                                                 y=120)

la1 = tk.Label(root, text='制作者QQ:2860874824', font=('微软雅黑', 14), fg='orange').place(x=0, y=175)

bu2 = tk.Button(root,text='小说网站', font=('微软雅黑', 12), fg='orange', relief='ridge', command=open_web).place(x=0,y=0)
# 设置控件标签 输入框 两个按钮 一个标签

root.mainloop()  # 窗口显示
