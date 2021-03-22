#coding:utf-8
import requests
import json
import time
from lxml import etree

# def onepuls_draw():
#     url = "https://www.oneplusbbs.com/static/choujiang/css/choujiang_red.css?v=1616039794"
#     # querystring = {"version":"6","module":"choujiang","do":"draw","sign":"b744750fda400f56defe9796714e74d0f83f82aa"}
#
#     headers = {
#         'Content-Length': '0',
#         'Connection': 'Keep-Alive',
#         'Accept-Encoding': 'gzip',
#         'Cookkie':'opcid=1597050209506_64856680; opcct=1597050208000; www_clear=1; CNZZDATA1277373783=1790128622-1597045122-%7C1604648390; acw_tc=2f6a1f9616160396419175397e2d72153a4eefbc9fa2c756ea37394fce1edf; qKc3_0e8d_saltkey=Sz36VIC0; qKc3_0e8d_lastvisit=1616036042; qKc3_0e8d_sendmail=1; oppt=oneplus; opsid=1616039643326_1320356593; opsct=1616039643326; fp=68e99a80753444f50b7c6ad24a7521a4; ONEPLUSID=HT_Z02lwS0niWUxjzHZlh3JwdI_z5gCO7UnjHTPxmPG1hYiHRdfDr8ESMNR_O1VJdH69tH-wDVpThVr1YcPCTTTk540UXkjIHZts_-UsOcB4EuHGoS3n3wKpQ; bbs_uid=2340139; bbs_uname=hpcll; bbs_avatar=https%3A%2F%2Fimage01.oneplus.cn%2Fuser%2F201909%2F02%2F328%2F76787d010ec8cf56f125be8455acb9f4.jpg; bbs_grouptitle=95%23%E6%B1%BD%E6%B2%B9; opuserid=6388221; bbs_formhash=69eff3f9; qKc3_0e8d_sid=lKv7V7; qKc3_0e8d_ulastactivity=b26fK%2F63YdT00jAmyenmvf4J5fGyFUoXVCX8jng1kAQ7%2BrjQuySN; qKc3_0e8d_noticeTitle=1; bbs_sign=signed; opbct=1616039681000; optime_browser=1616039687477; opnt=1616039686000; opstep=5; opstep_event=1; qKc3_0e8d_creditbase=0D0D0D0D18737D0D0D0D0; qKc3_0e8d_creditnotice=0D0D0D0D-2D0D0D0D0D2340139; qKc3_0e8d_lastact=1616039794%09plugin.php%09; opsertime=1616039794000'
#     }
#
#     response = requests.request("GET", url, headers=headers,)
#     print(response.text)
#     data = json.loads(response.text)
#     msg = data["msg"]
#     return msg

