
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'table.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import util.DbUtil as db

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_er_boook(object):

    def setupUi(self, er_boook):
        er_boook.setObjectName("er_boook")
        er_boook.resize(1200, 700)  # 宽，高
        er_boook.setMinimumSize(QtCore.QSize(1200, 700))
        er_boook.setMaximumSize(QtCore.QSize(1200, 700))
        # er_boook.move(855, 300) 设置位置
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/img/shuji.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        er_boook.setWindowIcon(icon)
        self.tableView = QtWidgets.QTableView(er_boook)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 1200, 700))
        self.tableView.setMinimumSize(QtCore.QSize(1200, 700))
        self.tableView.setMaximumSize(QtCore.QSize(1200, 700))
        self.tableView.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(50)
        self.tableView.setFont(font)
        self.tableView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tableView.setIconSize(QtCore.QSize(0, 0))
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setSortIndicatorShown(True)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        er_boook.setWindowFlags(QtCore.Qt.Widget)  # 普通显示 不是置顶

        # er_boook.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)#页面最前端 置顶显示

        # self.lad_table()#加载表格数据

        self.retranslateUi(er_boook)
        QtCore.QMetaObject.connectSlotsByName(er_boook)

    def retranslateUi(self, er_boook):
        _translate = QtCore.QCoreApplication.translate
        er_boook.setWindowTitle(_translate("er_boook", "题库"))

    def lad_table(self, bz):  # 加载表格数据
        if bz == 'None' or len(bz) == 0:
            sql='select * from poetry order by author asc;'  # 默认查询全部
        else:
            bz = '%' + bz + '%'  # 加上% 表示模糊搜索
            sql = 'select * from poetry where author like "%s" order by author asc;'%(bz)
        data = db.check(sql)  # 获取二维数组

        self.model = QtGui.QStandardItemModel(1, 4)
        self.model.clear()  # 清除表格内容
        self.model = QtGui.QStandardItemModel(1, 4)  # 设置行列数
        self.model.setHorizontalHeaderLabels(["题目", "作者", "类型", "内容"])  # 表头字段
        self.tableView.setModel(self.model)  # 表格控件关联Model
        self.tableView.setColumnWidth(0, 250)  # 第一个表头宽度
        self.tableView.setColumnWidth(1, 100)  # 第二个表头宽度
        self.tableView.setColumnWidth(2, 100)  # 第三个表头宽度
        self.tableView.setColumnWidth(3, 1400)  # 第四个表头宽度

        # 添加数据
        for i in range(len(data)):
            title = data[i][1].replace('\n', '')  # 将换行符删除
            self.model.setItem(i, 0, QtGui.QStandardItem(title))
            zh = data[i][5].replace('\n', '')  # 将换行符删除
            self.model.setItem(i, 1, QtGui.QStandardItem(data[i][2]))
            self.model.setItem(i, 2, QtGui.QStandardItem(data[i][3]))
            self.model.setItem(i, 3, QtGui.QStandardItem(zh))
