#coding:utf_8
import requests
import json
import time
def onepuls_draw():
    url = "http://api.oneplusbbs.com/api/mobile/index.php"

    querystring = {"version":"6","module":"choujiang","do":"draw","sign":"b744750fda400f56defe9796714e74d0f83f82aa"}

    headers = {
        'Content-Length': "0",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'Cookie': "qKc3_0e8d_lastvisit=1577147237; qKc3_0e8d_forum_lastvisit=D_138_1577150846D_135_1577151080; qKc3_0e8d_st_t=2340139%7C1577151080%7C6d6549c6ee1c615ee74bd5128a33e6be; qKc3_0e8d_sid=i7me3r; bbs_uid=2340139; qKc3_0e8d_visitedfid=112D2D135D138; qKc3_0e8d_st_p=2340139%7C1577418566%7C5829d6cedbf1ecada1cb20c3ab0dcc80; bbs_grouptitle=%E6%8E%BA%E6%B0%B4%E6%B2%B9; bbs_sign=signed; qKc3_0e8d_lastact=1577418661%09index.php%09; bbs_formhash=1789c565; qKc3_0e8d_ulastactivity=809cERJfCJTVEJKtRTyTZ84EmPXcRu0nUHqW%2Fq%2BYEzdha%2Bo07gv%2F; qKc3_0e8d_saltkey=RkCNzeGN; ONEPLUSID=ONEPLUS_AC_274e55513fb12d9ea3a1a717ccdeed9d; acw_tc=7819730615771508353161033eae535101f4c0938ffed60de73d22927e0e7b; qKc3_0e8d_taskdoing_2340139=1; opuserid=6388221; qKc3_0e8d_creditrule=%E5%8F%91%E8%A1%A8%E5%9B%9E%E5%A4%8D; qKc3_0e8d_creditbase=0D0D0D0D234D0D0D0D0; qKc3_0e8d_viewid=tid_5201305; bbs_avatar=https%3A%2F%2Fimage01.oneplus.cn%2Fuser%2F201909%2F02%2F328%2F76787d010ec8cf56f125be8455acb9f4.jpg; ONEPLUSTOKEN=ONEPLUS_AC_fd806c6124115628ffc94bdc16a52a01; qKc3_0e8d_home_diymode=1; qKc3_0e8d_atarget=1; qKc3_0e8d_viewidTimes=1; bbs_uname=hpcll; qKc3_0e8d_creditnotice=0D0D0D0D-2D0D0D0D0D2340139,qKc3_0e8d_lastvisit=1577147237; qKc3_0e8d_forum_lastvisit=D_138_1577150846D_135_1577151080; qKc3_0e8d_st_t=2340139%7C1577151080%7C6d6549c6ee1c615ee74bd5128a33e6be; qKc3_0e8d_sid=i7me3r; bbs_uid=2340139; qKc3_0e8d_visitedfid=112D2D135D138; qKc3_0e8d_st_p=2340139%7C1577418566%7C5829d6cedbf1ecada1cb20c3ab0dcc80; bbs_grouptitle=%E6%8E%BA%E6%B0%B4%E6%B2%B9; bbs_sign=signed; qKc3_0e8d_lastact=1577418661%09index.php%09; bbs_formhash=1789c565; qKc3_0e8d_ulastactivity=809cERJfCJTVEJKtRTyTZ84EmPXcRu0nUHqW%2Fq%2BYEzdha%2Bo07gv%2F; qKc3_0e8d_saltkey=RkCNzeGN; ONEPLUSID=ONEPLUS_AC_274e55513fb12d9ea3a1a717ccdeed9d; acw_tc=7819730615771508353161033eae535101f4c0938ffed60de73d22927e0e7b; qKc3_0e8d_taskdoing_2340139=1; opuserid=6388221; qKc3_0e8d_creditrule=%E5%8F%91%E8%A1%A8%E5%9B%9E%E5%A4%8D; qKc3_0e8d_creditbase=0D0D0D0D234D0D0D0D0; qKc3_0e8d_viewid=tid_5201305; bbs_avatar=https%3A%2F%2Fimage01.oneplus.cn%2Fuser%2F201909%2F02%2F328%2F76787d010ec8cf56f125be8455acb9f4.jpg; ONEPLUSTOKEN=ONEPLUS_AC_fd806c6124115628ffc94bdc16a52a01; qKc3_0e8d_home_diymode=1; qKc3_0e8d_atarget=1; qKc3_0e8d_viewidTimes=1; bbs_uname=hpcll; qKc3_0e8d_creditnotice=0D0D0D0D-2D0D0D0D0D2340139; acw_tc=784c10e615774189290091267e47234b6f030ca0803d730d899c17fa082dca; qKc3_0e8d_creditbase=0D0D0D0D242D0D0D0D0; qKc3_0e8d_creditnotice=0D0D0D0D-2D0D0D0D0D2340139; qKc3_0e8d_sid=FTfyZC; qKc3_0e8d_lastact=1577423341%09index.php%09",
        'Cookie2': "$Version=1",
        'User-Agent': "PostmanRuntime/7.19.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "api.oneplusbbs.com",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    msg = data["msg"]
    return msg


if __name__ == '__main__':
    a=0
    while a < 10 :
        msg = onepuls_draw()
        a +=1
        print("第 %d 次" % a ,msg)
        time.sleep(5) 