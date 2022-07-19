# -*- coding: utf-8 -*-
# @Time     : 2021/7/8 17:41
# @Author   : Wone
# @File     : 04-QWidget-父子关系案例.py
# @Software : PyCharm

from PyQt5.Qt import *
import sys

# class Label(QLabel):
#     def mousePressEvent(self, ev: QMouseEvent) -> None:
#         self.setStyleSheet('background-color: red;')

class Window(QWidget):
    def mousePressEvent(self, evt) -> None:
        local_x = evt.x()  # 获取事件对象当前的x轴(点击位置的x轴)
        local_y = evt.y()  # 获取事件对象当前的y轴(点击位置的y轴)
        sub_widget = self.childAt(local_x, local_y)  # 找到Window位于local_x, local_y位置的的子控件赋值给变量sub_widget
        if sub_widget != None:  # 判断控件是否为空
            sub_widget.setStyleSheet('background-color: red;')  # 设置子控件的背景颜色
        print('被点击了', local_x, local_y)

# 创建一个应用程序对象
app = QApplication(sys.argv)


# 2. 控件的操作
# 2.1 创建控件
window = Window()
# 2.2 设置控件
window.setWindowTitle('父子关系案例')
window.resize(500, 500)

for i in range(1, 11):  # for循环生成10个标签
    label = QLabel(window)
    label.setText("标签" + str(i))
    label.move(40 * i, 40 * i)





# 2.3 展示控件
window.show()
# 3. 应用程序的执行 进入到消息循环
sys.exit(app.exec_())
