#coding：utf-8
class bird:
    '鸟的结构'   #类文档字符串
    def wing(self):
        return "翅膀"
    def head(self):
        return "头"
    def foot(self):
        return "腿"
    def tail(self):
        return "尾巴"

a = bird()
print("这只鸟有一对白色的{},红色的{},黑色的{},蓝色的{}" .format(a.wing(),a.head(),a.foot(),a.tail()))
print("这只鸟有一对白色的%s,红色的%s,黑色的%s,蓝色的%s" % (a.wing(),a.head(),a.foot(),a.tail()))