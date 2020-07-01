
# coding:utf-8

import logging
from os import listdir, path, makedirs
from time import strftime, localtime, time

import util.DbUtil as db

def add(src, beizhu):
    try:
        sql = 'insert into poetry (title, author, kind, intro, content) values ("%s","%s","%s","%s","%s");'
        with open(src, 'r', encoding='utf-8') as f:
            x = f.read()
        All = []
        All = x.split('-')  # 分割后 返回全部的列表
        log('进度', 'info', '%s-文件正在添加' % (beizhu))
        for i in range(0, len(All), 5):
            title = All[i]
            author = All[i + 1]
            kind = All[i + 2]
            intro = All[i + 3]
            content = All[i + 4]
            db.inisert(sql, title, author, kind, intro, content)

        log('进度', 'info', '%s-文件添加完成' % (beizhu))
    except Exception as e:
        log('异常', 'error', '代码出错:%s' % (str(e)))
        log('进度', 'info', '%s-文件添加失败' % (beizhu))


def log(name, kind, message):
    # 第一步，创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Log等级总开关
    # 第二步，创建一个handler，用于写入日志文件
    rq = strftime('%Y%m%d%H%M', localtime(time()))[:-4]
    if not path.exists('log/'):  # 检测文件夹是否存在,否自己创建
        makedirs('log/')
    log_name = 'log/' + rq + name + '.log'  # 输出到指定路径
    logfile = log_name
    fh = logging.FileHandler(logfile, mode='a')  # 追加输出
    fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
    # 第三步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    # 第四步，将logger添加到handler里面
    logger.addHandler(fh)
    if kind == 'warning':
        logger.warning(message)
    elif kind == 'error':
        logger.error(message)
    elif kind == 'info':
        logger.info(message)
    elif kind == 'debug':
        logger.debug(message)
    else:
        logger.critical(message + 'log方法,第二个参数错误')
    # 最后在记录日志之后移除句柄,防止重复录入
    logger.removeHandler(fh)


def start(path):
    try:
        txt_list = []  # 存放txt文件名称
        j = 1
        filename_list = listdir(path)  # 获取文件夹下的文件
        for i in filename_list:  # 遍历文件名
            if i.endswith('.txt'):  # 判断是否以指定字符串结尾
                txt_list.append(i)  # 添加txt列表
        if len(txt_list) == 0 or len(filename_list) == 0:
            log('进度', 'info', "'%s'目录下,无可添加的txt文件"%(path))
            log('进度', 'info', "---------------------------------------------------------")
        elif len(txt_list) != 0:
            for k in txt_list:
                info = '共有%d个文件第,正在录入第%d个文件' % (len(txt_list), j)
                log('进度', 'info', info)
                a = k.index(".")  # 获取.的位置
                beizhu = k[0:a]  # 获取名字不带txt格式
                src = path + k
                add(src, beizhu)
                j += 1
            log('进度', 'info', "全部文件录入完成")
            log('进度', 'info', "---------------------------------------------------------")
    except Exception as e:
        log('异常', 'error', '代码出错:%s' % (str(e)))


if __name__ == '__main__':
    pass
    #add('add/诗词A.txt','A')
