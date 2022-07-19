from PyQt5.Qt import *
import sys

# 创建一个应用程序对象
app = QApplication(sys.argv)


# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle('最小尺寸最大尺寸的限定')
window.resize(500, 500)

window.setMinimumSize(200, 200)  # 设置最小大小
window.setMaximumSize(600, 600)  # 设置最大大小


# 2.3 展示控件
window.show()
# 3. 应用程序的执行 进入到消息循环
sys.exit(app.exec_())