from PyQt5.Qt import *
import sys

# 创建一个应用程序对象
app = QApplication(sys.argv)


# 2. 控件的操作
# 2.1 创建控件
window = QWidget()  # 实例化一个QWidget对象 赋值给变量window
# 2.2 设置控件
window.setWindowTitle('内容边距的设定')  # 设置标题
window.resize(500, 500)  # 设置大小

label = QLabel(window)  # 实例化一个QLabel对象 父类为window也就是在window上显示
label.setText('Wone-988321')  # 设置标签文本
label.resize(300, 300)  # 设置标签大小
label.setStyleSheet("background-color: cyan;")  # 设置标签的背景颜色 调用SetStyleSheet方法qss

label.setContentsMargins(0, 0, 0, 0)  # 左上右下 设置标签中内容的边距

print(label.contentsRect())  # 打印标签的Rect位置参数(x, y, width, height)



# 2.3 展示控件
window.show()
# 3. 应用程序的执行 进入到消息循环
sys.exit(app.exec_())