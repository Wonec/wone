# 导入模块
import re
import tkinter as tk
from urllib import parse
import tkinter.messagebox as msgbox
import webbrowser


class App:
    # 重写构造函数 创建类属性
    def __init__(self):
        # 软件名称
        self.title = ' WONE'
        self.image = 'wone.ico'

        # tk对象
        self.root = tk.Tk(className=self.title)
        self.root.iconbitmap(self.image)
        self.root.attributes('-alpha', 0.9)
        self.root.geometry('650x180')

        # 变量接受用户输入的电影地址，并且对地址做处理
        self.url = tk.StringVar()
        # 控制单选框默认选中的属性
        self.v = tk.IntVar()
        self.v.set(1)

        # 软件空间划分
        frame1 = tk.Frame(self.root)
        frame2 = tk.Frame(self.root)

        # 软件控件内容设置
        self.group = tk.Label(frame1, text='播放通道:', padx=10, pady=10)
        self.tb = tk.Radiobutton(
            frame1, text='唯一通道', variable=self.v, value=1, width=10, height=3)

        self.label = tk.Label(frame2, text='请输入视频播放地址:')
        self.entry = tk.Entry(frame2, textvariable=self.url, highlightcolor='black',
                              highlightthickness=1, width=30, fg='green', font=('微软雅黑体', 12))
        self.play = tk.Button(frame2, text='播放', font=(
            '微软雅黑体', 12), width=2, height=1, command=self.video_play)
        self.clear = tk.Button(frame2, text='清空', font=(
            '微软雅黑体', 12), width=2, height=1, command=self.clear)
        self.tx = tk.Button(frame2, text='腾讯视频', font=(
            '微软雅黑体', 10), width=5, height=1, command=self.open_tx)
        self.iqy = tk.Button(frame2, text='爱奇艺视频', font=(
            '微软雅黑体', 10), width=5, height=1, command=self.open_iqy)
        self.yk = tk.Button(frame2, text='优酷视频', font=(
            '微软雅黑体', 10), width=5, height=1, command=self.open_yk)

        # 控件布局
        # 激活空间
        frame1.pack()
        frame2.pack()
        # 位置确定
        self.group.grid(row=0, column=0)
        self.tb.grid(row=0, column=1)

        self.label.grid(row=0, column=0)
        self.entry.grid(row=0, column=1)
        self.play.grid(row=0, column=2, ipadx=10, ipady=10, padx=4, pady=10)
        self.clear.grid(row=0, column=3, ipadx=10, ipady=10, )
        self.tx.grid(row=1, column=0, ipadx=15, ipady=5)
        self.iqy.grid(row=1, column=1, ipadx=15, ipady=5)
        self.yk.grid(row=1, column=2, ipadx=15, ipady=5)

    # 定义播放按钮的事件函数
    # 解析电影
    def video_play(self):
        # 第三方播放解析api
        port = 'http://www.wmxz.wang/video.php?url='
        # 判断用户输入的电影地址是否合法
        if re.match(r'https?:/{2}\w.+$', self.url.get()):
            ip = self.url.get()
            ip = parse.quote_plus(ip)
            # 自动打开浏览器
            webbrowser.open(port + ip)
        elif len(self.url.get()) == 0:
            msgbox.showwarning(title='提示', message='视频地址栏输入为空')
        else:
            msgbox.showerror(title='错误', message='视频地址不合法,请重新输入')

    def clear(self):
        # 清空输入栏内容
        if len(self.url.get()) != 0:
            self.entry.delete(0, 'end')
        else:
            msgbox.showwarning(title='提示', message='输入框已为空')

    def open_tx(self):
        webbrowser.open('https://v.qq.com/')

    def open_iqy(self):
        webbrowser.open('https://www.iqiyi.com/')

    def open_yk(self):
        webbrowser.open('https://www.youku.com/')

    # 如何启动软件
    def loop(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.loop()
