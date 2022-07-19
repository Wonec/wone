# -*- coding: utf-8 -*-
# @Time     : 2021/7/8 12:48
# @Author   : Wone
# @File     : 04-QWidget-事件消息.py
# @Software : PyCharm

import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('事件消息的学习')
        self.initUI()

    def initUI(self):
        pass

    def showEvent(self, a0: QShowEvent) -> None:  # 窗口展示事件消息
        print('窗口被展示了出来')

    def closeEvent(self, a0: QCloseEvent) -> None:  # 窗口关闭事件消息
        print('窗口被关闭了')

    def moveEvent(self, a0: QMoveEvent) -> None:  # 窗口移动事件消息
        print('窗口被移动了')

    def resizeEvent(self, a0: QResizeEvent) -> None:  # 窗口尺寸改变事件消息
        print('窗口改变了尺寸大小')

    def enterEvent(self, a0: QEvent) -> None:   # 鼠标进入事件消息
        print('鼠标进来了')
        self.setStyleSheet('background-color: yellow;')

    def leaveEvent(self, a0: QEvent) -> None:  # 鼠标移出事件消息
        print('鼠标移开了')
        self.setStyleSheet('background-color: green;')

    def mousePressEvent(self, a0: QMouseEvent) -> None:  # 鼠标按下事件消息
        print('鼠标被按下')

    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:  # 鼠标松开事件消息
        print('鼠标被释放')

    def mouseDoubleClickEvent(self, a0: QMouseEvent) -> None:  # 鼠标双击事件消息
        print('鼠标双击')

    def mouseMoveEvent(self, a0: QMouseEvent) -> None:  # 鼠标移动事件消息(按下移动)
        print('鼠标移动')

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        print('键盘某个按键被按下了')

    def keyReleaseEvent(self, a0: QKeyEvent) -> None:
        print('键盘上某一个按键被释放了')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
