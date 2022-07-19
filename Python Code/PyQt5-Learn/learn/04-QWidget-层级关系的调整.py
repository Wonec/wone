# -*- coding: utf-8 -*-
# @Time     : 2021/7/8 17:57
# @Author   : Wone
# @File     : 04-QWidget-层级关系的调整.py
# @Software : PyCharm

from PyQt5.Qt import *
import sys

# 解决方法 1
# class Label(QLabel):
#     def mousePressEvent(self, evt) -> None:
#         self.raise_()

# 解决方法 2
class Window(QWidget):
    def mousePressEvent(self, evt) -> None:
        mouse_x = evt.x()
        mouse_y = evt.y()
        sub_widget = self.childAt(mouse_x, mouse_y)
        sub_widget.raise_()

# 创建一个应用程序对象
app = QApplication(sys.argv)


# 2. 控件的操作
# 2.1 创建控件
window = Window()
# 2.2 设置控件
window.setWindowTitle('层级关系调整')
window.resize(500, 500)

label1 = QLabel(window)
label1.setText('标签1')
label1.resize(200, 200)
label1.setStyleSheet('background-color: red;')

label2 = QLabel(window)
label2.setText('标签2')
label2.resize(200, 200)
label2.setStyleSheet('background-color: green;')
label2.move(100, 100)

# label2.lower()  # label2层级关系下降
# label1.raise_()  # label1层级关系山上升

label2.stackUnder(label1)  # label2下降到label1下面

# 2.3 展示控件
window.show()
# 3. 应用程序的执行 进入到消息循环
sys.exit(app.exec_())