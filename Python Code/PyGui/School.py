import sys
import requests
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class School_Net_Login(QWidget):
    def __init__(self):
        super(School_Net_Login, self).__init__()

        self.url = 'http://10.1.1.22:801/eportal/?c=ACSetting&a=Login&wlanuserip=&wlanacip=&wlanacname=&redirect=&session=&vlanid=0&port=&iTermType=1&protocol=http:'

        self.data = {'DDDDD': '311041210@telecom',
                     'upass': '041210',
                     'R1': '0',
                     'R2': '',
                     'R6': '0',
                     'para': '00',
                     '0MKKey': '123456'
                     }

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
        self.initUI()

    def initUI(self):
        self.setWindowTitle('校园网连接')
        self.setWindowIcon(QIcon(r'C:\Users\wone\Desktop\Code\PyGame\img\kela.ico'))

        layout = QFormLayout()

        self.response = QTextEdit('校园网连接:')
        self.response.setReadOnly(True)
        layout.addWidget(self.response)

        layout1 = QVBoxLayout()

        self.button1 = QPushButton('请求连接')
        self.button1.setDefault(True)
        self.button1.clicked.connect(self.run)

        self.button2 = QPushButton('退出')
        self.button2.clicked.connect(self.quit)

        layout1.addWidget(self.button1)
        layout1.addWidget(self.button2)

        layout2 = QHBoxLayout()
        layout2.addLayout(layout)
        layout2.addLayout(layout1)

        self.setLayout(layout2)

    def quit(self):
        sys.exit(app.exec_())

    def requests(self):
        response = requests.post(self.url, self.data, headers=self.headers)
        return response

    def whether_connect(self):
        response = self.requests()
        if response.status_code == 200:
            self.response.append(f'响应代码:{response.status_code} 响应成功')
            if '您已经成功登录' in response.text:
                self.response.append('account: {}'.format(self.data['DDDDD']))
                self.response.append('password: {}'.format(self.data['upass']))
                self.response.append('登录成功')
            else:
                self.response.append('AC认证失败')
                self.response.append('网络测试中...')
                test_url = 'https://www.baidu.com/'
                self.response.append(f'测试网址: {test_url}')
                response_test = requests.get(test_url)
                if response_test.status_code == 200:
                    self.response.append(f'测试响应码: {response_test.status_code} 连接成功')
                    self.response.append('网络已连接成功,请勿重复登录')
                else:
                    self.response.append('测试失败,请重新尝试登录')
        else:
            self.response.append('响应失败,请重新尝试(时间已过或网线WIFI未连接)')

    def run(self):
        self.whether_connect()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = School_Net_Login()
    main.show()
    sys.exit(app.exec_())
