months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
months1 = (0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335)

def is_leapyear():
    year = int(input("请输入年份："))
    month = int(input("请输入月份："))
    day = int(input("请输入日子："))

    if (year <= 0) | (1 > month | month > 12) | (1 > day | day > 31):
        print('输入的年月日有误，请重新输入')
        return

    is_leapyear = (year % 400 == 0) | (year % 4 == 0 and year % 100 != 0)
    months_temp = months1 if is_leapyear else months
    mus = months_temp[month - 1]
    count_mus = mus + day
    print(" %d年" % year,"是闰年" if is_leapyear else "是平年","已经过去了 %s 天" % count_mus)


if __name__ == '__main__':
    try:
        is_leapyear()
    except ValueError:
        print('输入的不是整数，请重新输入')
