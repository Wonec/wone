# -*- coding: utf-8 -*-
# @Time     : 2021/7/8 17:34
# @Author   : Wone
# @File     : 04-QWidget-父子关系.py
# @Software : PyCharm
from PyQt5.Qt import *
import sys

# 创建一个应用程序对象
app = QApplication(sys.argv)


# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('父子关系的学习')
window.resize(500, 500)

label1 = QLabel(window)
# label1.setParent()
label1.setText('标签1')

label2 = QLabel(window)
# label1.setParent()
label2.setText('标签2')
label2.move(50, 50)

label3 = QLabel(window)
# label1.setParent()
label3.setText('标签3')
label3.move(100, 100)

# print(window.childAt(255, 255))  # 查看这个坐标是否有子控件 没有则打印None
# print(label2.parentWidget())

print(window.childrenRect())  # 获取所有子对象的Rect矩形



# 2.3 展示控件
window.show()
# 3. 应用程序的执行 进入到消息循环
sys.exit(app.exec_())