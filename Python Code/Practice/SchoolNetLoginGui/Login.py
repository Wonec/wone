import sys
import requests
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Login(QWidget):

    def __init__(self):
        super(Login, self).__init__()
        # 声明控件
        self.combobox = QComboBox()
        self.textEdit = QTextEdit('输出:')
        self.lineEdit = QLineEdit()
        self.lineEdit1 = QLineEdit()
        self.button = QPushButton('登录')
        self.button1 = QPushButton('保存')
        self.button2 = QPushButton('退出')
        # 设置空变量 用于接收后面的数据
        self.operator = None
        self.start_pos = None
        # 学校网址 用来发送请求
        self.url = 'http://10.1.1.22:801/eportal/?c=ACSetting&a=Login&wlanuserip=&wlanacip=&wlanacname=&redirect=&session=&vlanid=0&port=&iTermType=1&protocol=http:'
        # headers 伪装成浏览器发送请求
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'suffixType=@telecom; PHPSESSID=rre1coi1p0h6hs2oaua38cvb23',
            'Host': '10.1.1.22',
            'Referer': 'http://10.1.1.22/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
        }

        self.resize(520, 360)
        self.setWindowIcon(QIcon('kela.ico'))  # ico图标
        self.setAttribute(Qt.WA_TranslucentBackground)  # 背景透明
        self.setWindowFlags(Qt.WindowStaysOnTopHint |
                            Qt.FramelessWindowHint)  # 窗口置顶 无边框

        self.init_ui()  # 调用UI方法
        self.set_text()  # 调用设置内容到输入框combobox方法
        self.combobox_change()  # 调用通过选项设置运营商方法

    def init_ui(self):
        # 基本界面数据及控件
        labelStyle1 = """QLabel
                        {
                            background:#9D9D9D;
                            color:orange;
                            box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 8px;font-family: 微软雅黑;
                        }"""

        labelStyle2 = """QLabel
                        {
                            background:#6C6C6C;
                            color:white;
                            box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:14px;border-radius: 8px;font-family: 微软雅黑;
                        }
                        QLabel:hover
                        {
                            background:#8D8D8D;
                            color:pink;
                        }
                        """

        lineEditStyle = """QLineEdit
                            {
                                background:#6C6C6C;
                                color:white;
                                box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 8px;font-family: 微软雅黑;
                            }
                            QLineEdit:hover
                            {
                                background:#4D4D4D;
                            }"""

        pushButtonStyle1 = """QPushButton
                            {
                                background:#6C6C6C;
                                color:white;
                                box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:15px;border-radius: 5px;font-family: 微软雅黑;
                            }
                            QPushButton:hover
                            {
                                background:#3A4B5C;
                            }
                            QPushButton:pressed
                            {
                                border: 1px solid #3C3C3C!important;
                            }"""

        pushButtonStyle2 = """QPushButton
                            {
                                background:#9D9D9D;
                                box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 8px;font-family: 微软雅黑;
                            }
                            QPushButton:hover
                            {
                                background:#6C6C6C;
                            }
                            QPushButton:pressed
                            {
                                border: 1px solid #3C3C3C!important;
                            }"""

        textEditStyle = """QTextEdit
                            {
                                background:#6C6C6C;color:black;
                                box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 8px;font-family: 微软雅黑;
                            }
                            QTextEdit:hover
                            {
                                background:#8D8D8D;
                            }"""

        # 用来当作背景的标签
        background_label = QLabel(self)
        background_label.setGeometry(0, 0, 520, 360)
        background_label.setStyleSheet(labelStyle1)

        # Logo
        image = QPixmap('kela.ico')
        logo_label = QLabel()
        logo_label.setPixmap(image)

        # 标签内容 字体居中 设置字体
        prompt_label = QLabel(
            '第一次使用请输入账号密码\n点击保存按钮写入到文件\n下次使用就可以直接读取\n生成的user.text文件不要删除\n与程序放在同一目录下即可\n作者: Wone')
        prompt_label.setStyleSheet(labelStyle2)
        prompt_label.setAlignment(Qt.AlignCenter)

        self.lineEdit.setStyleSheet(lineEditStyle)
        self.lineEdit.setPlaceholderText('username')

        self.lineEdit1.setStyleSheet(lineEditStyle)
        self.lineEdit1.setPlaceholderText('password')
        self.lineEdit1.setEchoMode(QLineEdit.PasswordEchoOnEdit)  # 显示设置密码

        self.combobox.addItems(['学校', '电信', '移动', '联通'])
        self.combobox.setView(QListView())
        self.combobox.currentIndexChanged.connect(
            self.combobox_change)  # combobox更改调用

        self.button.setStyleSheet(pushButtonStyle1)
        self.button.clicked.connect(self.login)

        self.button1.setStyleSheet(pushButtonStyle1)
        self.button1.clicked.connect(self.save)

        self.button2.setStyleSheet(pushButtonStyle1)
        self.button2.clicked.connect(self.close)

        self.textEdit.setStyleSheet(textEditStyle)
        self.textEdit.setReadOnly(True)  # 设置状态为只读

        # 账号密码输入框及布局
        f_layout = QFormLayout()
        # 登录按钮布局
        h_layout = QHBoxLayout()
        # 保存按钮以及退出按钮布局
        h_layout_1 = QHBoxLayout()
        # 输出消息框及横向布局
        h_layout_2 = QHBoxLayout()
        # 提示文本及竖向布局的添加
        v_layout = QVBoxLayout()
        # 第一行布局头像与总体布局
        v_layout_1 = QVBoxLayout()

        # 添加输入及选择框
        f_layout.addRow('账号:', self.lineEdit)
        f_layout.addRow('密码:', self.lineEdit1)
        f_layout.addRow('运营商:', self.combobox)

        # 添加登录按钮
        h_layout.addWidget(self.button)

        # 添加保存退出按钮
        h_layout_1.addWidget(self.button1)
        h_layout_1.addWidget(self.button2)

        h_layout_2.addWidget(self.textEdit)  # 添加输出框
        h_layout_2.addLayout(v_layout)  # 添加竖向布局

        v_layout.addWidget(prompt_label)  # 添加提示文本
        v_layout.addLayout(f_layout)  # 添加输入选择框
        v_layout.addLayout(h_layout)  # 添加登录按钮
        v_layout.addLayout(h_layout_1)  # 添加保存退出按钮

        v_layout_1.addWidget(logo_label)  # 添加Logo
        v_layout_1.addLayout(h_layout_2)  # 添加横向布局

        # 设置布局
        self.setLayout(v_layout_1)

        # Author
        label3 = QLabel(self)
        label3.setText('Wone')
        label3.setStyleSheet(
            '''QLabel{font-size:16px;color: white;font-family: 微软雅黑;}''')
        label3.move(60, 25)

        # 退出按钮
        button1 = QPushButton(self)
        button1.setText('×')
        button1.setGeometry(480, 10, 30, 30)
        button1.setStyleSheet(pushButtonStyle2)
        button1.clicked.connect(self.close)

    def get_text(self):
        # 从文件获取内容
        user_list = []  # 创建一个空列表 用来存放账号密码运营商选择

        # 尝试打开文件
        try:
            with open('user.txt', 'r+') as f:
                for line in f.readlines():
                    user_list.append(line)

        # 报错文件未找到则创建一个文件
        except FileNotFoundError:
            f = open('user.txt', 'w')
            f.close()

        return user_list

    def set_text(self):
        # 设置文件获取的内容
        try:
            # 用三个变量接收 get_text返回的数据
            user_list = self.get_text()

            # 判断operator的内容选择combobox选项
            if user_list[2] == '@acac':
                self.combobox.setCurrentIndex(0)
            if user_list[2] == '@telecom':
                self.combobox.setCurrentIndex(1)
            if user_list[2] == '@cmcc':
                self.combobox.setCurrentIndex(2)
            if user_list[2] == '@unicom':
                self.combobox.setCurrentIndex(3)

            # 设置输入框内容 去除两侧空格
            self.lineEdit.setText(user_list[0].strip())
            self.lineEdit1.setText(user_list[1].strip())

        except TypeError:
            pass
        except IndexError:
            pass

    def combobox_change(self):
        # 判断combobox选中内容来给全局变量赋值
        if self.combobox.currentText() == '学校':
            self.operator = '@acac'
        if self.combobox.currentText() == '电信':
            self.operator = '@telecom'
        if self.combobox.currentText() == '移动':
            self.operator = '@cmcc'
        if self.combobox.currentText() == '联通':
            self.operator = '@unicom'

    def requests_post(self):
        # 发送post请求
        self.data = {'DDDDD': self.lineEdit.text() + self.operator,
                     'upass': self.lineEdit1.text(),
                     'R1': '0',
                     'R2': '',
                     'R6': '0',
                     'para': '00',
                     '0MKKey': '123456'
                     }

        response = requests.post(
            url=self.url, data=self.data, headers=self.headers, timeout=2)
        return response

    def whether_connect(self):
        # 判断连接是否成功 并显示在输出框方法
        try:
            # 接收requests方法返回的数据
            response = self.requests_post()

            if response:
                # 判断是否响应成功
                if response.status_code == 200:
                    self.textEdit.append(f'响应代码:{response.status_code} 响应成功')
                    # 判断是否成功登录
                    if '您已经成功登录' in response.text:
                        self.textEdit.append(
                            'account: {}'.format(self.data['DDDDD']))
                        self.textEdit.append(
                            'password: {}'.format(self.data['upass']))
                        self.textEdit.append('登录成功')
                    # 失败检查网络连接是否成功
                    else:
                        self.textEdit.append(
                            'AC认证失败,请检查账号密码以及是否重复登录\n网络测试中······')
                        # 用来测试的网址
                        test_url = 'https://www.baidu.com/'
                        self.textEdit.append(
                            f'测试网址: <a href="#">{test_url}</a>')
                        # 向测试网址发送请求
                        response_test = requests.get(test_url)
                        # 判断是否响应成功
                        if response_test.status_code == 200:
                            self.textEdit.append(
                                f'测试响应码: {response_test.status_code} 连接成功')
                            self.textEdit.append('网络已连接成功,请勿重复登录')
                        # 失败则输出消息
                        else:
                            self.textEdit.append('测试失败,请重新尝试登录')
                # 失败输出消息
                else:
                    self.textEdit.append('响应失败,请重新尝试(超时或网线WIFI未连接)')
            # 否则跳过
            else:
                pass

        except requests.Timeout:
            self.textEdit.append('错误！请检查网络连接')
            QMessageBox.critical(self, '错误', '请检查网络连接')

    def login(self):
        # 判断输入框是否为空 空则弹出消息框
        if len(self.lineEdit.text()) == 0:
            QMessageBox.warning(self, '警告', '账号不能为空')
        elif len(self.lineEdit1.text()) == 0:
            QMessageBox.warning(self, '警告', '密码不能为空')
        # 不为空执行登录 并判断是否连接成功
        else:
            self.textEdit.setText('连接状态:')
            self.whether_connect()

    def save(self):
        # 根据输入框以及combobox内容写入到文件方法
        # 当输入框不为空时执行
        if self.lineEdit.text() and self.lineEdit1.text():
            # 打开文件写入数据
            with open('user.txt', 'w') as f:
                f.write(
                    f'{self.lineEdit.text()}\n{self.lineEdit1.text()}\n{self.operator}')

            self.textEdit.setText('写入信息:\n')
            self.textEdit.append(f'账号: {self.lineEdit.text()}\n')
            self.textEdit.append(f'密码: {len(self.lineEdit1.text()) * "*"}\n')
            self.textEdit.append(f'运营商: {self.combobox.currentText()}')
            QMessageBox.information(self, '保存', '保存成功')
        else:
            QMessageBox.warning(self, '警告', '输入框不可为空')

    def mousePressEvent(self, QEvent):  # 响应鼠标点击
        self.start_pos = QEvent.pos()  # 记录第一下鼠标点击的坐标

    def mouseMoveEvent(self, QEvent):
        try:
            self.move(self.pos() + QEvent.pos() - self.start_pos)
        except TypeError:
            pass


# 程序入口 实例化对象 UI显示
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = School()
    main.show()
    sys.exit(app.exec_())
