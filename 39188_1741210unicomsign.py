# coding=utf-8
# author:@QingYuan 39188
import re
from time import sleep
import datetime
import requests
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64


class UnicomSign():

    def __init__(self):
        self.UA = None
        self.VERSION = '8.0200'
        self.request = requests.Session()

    # 加密算法
    def rsa_encrypt(self, str):
        # 公钥
        publickey = '''-----BEGIN PUBLIC KEY-----
        MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDc+CZK9bBA9IU+gZUOc6
        FUGu7yO9WpTNB0PzmgFBh96Mg1WrovD1oqZ+eIF4LjvxKXGOdI79JRdve9
        NPhQo07+uqGQgE4imwNnRx7PFtCRryiIEcUoavuNtuRVoBAm6qdB0Srctg
        aqGfLgKvZHOnwTjyNqjBUxzMeQlEC2czEMSwIDAQAB
        -----END PUBLIC KEY-----'''
        rsakey = RSA.importKey(publickey)
        # rsakey = RSA.importKey(open("public.pem").read())
        cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 创建用于执行pkcs1_v1_5加密或解密的密码
        cipher_text = base64.b64encode(cipher.encrypt(str.encode('utf-8')))
        return cipher_text.decode('utf-8')
        # print(cipher_text.decode('utf-8'))

    # 用户登录
    def login(self, mobile, passwd):
        self.UA = 'Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36; unicom{version:android@' + self.VERSION + ',desmobile:' + mobile + '};devicetype{deviceBrand:Xiaomi,deviceModel:MI 6};{yw_code:}'
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        headers = {
            'Host': 'm.client.10010.com',
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive',
            'Cookie': 'devicedId=20be54b981ba4188a797f705d77842d6',
            'User-Agent': self.UA,
            'Accept-Language': 'zh-cn',
            'Accept-Encoding': 'gzip',
            'Content-Length': '1446'
        }
        login_url = 'https://m.client.10010.com/mobileService/login.htm'
        login_data = {
            "deviceOS": "android9",
            "mobile": self.rsa_encrypt(mobile),
            "netWay": "Wifi",
            "deviceCode": "20be54b981ba4188a797f705d77842d6",
            "isRemberPwd": 'true',
            "version": "android@"+self.VERSION,
            "deviceId": "20be54b981ba4188a797f705d77842d6",
            # "token_online": "6f334e39bb3e34de5a76f0faacc6e9e2bfbe67f4d12d709f636a410aee94f38d1bc4abf73429d39c40ab144a1fa3991b91a546e1507ebed9b37729b6e318aadf43b237c97d48e5574d2a0315906bb4a1a552ff237a0ebfe5840c790b8655a907c95f0becd59c7e725d1ea705d2f84a4ae96f7f1e54f1d3bc6ca0395352de23f402afb4c078a1c81f138fb6c2d2b667ea9fc36576ea2445da48e0ce0665401ea00931ac8bab7da67b16456d0e6487455a64c0908aad6ac81ffb8c8aeedd71395d1643eecdb43ea5ca8b821651df18c03ef482e9e702d9cb98de0a710940de2f33ee9024d007197a6f4ea8027c23684c012923665553e83f5cd43ae888d3d289a87abf83f575bd341646a3baf7beffbd3e498e2769e8c57473b2a62e8cff341e0dffee9de7d5cd0404ebd3f2dc73825097",
            "password": self.rsa_encrypt(passwd),
            "keyVersion": 1,
            "provinceChanel": "general",
            "appId": "86b8be06f56ba55e9fa7dff134c6b16c39b031d931057a9a5d8963f3ec7d40872272e9dd68eab9b9fd37ece944afab3b55edfe66c37dc5dd268070010cf2cc600294a3a862bd1ca39f85d25cfc83f5b4",
            "deviceModel": "MI 6",
            "deviceBrand": "Xiaomi",
            "timestamp": timestamp
        }
        # print(loginData)
        res1 = self.request.post(login_url, data=login_data, headers=headers)
        # res1.encoding = 'gbk'
        if res1.status_code == 200:
            print(">>>获取登录状态成功！")
            print(res1.text)
        else:
            print(">>>获取登录状态失败！")
        # print("登录成功cookies：", self.request.cookies)
        sleep(3)

    # 每日签到领积分、1g流量日包
    def daysign(self):
        headers = {
            "user-agent": self.UA,
            "referer": "https://img.client.10010.com",
            "origin": "https://img.client.10010.com"
        }
        res0 = self.request.post("https://act.10010.com/SigninApp/signin/getIntegral", headers=headers)
        if res0.json()['status'] == '0000':
            print(">>>签到前积分：" + res0.json()['data']['integralTotal'])
        else:
            print(">>>获取积分信息失败！")
        # print(1,res0.json())
        res1 = self.request.post("https://act.10010.com/SigninApp/signin/getContinuous", headers=headers)
        # print(res1.text)
        sleep(3)
        if res1.json()['data']['todaySigned'] == '1':
            res2 = self.request.post("https://act.10010.com/SigninApp/signin/daySign", headers=headers)
            # print(res2.json())
            print('>>>签到成功！')
        else:
            print('>>>今天已签到！')
            # print(res1.json())

        # 看视频，积分翻倍
        sleep(3)
        res3 = self.request.post("https://act.10010.com/SigninApp/signin/bannerAdPlayingLogo", headers=headers)
        if res3.json()['status'] == '0000':
            print(">>>积分翻倍成功！")
        else:
            print(res3.json()['msg'])
        # print(res3.json())
        res4 = self.request.post("https://act.10010.com/SigninApp/signin/getIntegral", headers=headers)
        if res4.json()['status'] == '0000':
            print(">>>签到后积分：" + res4.json()['data']['integralTotal'])
        else:
            print(">>>获取积分信息失败！")
        # print(2,res4.json())
        # 每日领取1G流量日包
        res5 = self.request.post("https://act.10010.com/SigninApp/doTask/finishVideo", headers=headers)
        res6 = self.request.post("https://act.10010.com/SigninApp/doTask/getTaskInfo", headers=headers)
        res7 = self.request.post("https://act.10010.com/SigninApp/doTask/getPrize", headers=headers)
        if res7.json()['status'] == '0000':
            print(">>>1G流量日包领取成功！")
        else:
            print(">>>1G流量日包任务失败！")

    # 每日任务
    def daytask(self):
        headers = {
            "user-agent": self.UA,
            "referer": "https://img.client.10010.com",
            "origin": "https://img.client.10010.com"
        }
        # 娱乐中心--每日打卡
        data1 = {
            'methodType': 'signin',
            'clientVersion': self.VERSION,
            'deviceType': 'Android',
        }
        res1 = self.request.post("https://m.client.10010.com/producGame_signin", data=data1, headers=headers)
        res1.encoding = 'utf-8'
        print(">>>每日打卡：", res1.json()['respDesc'])
        # 游戏宝箱
        data2 = {
            'methodType': 'reward',
            'deviceType': 'Android',
            'clientVersion': self.VERSION,
            'isVideo': 'N'
        }

        res2 = self.request.post("https://m.client.10010.com/game_box", data=data2, headers=headers)
        res2.encoding = 'utf-8'
        print(">>>游戏宝箱任务：", res2.json()['desc'])
        sleep(3)
        data3 = {
            'methodType': 'reward',
            'deviceType': 'Android',
            'clientVersion': self.VERSION,
            'isVideo': 'Y'
        }
        sleep(3)
        res3 = self.request.post("https://m.client.10010.com/game_box", data=data3, headers=headers)
        res3.encoding = 'utf-8'
        print(">>>游戏宝箱翻倍：", res3.json()['desc'])
        # 领取游戏宝箱100M
        data4 = {
            'methodType': 'taskGetReward',
            'taskCenterId': '187',
            'clientVersion': self.VERSION,
            'deviceType': 'Android'
        }
        res4 = self.request.post("https://m.client.10010.com/producGameTaskCenter", data=data4, headers=headers)
        res4.encoding = 'utf -8'
        print(">>>游戏宝箱", res4.json()['msg'])
        # 沃之树任务
        res5 = self.request.post("https://m.client.10010.com/mactivity/arbordayJson/arbor/3/0/3/grow.htm", headers=headers)
        print(">>>每日浇水：", res5.json()['msg'])
        # 签到看视频，下载APP流量奖励
        print(">>>签到看视频，下载APP流量奖励任务开始...")
        data5 = {
            'stepflag': 22
        }
        data6 = {
            'stepflag': 23
        }
        for i in range(3):
            res5 = self.request.post("https://act.10010.com/SigninApp/mySignin/addFlow", data=data5, headers=headers)
            sleep(3)
            res6 = self.request.post("https://act.10010.com/SigninApp/mySignin/addFlow", data=data6, headers=headers)
        print(">>>签到看视频，下载APP流量奖励任务完成！")
        # 金币抽奖免费3次
        res7 = self.request.post("https://m.client.10010.com/dailylottery/static/textdl/userLogin", headers=headers)
        data8 = {
            'usernumberofjsp': re.findall(r"encryptmobile=(.+?)';", res7.text)[0],
            'flag': 'convert'
        }
        for i in range(3):
            res8 = self.request.post("https://m.client.10010.com/dailylottery/static/doubleball/choujiang", data=data8, headers=headers)
            print(">>>金币抽奖：", res8.json()['RspMsg'])
            sleep(3)


if __name__ == '__main__':
    user = UnicomSign()
    user.login('17600218893', '134679')  # 用户登录
    user.daysign()  # 日常签到领积分，1g流量日包
    user.daytask()  # 日常任务
    print("所有任务执行完成！")