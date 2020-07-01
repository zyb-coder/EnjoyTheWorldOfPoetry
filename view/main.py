from sys import exit
from os import system
from pygame import font, init, mixer  # 用于打开游戏界面和播放音频文件
from threading import Thread  # 导入线程函数
import xml.dom.minidom as xl  # 导入操作xml文件的包
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog

import dao.game as ga  # 游戏模块
import util.DbUtil as db  # 对数据库的操作
import dao.inputWord as iw  # 录入单词模块
from dao.void import Video  # 视频播放模块
from view.table import Ui_er_boook  # 表格界面
from view.main_window import Ui_MainWindow  # 主界面
from view.word_train import Ui_view_WordTrain  # 答题卡界面


class Main(Video, QMainWindow, Ui_MainWindow):
    def __init__(self):  # 初始化类
        super(Main, self).__init__()
        # 首先找到 Main 的父类 再把父类Ui_MainWindow和父类类QMainWindow的对象转换为类Main的对象
        # 转换成  类Main 对象后在调用自己的初始化函数__init__()
        self.setupUi(self)
        # 定义点击按钮次数,奇数打开界面,偶数关闭界面
        self.c = 1  # 翻译界面点击次数
        self.g = 1  # 游戏界面点击次数

        self.dom = xl.parse(r'data/config.xml')  # 加载读取xml文件
        rootData = self.dom.documentElement  # 获取xml文档对象
        self.VideoState = rootData.getElementsByTagName('VideoState')  # 查找所有这个标签
        state = self.VideoState[0].firstChild.data  # 获取第一个这个标签为的它的第一个孩子的信息
        # 判断教学视频开关
        self.state = state == str(True)
        self.VideoWay = rootData.getElementsByTagName('VideoWay')
        state = self.VideoWay[0].firstChild.data
        # 判断视频播放方式 False自带 True本地
        self.way = state == str(True)

        # 开场视频
        self.Velocity = rootData.getElementsByTagName('Velocity')
        V = self.Velocity[0].firstChild.data  # 速度
        src4 = 'data/video/start.mp4'
        src3 = 'data/video/start.mp3'
        self.IdenVideo(src4, src3, 790, 495, 690, 150, 1,V)
        # 大窗口视频参数790, 495, 690, 150
        # 小窗口高视频参616, 438, 855, 200
        # 小窗口视频参数616, 337, 855, 300
        # 左窗口视频参数550, 490, 140, 150
        # 左2窗口视频参数600, 440, 80, 170

        try:
            self.authorAll = self.Cauthor()  # 查询全部作者
            self.out_text.setPlainText(self.authorAll)  # 应用到输出界面
        except:
            self.tishi('缺少db文件')

        self.view_fan.hide()  # 因翻译界面和主界面是一个窗体,所以先将翻译界面隐藏起来

        # 设置按钮事件  connect调用函数功能时需用 lambda定义(匿名函数)或者调用函数是不加()

        # 视频说明
        self.user_set.triggered.connect(self.shuoming)
        # 视频操作-开
        self.user_add.triggered.connect(self.VoideON)
        # 视频操作-关
        self.user_acc.triggered.connect(self.VoideOFF)
        # 软件说明
        self.user_out.triggered.connect(self.ruanjian)
        # 软件播放
        self.help_about_help.triggered.connect(self.MyPlay)
        # 本地播放
        self.help_about_check.triggered.connect(self.HerPlay)
        # 有查看按钮
        self.butt_fanyi.clicked.connect(self.but_fanyi)
        # 清除的按钮
        self.butt_return.clicked.connect(self.cl)
        # 查看的按钮
        self.butt_range.clicked.connect(self.but_range)
        # 单词训练按钮
        self.butt_wordTrain.clicked.connect(self.but_word_train)
        # 查看词汇按钮
        self.butt_words.clicked.connect(self.add_word)
        # 查看错题本按钮
        # table = self.opten_table()
        self.butt_erbook.clicked.connect(self.opten_table)
        # 娱乐休闲按钮
        self.butt_test.clicked.connect(self.open_game)
        # 官网按钮事件 调用yd模块中的open_html()函数
        self.butt_guanWang.clicked.connect(self.open_html)

    # mp4路径,mp3路径,长宽,屏幕位置,是否全屏,可选参数音量
    def IdenVideo(self, src4, src3, wide, high, X, Y, K,V):
        if self.state:  # 判断是状态否打开
            if not self.way:  # 判断播放方式
                try:  # 防止第一次未定义报错
                    # 判断是否有别的视频在播放
                    if self.video.isAlive():
                        # 停止播放视频
                        self.StopVideo()
                except:
                    pass
                # 再开启新线程
                self.video = Thread(target=self.PlayVideo,
                                    args=(src4, src3, wide, high, X, Y,K,int(V)))
                self.video.start()
            else:
                # 默认程序打开视频  路径为反斜杠
                src = src4.replace('/', '\\')
                system("start explorer %s"%(src))

    def VoideON(self):  # 教学视频打开
        self.state = True
        self.SaveXlm(self.VideoState, 'True')

    def VoideOFF(self):  # 教学视频关闭
        self.state = False
        self.SaveXlm(self.VideoState, 'Flase')

    def MyPlay(self):  # 软件播放
        self.way = False
        self.SaveXlm(self.VideoWay, 'Flase')

    def HerPlay(self):  # 本地播放
        self.way = True
        self.SaveXlm(self.VideoWay,'True')

    def SaveXlm(self, obj, bol):
        obj[0].firstChild.data = bol
        # 保存修改xml文件
        with open(r'data/config.xml', 'w', encoding='UTF-8') as fh:
            self.dom.writexml(fh, encoding='UTF-8')

    def but_fanyi(self):  # 显示注释界面
        if self.c % 2 != 0:
            self.c += 1  # 次数自增1
            self.view_fan.show()  # 显示界面
            src4 = 'data/video/g1.mp4'
            src3 = 'data/video/Gmusic.mp3'  # 不播放音乐
            self.IdenVideo(src4, src3, 600, 440, 80, 170,0,24)
        else:
            self.view_fan.hide()  # 隐藏界面
            self.c += 1

    def shuoming(self):  # 不能放到初始化里,以免报错
        self.tishi('按‘Q’键关闭全屏播放\n尽量不要移动视频窗口\n可能造成音频不同步\n建议减小音量!!!')

    def ruanjian(self):
        self.tishi('可更改的选项和练习记录都将记录在配置文件中,再次启动不会被初始化')

    def cl(self):  # 重置界面
        self.input_text.clear()
        self.lien_bz.setText("None")
        self.out_text.setPlainText(self.authorAll)

    def but_range(self):  # 优先对诗名搜索,其次是诗人
        try:
            str = self.input_text.toPlainText()  # 获取多文本行中的内容
            # 判断输入的是否为空或者全是空格,防止程序崩溃
            if len(str) != 0 | str.isspace() == False:
                title = '"%' + str + '%"'
                sql = 'select title,author,content,intro from poetry where title like %s' % (title);
            else:
                str = self.lien_bz.text()  # 获取文本框信息
                author = '"%' + str + '%"'
                sql = 'select title,author,content,intro from poetry where author like %s' % (author);
            shiList = list(db.check(sql))
            if len(shiList) == 0:
                self.tishi("搜索不到相关的诗词")
            else:
                #  把所有相关的诗词都搜索出来
                shiciAll = '共有%d首诗词\n' % (len(shiList))
                introAll = '以下是诗词注释\n'
                for i in range(len(shiList)):  # 把所有相关的都搜索出来
                    titleStr = '\n' + '****' + shiList[i][0] + '****'
                    authorStr = '\n' + '---' + shiList[i][1] + '---' + '\n'
                    content = shiList[i][2].replace('，', '\n') + '\n'
                    # 所有的题目和诗词
                    shiciAll += '--------------------' + titleStr + authorStr + content
                    # 所有题目注释
                    introAll += titleStr + shiList[i][3] + '\n' + '-------------------------------' + '\n'

                self.input_text.setPlainText(shiciAll)
                self.out_text.setPlainText(introAll)
        except:
            self.tishi("搜索失败")

    def but_word_train(self):  # 打开单词训练窗口
        self.MainW = QMainWindow()
        ui = Ui_view_WordTrain()  # 将包中的子页面类实例化
        beizhu = self.lien_bz.text()  # 获取备注信息
        ui.setupUi(self.MainW)  # 初始化页面将信号与槽建立起来
        ui.load_data(beizhu)  # 加载答题卡信息
        self.MainW.show()  # 让窗口显示出来
        src4 = 'data/video/g2.mp4'
        src3 = 'data/video/Gmusic.mp3'
        self.IdenVideo(src4, src3, 600, 440, 80, 170, 0,24)

    def Cauthor(self):  # 查询所有作者
        sql = 'select author from poetry;'
        # 先变成几何去除重复元素,在变成列表
        authorList = list(set(db.check(sql)))
        authorStr = ''  # 盛放所有作者的字符串
        for i in authorList:
            authorStr += i[0] + '\n'
        authorStr = '*******共有%d位诗人*******\n' % (len(authorList)) + authorStr
        return authorStr

    def add_word(self):  # 将txt中的单词添加到数据库中
        try:
            self.tishi("进度和异常情况,"
                       "\n请在log文件夹下查看日志")
            src4 = 'data/video/g3.mp4'
            src3 = 'data/video/Gmusic.mp3'
            self.IdenVideo(src4, src3, 600, 440, 80, 170, 0,24)
            # 获取文件夹路径
            filsrc = QFileDialog.getExistingDirectory(self, "请选择文件夹路径", "c:")
            if len(filsrc) == 0:
                self.tishi("取消添加")
            else:
                src = filsrc + '/'
                # 定义线程aW，线程任务为调用iw.start函数,iw.start函数的参数是路径args类型为元组 一个参数也要有逗号
                addWord = Thread(target=iw.start, args=(src,))
                addWord.start()  # 开始执行这个线程
                if not addWord.isAlive():  # 返回线程是否活动的。
                    self.tishi("子线程出错")
        except:
            self.tishi("添加失败")

    def opten_table(self):  # 打开单词库
        try:
            self.table = QMainWindow()
            ui = Ui_er_boook()  # 将包中的子页面类实例化
            ui.setupUi(self.table)  # 初始化页面将信号与槽建立起来
            beizhu = self.lien_bz.text()  # 获取备注信息
            ui.lad_table(beizhu)  # 加载table信息
            self.table.show()  # 让窗口显示出来
        except:
            self.tishi('系统文件丢失')

    def tishi(self, str):  # 提示框
        reply = QMessageBox.question(self, '提示', str,
                                     QMessageBox.Yes, QMessageBox.Yes)

    def open_game(self):
        if self.g % 2 != 0:
            self.tishi('再次点击即可关闭音乐和游戏')
            self.g += 1  # 次数自增1
            # 使用pyame模块 播放音乐
            mixer.init()  # 模块初始化
            mixer.music.load('data/video/GameMusic.mp3')  # 加载音乐
            mixer.music.set_volume(0.3)  # 音量设置
            mixer.music.play()  # 播放音乐
            init()  # 打开游戏窗口
            font.init()
            catchball = ga.Main1(600, 500)  # 参数为窗口的大小
        else:
            self.g += 1
            mixer.music.stop()  # 关闭音乐
            init()  # 初始化游戏
            font.init()
            # 设置窗口大小为1
            catchball = ga.Main1(1, 1)

    def open_html(self):
        # 调用系统默认程序,打开指定文件
        system("start explorer data\html\index.html")

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        有些子进程不会彻底关闭,将其重写
        :param event: close()触发的事件
        :return: None
        """
        try:
            src4 = 'data/video/end.mp4'
            src3 = 'data/video/end.mp3'
            self.IdenVideo(src4, src3, 790, 495, 690, 150, 2,29)
        # 防止子线程没有开启并发生报错
            if self.video.isAlive():
                # 停止播放视频
                self.StopVideo()
                event.accept()
                exit(0)  # 关闭所有进程
            event.accept()
            exit(0)  # 没有视频播放,直接关闭
        except:
            event.accept()
            exit(0)  # 关闭所有进程