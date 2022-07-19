# -*- coding: utf-8 -*-
# @Time     : 2021/7/8 15:09
# @Author   : Wone
# @File     : 04-QWidget-案例1.py
# @Software : PyCharm

from PyQt5.Qt import *
import sys


class MyLabel(QLabel):  # 继承自父类QWidget
    def enterEvent(self, a0: QEvent) -> None:  # 重写鼠标进入方法
        print('鼠标进入')
        self.setText('欢迎光临')  # 设置标签标题

    def leaveEvent(self, a0: QEvent) -> None:
        print('鼠标离开')
        self.setText('谢谢惠顾')  # 设置标签标题

    def keyReleaseEvent(self, evt) -> None:
        print('xxx')
        # if evt.key() == Qt.Key_Tab:  # 通过evt.key进行判断
        #     print('用户按下了Tab建')
        # if evt.modifiers() == Qt.ControlModifier and evt.key() == Qt.Key_S:  # Ctrl是修饰键
        #     print('用户按下了组合键Ctrl+S')
        if evt.modifiers() == Qt.ControlModifier | Qt.ShiftModifier and evt.key() == Qt.Key_A:  # 多个修饰键需要 | 连接
            print('用户按下了组合键Ctrl+Shift+A')


# 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('鼠标操作的案例')
window.resize(500, 500)

label = MyLabel(window)  # 实例化MyLable父对象为window
label.resize(200, 200)
label.move(100, 100)
label.setStyleSheet('background-color: cyan;')
label.grabKeyboard()

# 2.3 展示控件
window.show()
# 3. 应用程序的执行 进入到消息循环
sys.exit(app.exec_())
