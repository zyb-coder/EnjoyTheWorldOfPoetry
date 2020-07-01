# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'word_train.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from random import shuffle  # 打乱列表
import xml.dom.minidom as xl  # 导入操作xml文件的包
from PyQt5 import QtCore, QtGui, QtWidgets  # QtCore窗口样式 QtWidgets消息提示窗口

from dao.WordTrain import Train  # 导入单词训练模块


class Ui_view_WordTrain(object):
    def __init__(self):  # 初始化函数
        self.bz = 'None'  # 默认单元备注为None

        self.dom = xl.parse(r'data/config.xml')  # 加载读取xml文件
        rootData = self.dom.documentElement  # 获取xml文档对象
        self.color = rootData.getElementsByTagName('color')  # 查找所有color标签
        cStr = self.color[0].firstChild.data  # 获取第一个标签为color的它的第一个孩子的信息
        listStr = cStr.split(",")  # 将字符串按","号分割 返回列表
        self.listInt = list(map(int, listStr))  # 将int方法作用到x列表的每个元素上 返回新列表

        # self.c 为rgb列表索引值
        self.colorCount = rootData.getElementsByTagName('login')  # 查找所有login标签
        self.c = int(self.colorCount[0].getAttribute('count'))  # 获取第一个标签为login的它的count属性的值

    def setupUi(self, view_WordTrain):
        view_WordTrain.setObjectName("view_WordTrain")
        view_WordTrain.resize(590, 320)
        view_WordTrain.setMinimumSize(QtCore.QSize(590, 320))
        view_WordTrain.setMaximumSize(QtCore.QSize(590, 320))
        view_WordTrain.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/img/lianxi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        view_WordTrain.setWindowIcon(icon)

        view_WordTrain.move(700,50)  # 设置窗口在屏幕的位置 855, 300
        view_WordTrain.setWindowFlags(QtCore.Qt.Widget)  # 普通显示 不是置顶

        # 在最前端显示和取消边框
        # view_WordTrain.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)

        # rgb 默认 144,238,144
        view_WordTrain.setStyleSheet("background-color: rgb(%d,%d,%d);"
                                     % (self.listInt[0], self.listInt[1], self.listInt[2]))
        self.text_logo = QtWidgets.QLabel(view_WordTrain)
        self.text_logo.setGeometry(QtCore.QRect(25, 48, 31, 31))
        self.text_logo.setText("")
        self.text_logo.setPixmap(QtGui.QPixmap("data/img/en.png"))
        self.text_logo.setScaledContents(True)
        self.text_logo.setObjectName("text_logo")
        self.text_english = QtWidgets.QLabel(view_WordTrain)
        self.text_english.setGeometry(QtCore.QRect(60, 40, 521, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(85)
        self.text_english.setFont(font)
        self.text_english.setObjectName("text_english")

        self.but_a = QtWidgets.QRadioButton(view_WordTrain)
        self.but_a.setGeometry(QtCore.QRect(80, 120, 271, 40))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        self.but_a.setFont(font)
        self.but_a.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.but_a.setObjectName("but_a")
        self.but_b = QtWidgets.QRadioButton(view_WordTrain)
        self.but_b.setGeometry(QtCore.QRect(360, 120, 221, 40))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        self.but_b.setFont(font)
        self.but_b.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.but_b.setObjectName("but_b")
        self.but_c = QtWidgets.QRadioButton(view_WordTrain)
        self.but_c.setGeometry(QtCore.QRect(80, 190, 271, 40))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        self.but_c.setFont(font)
        self.but_c.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.but_c.setObjectName("but_c")
        self.but_d = QtWidgets.QRadioButton(view_WordTrain)
        self.but_d.setGeometry(QtCore.QRect(360, 190, 221, 40))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        self.but_d.setFont(font)
        self.but_d.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.but_d.setObjectName("but_d")
        self.but_go = QtWidgets.QPushButton(view_WordTrain)
        self.but_go.setGeometry(QtCore.QRect(400, 80, 75, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.but_go.setFont(font)
        self.but_go.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.but_go.setObjectName("but_go")
        self.but_tuichu = QtWidgets.QPushButton(view_WordTrain)
        self.but_tuichu.setGeometry(QtCore.QRect(500, 80, 75, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.but_tuichu.setFont(font)
        self.but_tuichu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.daan_text = QtWidgets.QTextBrowser(view_WordTrain)
        self.daan_text.setGeometry(QtCore.QRect(10, 240, 440, 70))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.daan_text.setVisible(False)  # 多文本行设置隐形不可见
        self.daan_text.setFont(font)
        self.daan_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.daan_text.setStyleSheet("color: rgb(239, 0, 0);")
        self.daan_text.setPlaceholderText("")
        self.daan_text.setObjectName("daan_text")

        self.but_tuichu.setObjectName("but_tuichu")
        self.but_bx = QtWidgets.QRadioButton(view_WordTrain)
        self.but_bx.setGeometry(QtCore.QRect(500, 70, 31, 16))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.but_bx.setFont(font)
        self.but_bx.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.but_bx.setText("bx")
        self.but_bx.setObjectName("but_bx")  # 备选按钮，隐藏在下一页的下面

        self.but_cz = QtWidgets.QPushButton(view_WordTrain)
        self.but_cz.setGeometry(QtCore.QRect(330, 85, 50, 30))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.but_cz.setFont(font)
        self.but_cz.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.but_cz.setObjectName("but_cz")

        self.label = QtWidgets.QLabel(view_WordTrain)
        self.label.setGeometry(QtCore.QRect(470, 240, 111, 71))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label.raise_()
        self.but_cz.raise_()
        self.but_bx.raise_()
        self.but_go.raise_()
        self.text_logo.raise_()
        self.text_english.raise_()
        self.but_a.raise_()
        self.but_b.raise_()
        self.but_c.raise_()
        self.but_d.raise_()
        self.but_tuichu.raise_()
        self.daan_text.raise_()

        self.retranslateUi(view_WordTrain)

        # ！！！子页面调用函数方法时需要用lambda关键字 否则没有作用
        # self.load_data()#打开这个页面的时候就加载答题卡信息

        # 换肤按钮
        self.but_cz.clicked.connect(lambda: self.range(view_WordTrain))
        # 下一页按钮 刷新数据
        self.but_go.clicked.connect(lambda: self.load_data(self.bz))
        # 重置按钮
        self.but_tuichu.clicked.connect(lambda: self.clear())
        # 设置单选按钮事件 传入参数
        self.but_a.toggled.connect(lambda: self.decide_daan(self.but_a))
        self.but_b.toggled.connect(lambda: self.decide_daan(self.but_b))
        self.but_c.toggled.connect(lambda: self.decide_daan(self.but_c))
        self.but_d.toggled.connect(lambda: self.decide_daan(self.but_d))
        #self.but_bx.toggled.connect(lambda: self.decide_daan(self.but_bx))

        QtCore.QMetaObject.connectSlotsByName(view_WordTrain)

    def retranslateUi(self, view_WordTrain):
        _translate = QtCore.QCoreApplication.translate
        view_WordTrain.setWindowTitle(_translate("view_WordTrain", "诗词训练"))
        self.text_english.setText(_translate("view_WordTrain", "加载..."))
        self.but_a.setText(_translate("view_WordTrain", '加载...'))
        self.but_b.setText(_translate("view_WordTrain", "加载..."))
        self.but_c.setText(_translate("view_WordTrain", "加载..."))
        self.but_d.setText(_translate("view_WordTrain", "加载..."))
        self.but_go.setText(_translate("view_WordTrain", "下一页"))
        self.but_cz.setText(_translate("view_WordTrain", "换 肤"))
        self.but_tuichu.setText(_translate("view_WordTrain", "清除记录"))

    def load_data(self, bz):  # 下一页 加载答题卡信息
        self.but_bx.setChecked(True)  # 清空选项按钮选中状态 隐藏按钮选中
        self.bz = bz  # 将当前的单元信息传递给给这个类
        tr = Train()
        self.id, self.title, self.ju, self.xx, self.count = tr.ran_word(bz)
        # 如果返回值为int类型则信息获取失败
        if type(self.xx) == int:
            self.call("资源加载失败")  # 弹出提示框
        elif self.xx == 'ok':
            self.call("已做完全部词汇")  # 弹出提示框
        else:
            strCount = "剩余"+str(self.count)+"个"
            self.label.setText(strCount)
            self.daan_text.setVisible(False)  # 多文本行设置隐形不可见
            self.daan_text.clear()  # 清空答案显示区
            self.xx.append(self.ju)  # 将正确答案也放入其中
            shuffle(self.xx)  # 打乱列表顺序
            self.text_english.setText(self.title)
            self.but_a.setText(self.xx[0])
            self.but_b.setText(self.xx[1])
            self.but_c.setText(self.xx[2])
            self.but_d.setText(self.xx[3])


    def addid(self):
        with open('data/id.txt', 'a') as f:  # 在文件中添加这个id记录
            f.write(str(self.id) + '\n')

    def decide_daan(self, btn):  # 判断选择是否正确
        # 获取当前单选按钮的值并判断是否为正确答案 是否为选中状态
        if btn.text() == self.ju:  # 判断按钮文本
            if btn.isChecked() == True:  # 判断按钮是否为选中状态
                self.daan_text.setVisible(True)  # 多文本行可见
                self.daan_text.setPlainText('正确')
                self.addid()  # 写入本地记录
        elif btn.text() == "bx":  # 备选按钮被选中清空显示区
            pass

        else:
            self.daan_text.setVisible(True)  # 多文本行可见
            self.daan_text.setPlainText('答案为：'+self.ju)

    def clear(self):
        with open('data/id.txt', 'w') as f:
            f.write('')  # 清空txt文件
        self.call('清空成功')

    def call(self, str):  # 提示框
        # No 按钮返回16384
        s = QtWidgets.QMessageBox.information(None, '消息', str
                                              , QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.Yes)

    def range(self, view_WordTrain):  # 换肤功能

        # 定义rgb颜色值列表
        i = [[144, 238, 144], [173, 216, 230], [205, 0, 0], [100, 149, 237], [205, 205, 193],
             [171, 130, 255], [60, 179, 113], [69, 139, 0], [139, 0, 139], [255, 255, 255]]

        self.c += 1  # 索引值加一
        if self.c == len(i):
            self.c = 0  # 遍历完列表 索引值变为0

        # 修改单词训练界面颜色
        view_WordTrain.setStyleSheet("background-color: rgb(%d, %d, %d);"
                                     % (i[self.c][0], i[self.c][1], i[self.c][2]))

        col = ''
        strList = map(str, i[self.c])  # 将元素整型换成字符串
        for s in strList:
            col += s + ','  # 将列表中所有字符串连接起来
        col = col[:-1]  # 去除最后一个逗号

        # 修改xml文件属性
        self.colorCount[0].setAttribute('count', str(self.c))  # 修改第一login标签的count属性对应的值
        self.color[0].firstChild.data = col  # 第一个标签为color的它的第一个孩子的信息

        # 保存修改xml文件
        with open(r'data/config.xml', 'w', encoding='UTF-8') as fh:
            self.dom.writexml(fh, encoding='UTF-8')


