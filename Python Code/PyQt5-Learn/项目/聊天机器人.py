import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import json
import requests
import random


class ChatBot(QWidget): # 继承自父类QWidget
    def __init__(self):  # 自己的初始化参数涉资
        super(ChatBot, self).__init__()  # 初始化父类的方法
        self.url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg='
        self.initUI()  # 调用initUI方法

    def initUI(self):
        self.setWindowTitle('聊天机器人')  # 设置窗口标题
        self.setWindowIcon(QIcon(r'C:\Users\wone\Desktop\PythonCode\Practice\SchoolNetLoginGui\kela.ico'))  # 设置窗口图标QIcon传入图标所在地址

        layout = QFormLayout()  # 实例化QFormLayout对象 表单布局

        self.botBack = QTextEdit()  # 实例化QTextEdit对象
        self.botBack.setReadOnly(True)  # 打开只读模式 设置为True
        self.botBack.setText('您好！这里是大聪明，非常欢迎您的到来，有什么想和我聊聊的吗？')  # 设置内容
        layout.addRow('机器人:', self.botBack)  # 添加到布局

        self.myMsg = QLineEdit()  # 实例化QLineEdit对象
        layout.addRow('我:', self.myMsg)  # 添加到布局

        layout1 = QHBoxLayout()  # 实例化QHBoxLayout对象 横向布局

        self.button1 = QPushButton('发送消息')  # 实例化QPushButton对象 设置按钮文本内容
        self.button1.setDefault(True)  # 设置为默认选择 当聚焦在按钮上时回车键点击按钮
        self.button1.clicked.connect(self.run)  # 连接槽函数 触发信号为clicked单击按钮

        layout1.addLayout(layout)  # 横向布局添加前布局
        layout1.addWidget(self.button1)  # 横向布局添加按钮控件

        self.setLayout(layout1)  # 设置布局为横向布局

    def get_response(self, new_url):  # 网页的请求方法 get请求
        response = requests.get(url=new_url).text
        return response

    def extract_response(self):  # 解析请求返回数据 response
        data = json.loads(self.get_response())  # 转换为json格式
        text = data['content'].replace('菲菲', '大聪明').replace('{br}', '\n')  # 提取出需要的数据 列表的提取方法
        self.botBack.setText(text)  # 提取到的数据设置到机器人的回复框

    def run(self):
        if self.myMsg.text() == 'quit':  # 当输入框内容为quit时结束程序
            # sys.exit(app.exec_())
            self.close()
        elif self.myMsg.text() == '':  # 当输入框为空时 设置机器人回复内容
            texts = ['未获取到相关信息', '您的输入为空', '输入框没有内容', '请输入消息哦', '没有获取到消息']  # 设置默认回复消息
            text = texts[random.randint(0, 4)]  # 随机选择消息
            self.botBack.setText(text)  # 设置到机器人的回复框
        else:
            new_url = self.url + self.myMsg.text()  # 拼接url
            self.get_response(new_url)  # 调用请求方法传入拼接的url
            self.extract_response()  # 调用解析数据方法




if __name__ == '__main__':
    app = QApplication(sys.argv)  # 实例化QApplication对象
    main = ChatBot()  # 实例化ChatBot对象
    main.show()  # 控件展示
    sys.exit(app.exec_())  # 程序循环消息
