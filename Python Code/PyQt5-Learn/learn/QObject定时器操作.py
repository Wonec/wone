from PyQt5.Qt import *
import sys


class MyObject(QObject):  # 继承父类 QObject 所有QWidget的基类
    def timerEvent(self, evt):
        print(evt, '1')  # 每次定时器操作打印事件类型 + 1

class MyLabel(QLabel):  # 继承父类QLabel
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 初始化父类方法
        self.setText('10')
        self.move(100, 100)
        self.setStyleSheet("font-size: 22px;")

    def setSec(self, sec):  # 接收传入参数设置标签的文字内容
        self.setText(str(sec))

    def startMytimer(self, ms):  # 设置定时器id ms代表毫秒
        self.timer_id = self.startTimer(ms)

    def timerEvent(self, a0: 'QTimerEvent') -> None:
        print('xx')
        # 1.获取当前标签的内容
        current_sec = int(self.text())  # 获取标签内容 转换成整数类型
        current_sec -= 1  # 每次定时器执行 变量current_sec - 1
        self.setText(str(current_sec))  # 重新设置标签的内容

        if current_sec == 0:  # 当变量current_sec = 0 时结束定时器
            print('停止')
            self.killTimer(self.timer_id)  # 调用killTimer方法结束设置的定时器id timer_id


class MyWidget(QWidget):
    def timerEvent(self, a0: 'QTimerEvent') -> None:
        print('xxx')
        current_w = self.width()  # 获取当前窗口的宽度并赋值给变量 current_w
        current_h = self.height()  # 获取当前窗口的高度并赋值给变量 current_h
        self.resize(current_w + 2, current_h + 2)  # 每10毫秒窗口宽高增加 1像素


# 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = MyWidget()  # 实例化类
# 2.2 设置控件
window.setWindowTitle('QObject定时器的的使用')  # 设置窗口标题
window.resize(500, 500)  # 设置窗口大小

window.startTimer(10)  # 设置定时器事件 10毫秒 每10毫秒进行一次操作

# label = MyLabel(window)
# label.setSec(1000)
# label.startMytimer(100000)


# 2.3 展示控件
window.show()
# 3. 应用程序的执行 进入到消息循环
sys.exit(app.exec_())
