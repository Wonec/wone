# -*- coding: utf-8 -*-
# @Time     : 2021/7/9 19:22
# @Author   : Wone
# @File     : 04-QWidget-顶层窗口操作-案例.py
# @Software : PyCharm


from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.99)
        # 2.2 设置控件
        self.setWindowTitle('顶层窗口操作-案例')
        self.resize(500, 500)
        self.move_flag = False

        # 公共数据
        self.top_margin = 10
        self.btn_w = 80
        self.btn_h = 40

        self.initUI()

    def initUI(self):

        # 添加三个子空间 - 窗口的右上角
        self.close_btn = QPushButton(self)
        self.close_btn.setText('关闭')
        self.close_btn.resize(self.btn_w, self.btn_h)

        self.max_btn = QPushButton(self)
        self.max_btn.setText('最大化')
        self.max_btn.resize(self.btn_w, self.btn_h)

        self.min_btn = QPushButton(self)
        self.min_btn.setText('最小化')
        self.min_btn.resize(self.btn_w, self.btn_h)

        self.close_btn.pressed.connect(self.close)

        def max_normal():
            if self.isMaximized():
                self.showNormal()
                self.max_btn.setText('最大化')
            else:
                self.showMaximized()
                self.max_btn.setText('恢复')

        self.max_btn.pressed.connect(max_normal)
        self.min_btn.pressed.connect(self.showMinimized)

    def resizeEvent(self, QResizeEvent):
        print('窗口大小发生了改变')
        # close_btn_w = btn_w
        window_w = self.width()
        close_btn_x = window_w - self.btn_w
        close_btn_y = self.top_margin
        self.close_btn.move(close_btn_x, close_btn_y)

        max_btn_x = close_btn_x - self.btn_w
        max_btn_y = self.top_margin
        self.max_btn.move(max_btn_x, max_btn_y)

        min_btn_x = max_btn_x - self.btn_w
        min_btn_y = self.top_margin
        self.min_btn.move(min_btn_x, min_btn_y)

    def mousePressEvent(self, evt):
        # 判定点击的是否是鼠标左键
        # 在此处设计一个标记, 用作判断是否需要移动
        # 窗口的原始坐标
        # 鼠标按下的点
        if evt.button() == Qt.LeftButton:
            self.move_flag = True
            self.mouse_x = evt.globalX()
            self.mouse_y = evt.globalY()

            self.origin_x = self.x()
            self.origin_y = self.y()

    def mouseMoveEvent(self, evt):
        # if 窗口移动标记 == True:
        # 根据鼠标按下的点 计算移动向量
        # 根据移动向量 和窗口的原始坐标 = 最小坐标
        # 移动整个窗口的位置
        if self.move_flag:
            move_x = evt.globalX() - self.mouse_x
            move_y = evt.globalY() - self.mouse_y
            self.move(move_x + self.origin_x, move_y + self.origin_y)

    def mouseReleaseEvent(self, evt):
        self.move_flag = False
        # 把这个标记进行重置


# 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
# window = QWidget(flags=Qt.FramelessWindowHint)
window = Window()

# 2.3 展示控件
window.show()
# 3. 应用程序的执行 进入到消息循环
sys.exit(app.exec_())
