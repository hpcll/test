#coding:utf-8
months = (0,31,59,90,120,151,181,212,243,273,304,334)
months1 = (0,31,60,91,121,152,182,213,244,274,305,335)

month_31 = [1,3,5,7,8,10,12]
month_28 = [2]
month_30 = [4,6,9,11]

#2019 11 29

#所有异常的判断都用return的方式
#定义一个是否是平年的变量， 或者封装一个判断平润年的方法
##if 1 < month || month >12:
##   print("月份输入有误，请重新输入！")
##   return

# months_temp = func()? months : months1
# months_temp = null
# if(func()):
#months_temp = months
#else:
#months_temp = months1
# months months1 使用对应的数组


"""
months_temp = (year % 4 == 0 and year % 100 != 0) | (year % 100 == 0 and year % 400 == 0) ? months : months1




months_temp = months1 if (year % 4 == 0 and year % 100 != 0) | (year % 100 == 0 and year % 400 == 0) else months



 if month in month_28:
                        day = int(input("日："))
                        if 1<= day <=29:
                            mus = months_temp[month - 1]
                            count_mus = mus + day
                            print(year, "是闰年", "已经过去了", count_mus, "天")
                            # break
                        else:
                            print("输入的日期有误")
                    elif month in month_31:
                        day = int(input("日："))
                        if 1<= day <=31:
                            mus = months_temp[month - 1]
                            count_mus = mus + day
                            print(year, "是闰年", "已经过去了", count_mus, "天")
                            # break
                        else:
                            print("输入的日期有误")
                    elif month in month_30:
                        day = int(input("日："))
                        if 1<= day <=30:
                            mus = months_temp[month - 1]
                            count_mus = mus + day
                            print(year, "是闰年", "已经过去了", count_mus, "天")
                            # break


"""







try:
    year = int(input("年："))
    if 1 <= year:
        if (year % 4 == 0 and year % 100 != 0) | (year % 100 == 0 and year % 400 == 0):
            month = int(input("月："))
            if 1 <= month <= 12:
                if month in month_28:
                    day = int(input("日："))
                    if 1<= day <=29:
                        mus = months1[month - 1]
                        count_mus = mus + day
                        print(year, "是闰年", "已经过去了", count_mus, "天")
                        # break
                    else:
                        print("输入的日期有误")
                elif month in month_31:
                    day = int(input("日："))
                    if 1<= day <=31:
                        mus = months1[month - 1]
                        count_mus = mus + day
                        print(year, "是闰年", "已经过去了", count_mus, "天")
                        # break
                    else:
                        print("输入的日期有误")
                elif month in month_30:
                    day = int(input("日："))
                    if 1<= day <=30:
                        mus = months1[month - 1]
                        count_mus = mus + day
                        print(year, "是闰年", "已经过去了", count_mus, "天")
                        # break
                    else:
                        print("输入的日期有误，请重新输入！！")
                else:
                    print("输入的日期有误，请重新输入！！！")


            else:
                print("月份输入有误，请重新输入！")

        else:
            month = int(input("月："))
            if 1 <= month <= 12:
                if month in month_28:
                    day = int(input("日："))
                    if 1 <= day <= 28:
                        mus = months[month - 1]
                        count_mus = mus + day
                        print(year, "是平年", "已经过去了", count_mus, "天")
                        # break
                    else:
                        print("输入的日期有误")
                elif month in month_31:
                    day = int(input("日："))
                    if 1 <= day <= 31:
                        mus = months[month - 1]
                        count_mus = mus + day
                        print(year, "是平年", "已经过去了", count_mus, "天")
                        # break
                    else:
                        print("输入的日期有误")
                elif month in month_30:
                    day = int(input("日："))
                    if 1 <= day <= 30:
                        mus = months[month - 1]
                        count_mus = mus + day
                        print(year, "是平年", "已经过去了", count_mus, "天")
                        # break
                    else:
                        print("输入的日期有误，请重新输入！！")
                else:
                    print("输入的月份有误！！！")


            else:
                print("日期输入有误，请重新输入！！！")
    else:
        print("输入的日期有误，请重新输入！！！")
except ValueError:
    print('输入的不是整数，请重新输入')