def jy_count():
    url = "https://www.oneplusbbs.com/plugin-choujiang.html"


    headers = {
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Cookkie':'opcid=1597050209506_64856680; opcct=1597050208000; www_clear=1; CNZZDATA1277373783=1790128622-1597045122-%7C1604648390; acw_tc=2f6a1f9616160396419175397e2d72153a4eefbc9fa2c756ea37394fce1edf; qKc3_0e8d_saltkey=Sz36VIC0; qKc3_0e8d_lastvisit=1616036042; qKc3_0e8d_sendmail=1; oppt=oneplus; opsid=1616039643326_1320356593; opsct=1616039643326; fp=68e99a80753444f50b7c6ad24a7521a4; ONEPLUSID=HT_Z02lwS0niWUxjzHZlh3JwdI_z5gCO7UnjHTPxmPG1hYiHRdfDr8ESMNR_O1VJdH69tH-wDVpThVr1YcPCTTTk540UXkjIHZts_-UsOcB4EuHGoS3n3wKpQ; bbs_uid=2340139; bbs_uname=hpcll; bbs_avatar=https%3A%2F%2Fimage01.oneplus.cn%2Fuser%2F201909%2F02%2F328%2F76787d010ec8cf56f125be8455acb9f4.jpg; bbs_grouptitle=95%23%E6%B1%BD%E6%B2%B9; opuserid=6388221; bbs_formhash=69eff3f9; qKc3_0e8d_sid=lKv7V7; qKc3_0e8d_ulastactivity=b26fK%2F63YdT00jAmyenmvf4J5fGyFUoXVCX8jng1kAQ7%2BrjQuySN; qKc3_0e8d_noticeTitle=1; bbs_sign=signed; opbct=1616039681000; optime_browser=1616039687477; opnt=1616039686000; opstep=5; opstep_event=1; qKc3_0e8d_creditbase=0D0D0D0D18737D0D0D0D0; qKc3_0e8d_creditnotice=0D0D0D0D-2D0D0D0D0D2340139; qKc3_0e8d_lastact=1616039794%09plugin.php%09; opsertime=1616039794000'

        # 'Cookie': 'opcid=1597050209506_64856680; opcct=1597050208000; UM_distinctid=173d79c45e9a25-05405b478a61a1-15356650-1fa400-173d79c45eace8; www_clear=1; CNZZDATA1277373783=1790128622-1597045122-%7C1604648390; qKc3_0e8d_saltkey=N7et1rRz; qKc3_0e8d_lastvisit=1609141600; acw_tc=2f6a1faf16091453286746923e518db293e93c6fcb6e23712cb7239c3b64ce; oppt=oneplus; opsid=1609145330307_388828145; opsct=1609145330307; ONEPLUSID=HT_Z02lwS0niWUxjzHZlh3JwfooOdWDs54QwLt0YJGV27jKPvlOivoIOqyCtzIJOfo4oSouYb4r0tNr1YcPCTTTk540UXkjIHZts_-UsOcB4EuHGoS3n3wKpQ; bbs_uid=2340139; bbs_uname=hpcll; bbs_avatar=https%3A%2F%2Fimage01.oneplus.cn%2Fuser%2F201909%2F02%2F328%2F76787d010ec8cf56f125be8455acb9f4.jpg; bbs_grouptitle=95%23%E6%B1%BD%E6%B2%B9; opuserid=6388221; bbs_sign=unsigned; bbs_formhash=5e2f4073; qKc3_0e8d_sid=demhKt; qKc3_0e8d_ulastactivity=c400OTBJyHMJ3QNHqipv52BHrzOmovvzR%2BYLbHTxLqhBV8PujV6R; qKc3_0e8d_noticeTitle=1; opstep_event=0; opsertime=1609145720000; qKc3_0e8d_checkpm=1; qKc3_0e8d_lastact=1609145720%09home.php%09misc; qKc3_0e8d_sendmail=1; opbct=1609145450000; optime_browser=1609145720644; opnt=1609145720000; opstep=7; fp=fd4dc0f25c5d41ea55743d70a7ace3ad; qKc3_0e8d_ulastactivity=616aWLhySRauaxrv6zzMxsNyrpGIc10ZGm8CuIncRz160ZOCPW3R; acw_tc=2f6a1fd616091455001245181e88db07dfb2bc682408d6c9d68c3635b1721d; qKc3_0e8d_saltkey=wLcKlzpt; qKc3_0e8d_lastvisit=1609141900; bbs_avatar=https%3A%2F%2Fimage01.oneplus.cn%2Fshop%2F201811%2F12%2F1439%2F53bf1de95a7f8d0e902e76148ec90976.png; bbs_grouptitle=%E6%B8%B8%E5%AE%A2; bbs_formhash=8eb28187; ONEPLUSID=HT_Z02lwS0niWUxjzHZlh3JwfooOdWDs54QwLt0YJGV27jKPvlOivoIOqyCtzIJOfo4oSouYb4r0tNr1YcPCTTTk540UXkjIHZts_-UsOcB4EuHGoS3n3wKpQ; bbs_sign=unsigned; qKc3_0e8d_sid=demhKt; qKc3_0e8d_lastact=1609146033%09plugin.php%09; opuserid=6388221; opsertime=1609146033000'
    }

    response = requests.request("GET", url, headers=headers)
    # print(response.text)
    return response.text



# if __name__ == '__main__':
#     a=0
#     while a < 10 :
#         msg = onepuls_draw()
#         a +=1
#         print("第 %d 次" % a ,msg)
#         time.sleep(5)
# #         html = jy_count()
# #         print(html)
# #         dom = etree.HTML(html)
# #         result = etree.tostring(dom)
# #         print(html.find('我的加油'))
# #         # my_jiayou = dom.xpath('//div[@class =’ma_about_me’]')
# #         # print(type(result))
if __name__ == '__main__':
    print(jy_count())