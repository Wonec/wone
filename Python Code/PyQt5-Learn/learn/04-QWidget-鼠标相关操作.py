from PyQt5.Qt import *
import sys


class MyWindow(QWidget):
    def mouseMoveEvent(self, me):  # 重写父类中mouseMoveEvent方法
        print("鼠标移动了", me.localPos())  # localPos 鼠标移动事件中的局部位置参数

# 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = MyWindow()
# 2.2 设置控件
window.setWindowTitle('鼠标操作')
window.resize(500, 500)

window.setMouseTracking(True)  # 鼠标追踪设置为True 不用按下按键也可以进行鼠标事件监听
print(window.hasMouseTracking())


# pixmap = QPixmap(r"C:\Users\wone\Documents\Tencent Files\2860874824\Image\C2C\346E2058F85C23C25989900D78B8FC63.gif")
# new_pixmap = pixmap.scaled(80, 80)
# cursor = QCursor(new_pixmap, 4, 53)
# window.setCursor(cursor)

# window.unsetCursor()  # 重置鼠标图标
# current_cursor = window.cursor()
# current_cursor.setPos(0, 0)

# label = QLabel(window)
# label.setText('WONE')
# label.resize(100, 100)
# label.setStyleSheet('background-color: cyan;')

# label.setCursor(Qt.CrossCursor)

# 2.3 展示控件
window.show()
# 3. 应用程序的执行 进入到消息循环
sys.exit(app.exec_())
