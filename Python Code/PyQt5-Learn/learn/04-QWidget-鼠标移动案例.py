# -*- coding: utf-8 -*-
# @Time     : 2021/7/8 16:59
# @Author   : Wone
# @File     : 04-QWidget-鼠标移动案例.py
# @Software : PyCharm

import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('窗口移动的学习')
        self.initUI()
        self.move_flag = False

    def initUI(self):
        pass

    def mousePressEvent(self, evt) -> None:
        if evt.button() == Qt.LeftButton:
            self.move_flag = True
            # print('鼠标按下')
            # 确定鼠标第一次按下的点位置
            self.mouse_x = evt.globalX()
            self.mouse_y = evt.globalY()
            print(self.mouse_x, self.mouse_y)

            # 确定窗口所在原始点位置
            self.origin_x = self.x()
            self.origin_y = self.y()

    def mouseMoveEvent(self, evt) -> None:
        if self.move_flag:
            print(evt.globalX(), evt.globalY())
            # 移动距离 = 鼠标拖动后的位置 - 第一次按下的位置
            move_x = evt.globalX() - self.mouse_x
            move_y = evt.globalY() - self.mouse_y
            print(move_x, move_y)
            self.move(self.origin_x + move_x, self.origin_y + move_y)

    def mouseReleaseEvent(self, evt) -> None:
        self.move_flag = False
        # print('鼠标释放')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    window.setMouseTracking(True)
    sys.exit(app.exec_())
