import sys
from PyQt5.QtWidgets import QApplication,QWidget
if __name__ == '__main__':
    app=QApplication(sys.argv)
    #创建一个窗口
    w=QWidget()
    w.resize(300,150)
    #移动窗口
    w.move(300,300)

    w.setWindowTitle("第一个基于pyqt5的桌面应用")


    w.show()

    sys.exit(app.exec_())