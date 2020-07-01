
from re import split
from random import choice

import util.DbUtil as db


class Train:
    '''完成单词训练的方法'''

    def read_file(self):  # 读取文件
        idlist = []
        with open('data/id.txt', 'r') as f:
            idtxt = f.readlines()  # 一行为单位读取所有内容
        for i in range(len(idtxt)):  # 删除换行符
            id = idtxt[i].replace('\n', '')
            idlist.append(int(id))
        return idlist

    def charPart(self, ty):  # 拆分元组,随机抽取一句诗
        con1 = ty[5].replace('\r\n', '')  # 抽取题目后删除换行符
        con2 = split('[，。]', con1)  # 将每一句分隔开
        con2.pop()  # 删除最后一个元素
        contentEnd = choice(con2)  # 随机抽取一句诗句
        return contentEnd  # 返回一句诗

    def ran_word(self, bz):  # 随机抽取一个单词和翻译不重复
        try:
            idtxt = self.read_file()  # 获取文件中id的列表
            if bz == 'None' or len(bz) == 0:
                sql = 'select * from poetry;'  # 默认查询全部
            else:
                bz = '%' + bz + '%'  # 加上% 表示模糊搜索
                sql = 'select * from poetry where author like "%s";' % (bz)  # 模糊搜索

            All = db.check('select * from poetry;')
            AllList = []
            for i in range(len(All)):
                AllList.append(All[i][0])  # 提取所有的id

            tup = db.check(sql)  # 获取所有数据的大元组
            idmysql = []  # 存放数据库id的列表
            for i in range(len(tup)):
                idmysql.append(tup[i][0])  # 提取所有的id

            # 取差集 idmysql中有而idtxt中没有的
            idlist = list(set(idmysql).difference(set(idtxt)))  # 未学习过的id

            if len(idlist) != 0:  # 判断词汇是否都学完
                count = len(idlist) - 1  # 返回未训练单词的个数
                id = choice(idlist)  # 随机抽取一个id
                idlist.remove(id)  # 在差集列表中删除这个id
                idmysql.remove(id)  # 在数据库列表中删除这个id
                s1 = 'select * from poetry where id = %d ;' % (id)
                ztup = db.check(s1)  # 查询这个id的信息
                title = ztup[0][1].replace('\n', '')  # 题目删除换行符
                ju = self.charPart(ztup[0])  # 正确答案诗句
                xx = []  # 盛放三个错误选项的列表
                AllList.remove(id)
                for i in range(3):
                    xid = choice(AllList)  # 随机抽取一个id
                    AllList.remove(xid)  # 再删除这个id
                    x1 = 'select * from poetry where id = %d ;' % (xid)
                    xtup = db.check(x1)  # 查询这个id的信息
                    xju = self.charPart(xtup[0])  # 错误答案诗句
                    xx.append(xju)
                return id, title, ju, xx, count  # 返回id,题目,正确选项,错误选项列表,次数
            else:
                return 'ok','ok', 'ok', 'ok', 'ok'  # 表示词汇都学完了
        except Exception as e:
            print(e)
            return 0,0, 0, 0, 0  # 表示获取单词信息失败


if __name__ == '__main__':
   pass
