# -*- coding: utf-8 -*-
# @Time     : 2021/7/9 20:30
# @Author   : Wone
# @File     : 04-QWidget-交互状态.py
# @Software : PyCharm
from PyQt5.Qt import *
import sys

# 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('交互状态')
window.resize(500, 500)

btn = QPushButton(window)
btn.setText('按钮')
btn.pressed.connect(lambda: print('按钮被点击了'))
btn.setEnabled(False)
print(btn.isEnabled())

# 2.3 展示控件
window.show()
# 3. 应用程序的执行 进入到消息循环
sys.exit(app.exec_())
