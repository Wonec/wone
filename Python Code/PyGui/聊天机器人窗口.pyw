import tkinter as tk
import requests
import json
import sys
from tkinter import messagebox

class ChatBotWindow(object):
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('500x200')
        self.window.iconbitmap('wone.ico')
        self.window.title('聊天机器人')
        self.my_var = tk.StringVar()
        self.bot_var = tk.StringVar()
        self.label1 = tk.Label(self.window, text='机器人:').place(x=10, y=20)
        self.label2 = tk.Label(self.window, text='我:').place(x=150, y=70)
        self.entry1 = tk.Entry(self.window, width=60, state='readonly', fg='blue', textvariable=self.bot_var).place(x=60, y=20)
        self.entry1 = tk.Entry(self.window, textvariable=self.my_var).place(x=175, y=70)
        self.button = tk.Button(self.window, text='发送', command=self.main, width=10, height=2).place(x=200, y=120)
        self.url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg='
        self.bot_var.set('您好！这里是大聪明，非常欢迎您的到来，有什么想和我聊聊的吗？')

    def get_response(self):
        response = requests.get(url=self.new_url).text
        return response

    def extract_response(self):
        data = json.loads(self.get_response())
        text = data['content'].replace('菲菲', '大聪明').replace('{br}', '\n')
        self.bot_var.set(text)

    def main(self):
        if self.my_var.get() == 'q':
            off = messagebox.askyesno(message='是否退出程序')
            if off == True:
                sys.exit()
            else:
                pa
        elif len(self.my_var.get()) == 0:
            messagebox.showerror(message='内容为空,请输入内容')

        else:
            self.new_url = self.url + self.my_var.get()
            self.get_response()
            self.extract_response()



if __name__ == '__main__':
    exe = ChatBotWindow()
    exe.window.mainloop()
