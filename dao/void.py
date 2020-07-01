from cv2 import destroyAllWindows, VideoCapture, resize,imshow, moveWindow,waitKey, getWindowProperty, \
    WND_PROP_AUTOSIZE,WND_PROP_FULLSCREEN,WINDOW_FULLSCREEN,setWindowProperty,namedWindow,WINDOW_NORMAL,\
    CAP_PROP_FOURCC,VideoWriter_fourcc
from pygame import mixer
from time import sleep

class Video():

    def StopVideo(self):
        # 释放内存,销毁窗口,停止音乐
        self.cap.release()
        destroyAllWindows()
        mixer.music.stop()


    def PlayVideo(self, Vsrc, Asrc, wide, high, X, Y, K,V):
        # mp4路径,mp3路径,长宽,屏幕位置,是否全屏
        # 获得读取视频,获得视频的格式
        self.cap = VideoCapture(Vsrc)
        # 转换格式减少延迟
        self.cap.set(CAP_PROP_FOURCC, VideoWriter_fourcc('M', 'J', 'P', 'G'))
        success, frame = self.cap.read()
        # 模块初始化
        mixer.init()
        # 加载音乐
        mixer.music.load(Asrc)
        if K == 1:  # 是否全屏播放, 跳帧播放
            namedWindow('Teaching', WINDOW_NORMAL)
            # 去除边框
            setWindowProperty('Teaching', WND_PROP_FULLSCREEN, WINDOW_FULLSCREEN)
            mixer.music.play()
            while success:
                imshow('Teaching', frame)
                waitKey(V)  # 45
                # 隔帧读取
                success, frame = self.cap.read()
                success, frame = self.cap.read()
                # 获取窗口属性 没有数据显示返回-1 有数据显示返回1
                if waitKey(1) == ord('q'):
                    break  # 结束循环(实现了按q键,关闭播放 退出界面的功能)
            sleep(2)
        elif K == 2:
            namedWindow('Teaching', WINDOW_NORMAL)
            setWindowProperty('Teaching', WND_PROP_FULLSCREEN, WINDOW_FULLSCREEN)
            mixer.music.play()
            while success:
                imshow('Teaching', frame)
                waitKey(V)  # 29
                success, frame = self.cap.read()
                if waitKey(1) == ord('q'):
                    break
        else:
            i = 1
            mixer.music.play()
            while success:
                # 视频数据(矩阵),窗口宽,高
                frame = resize(frame, (wide, high))
                imshow('Teaching', frame)
                if i == 1:
                    # 设置窗口初始位置
                    moveWindow('Teaching', X, Y)
                    i = 2  # 位置不在固定
                # 延迟  最佳延迟830/fps
                waitKey(V)  # 24
                # 获取下一帧
                success, frame = self.cap.read()
                # 获取窗口属性 没有数据显示返回-1 有数据显示返回1
                if getWindowProperty('Teaching', WND_PROP_AUTOSIZE) == -1:
                    break  # 跳出循环结束播放
        try:
            # 释放内存
            self.cap.release()
            # 销毁窗口
            destroyAllWindows()
            # 结束音乐
            mixer.music.stop()
        except:
            self.cap.release()
            destroyAllWindows()