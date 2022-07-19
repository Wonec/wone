from PyQt5.Qt import *
import sys

# 创建一个应用程序对象
app = QApplication(sys.argv)


# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.resize(500, 500)
window.move(300, 300)
# 控件个数
widget_count = 100
# 列数
column_count = 10
# 行数 = (控件个数-1) // 列数 + 1
row_count = (widget_count - 1) // column_count + 1

# 控件的宽度 = 窗口宽度 / 列数
widget_width = window.width() / column_count
# 控件高度 = 窗口高度 / 行数
widget_height = window.height() / row_count

for i in range(0, widget_count):  # for循环来创建控件对象
    w = QWidget(window)  # 实例化QWidget对象 在window上显示
    w.resize(widget_width, widget_height)  # 设置控件宽高
    w.setStyleSheet('background-color: red;border: 1px solid yellow')  # setStyleSheet设置背景颜色为红色边框为黄色 1像素
    '''
    widget_x = 当前编号(0-widget_count) 对列数进行求模 0 % 10 = 0, 1 % 10 = 1 ... 10 % 10 = 0, 11 % 10 = 1 
    再乘以控件宽度 0 * 控件宽度 = 0, 1 * 控件宽度 = 控件宽度
    widget_y = 当前编号(0-widget_count)整除列数 0-9 整除 10 = 0, 10-19 整除 10 = 1
    再乘以控件高度
    每一行控件的x不同y相同 
    '''
    widget_x = i % column_count * widget_width  # 控件x坐标 = 当前编号 % 列数 * 控件宽度
    widget_y = i // column_count * widget_height  # 控件y坐标 = 当前编号 // 控件个数 * 控件高度
    print(f'x={widget_x}, y={widget_y}')
    w.move(widget_x, widget_y)  # 控件移动到计算出来的 widget_x, widget_y处
    w.show()

# 2.3 展示控件
window.show()
# 3. 应用程序的执行 进入到消息循环
sys.exit(app.exec_())