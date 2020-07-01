# 导入操作视频文件的模块
from moviepy.editor import VideoFileClip, concatenate_videoclips


def VideoShift(src, kind):
    """将视频文件转为音频文件,参数一路径，参数二文件格式 mp3 or wav
    mp3是有损格式，wav是无损格式，按需选择可选择"""

    video = VideoFileClip(src) # 读取视频信息
    audio = video.audio  # 提取视频的音频信息
    # 将路径按.分割,生成列表并且把最后一个元素删除(最后一个为文件格式)
    NameList = src.split('.')[:-1]
    name = ''
    for n in NameList:
        name += n
    audio.write_audiofile(name+'.'+kind)  # 音频信息写入文件
    return 1



# 多个视频合成
video1 = VideoFileClip('e:/video/New1.mp4')
video2 = VideoFileClip('e:/video/1.mp4').subclip(123, 195)  # 第一个视频
video3 = VideoFileClip('e:/video/2.mp4').subclip(1, 101)  # 第二个视频的50-60秒
video4 = VideoFileClip('e:/video/3.mp4') .subclip(1, 31)   # 第三个视频
finalclip = concatenate_videoclips([video1, video2,video3, video4])  # 三个视频合在一起
finalclip.write_videofile("New.mp4")  # 新视频写成文件


# 获取视频时长,单位秒
# video = VideoFileClip('e:/video/1.55.mp4')
# time = video.duration

