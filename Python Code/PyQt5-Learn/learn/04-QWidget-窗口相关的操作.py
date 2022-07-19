# -*- coding: utf-8 -*-
# @Time     : 2021/7/8 18:06
# @Author   : Wone
# @File     : 04-QWidget-窗口相关的操作.py
# @Software : PyCharm
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def mousePressEvent(self, QMouseEvent):

        if self.isMaximized():  # 判断当前是否是最大化
            self.showNormal()  # 展示正常窗口
        else:
            self.showMaximized()


# 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()
# 2.2 设置控件
window.resize(500, 500)
window.setWindowTitle('w1')

# icon = QIcon('img/kela.ico')
# window.setWindowIcon(icon)
#
# # QIcon
# print(window.windowIcon())
#
# window.setWindowTitle('wone')
# print(window.windowTitle())
#
# window.setWindowOpacity(0.7)  # 设置不透明度 float型 取值范围0.0-1.0
# print(window.windowOpacity())

# print(window.windowState() == Qt.WindowNoState)

# window.setWindowState(Qt.WindowMinimized)  # 最小化
# window.setWindowState(Qt.WindowMaximized)  # 最大化
# window.setWindowState(Qt.WindowFullScreen)  # 全屏


# w2 = QWidget()
# w2.setWindowTitle('w2')


# 2.3 展示控件
window.show()
# w2.show()

# window.showMaximized()
# window.showFullScreen()
# window,showMinimized()
# window.setWindowState(Qt.WindowActive)  # 设置活动状态 放在前面

# 3. 应用程序的执行 进入到消息循环
sys.exit(app.exec_())
