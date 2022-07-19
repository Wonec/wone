from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys

class WebEngineView(QWebEngineView):  # 继承自父类QWebENgineView
    def createWindow(self, QWebEnginePage_WebWindowType):  # 重写createWindow方法
        # 返回当前窗口
        return self

class Browser(QMainWindow):  # 继承自父类QMainWindow
    def __init__(self):  # 类初始化
        super(Browser, self).__init__()  # 父类的初始化方法
        self.initUI()  # 调用initUI方法

    def initUI(self):
        self.setWindowTitle('Wone-Browser')  # 设置窗口标题
        self.showMaximized()  # 设置窗口最大化

        self.browser = WebEngineView(self)  # 实例化WebEnginView对象
        self.browser.setUrl(QUrl('https://baidu.com'))  # 设置初始的url
        self.setCentralWidget(self.browser)  # 将browser设置为居中控件

        # 导航栏
        navbar = QToolBar()  # 实例化QToolBar对象 工具栏
        self.addToolBar(navbar)  # 添加工具栏

        back_btn = QAction('Back', self)  # 实例化QAction对象 工具栏按钮
        back_btn.triggered.connect(self.browser.back)  # 当触发时连接槽函数
        navbar.addAction(back_btn)  # 添加Action按钮 到工具栏

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()  #  实例化QLineEdit对象 网址输入框
        self.url_bar.returnPressed.connect(self.navigate_to_url)  # 当回车确认时连接槽函数
        navbar.addWidget(self.url_bar)  # 添加控件到工具栏

        self.browser.urlChanged.connect(self.update_url)  # 当浏览器url变化时连接槽函数

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://baidu.com'))  # 回到最初设置的url地址

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(str(url)))  # 进入搜索的url地址

    def update_url(self, url):
        self.url_bar.setText(url.toString())  # 网页切换时设置地址栏为当前网页地址


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r'C:\Users\wone\Desktop\PythonCode\Practice\SchoolNetLoginGui\kela.ico'))
    main = Browser()  # 实例化Browser类
    main.show()  # 展示窗口
    sys.exit(app.exec_())  # 程序消息循环
