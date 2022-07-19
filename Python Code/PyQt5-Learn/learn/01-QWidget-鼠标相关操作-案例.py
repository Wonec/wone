import sys
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()  # 初始化父类的方法
        '''初始化中设置基本窗口参数 标题 大小 位置 '''
        self.setWindowTitle('鼠标相关操作案例')
        self.resize(500, 500)
        self.move(200, 200)
        self.setMouseTracking(True)  # 调用方法鼠标跟踪为 True 不摁下鼠标按键也可以执行监听鼠标

        pixmap = QPixmap(r"C:\Users\wone\Desktop\PythonCode\Practice\SchoolNetLoginGui\kela.ico")  # QPixmap接收图片 赋值给变量pixmap
        cursor = QCursor(pixmap)  # QCursor设置鼠标图片pixmap 赋值给cursor
        self.setCursor(cursor)  # 设置鼠标图片

        label = QLabel(self)   # 创建一个QLabel对象 父类为self 也就是当前的QWidget
        self.label = label  # 创建一个全局变量接收label对象
        label.setText('WONE')  # 设置标签内容
        label.move(100, 100)  # 移动标签位置
        label.setStyleSheet('background-color: cyan;')  # setStyleSheet  qss设置标签背景颜色

    def mouseMoveEvent(self, mv):  # 对父类中的mouseMoveEvent方法重写
        print('鼠标移动', mv.localPos())
        # label = self.findChild(QLabel)
        self.label.move(mv.localPos().x(), mv.localPos().y())  # 标签调用move方法传入鼠标局部位置参数(窗口内的位置)

app = QApplication(sys.argv)

window = Window()
# window.setWindowTitle('鼠标相关操作案例')
# window.resize(500, 500)
# window.move(200, 200)
# window.setMouseTracking(True)
#
# pixmap = QPixmap(r"C:\Users\wone\Desktop\PythonCode\Practice\SchoolNetLoginGui\kela.ico")
# cursor = QCursor(pixmap)
# window.setCursor(cursor)
#
#
# label = QLabel(window)
# label.setText('WONE')
# label.move(100, 100)
# label.setStyleSheet('background-color: cyan;')

window.show()
sys.exit(app.exec_())