
from sys import exit, argv
from PyQt5.QtWidgets import QApplication

from view.main import Main

app = QApplication(argv)
Main = Main()  # 实例化类
Main.show()
# 类似于一个循环让窗口不一闪而过
exit(app.exec_())

