import requests
import base64

token_online = ['6f334e39bb3e34de5a76f0faacc6e9e2da91b876b8a799464696906770f4448cf48b4c115c37e3c8429f2fc757de2a231507a2d59e445f72363972fd9b0df0482ede24d2f5915126be599350058353da027bd49aa3995b8be307ffd5bef8fdc54bfc94c2106ae81ad08133882dac68469e7e41a675f3e55e88def93fb36f700cc72886b5a4e9d4d3ef25107df7350d96b02c80cea1027395353b278ee793579a5c189a8ce9b5b321b7a33e5a5786dbf42a96352bc798ee7758dfc75326ce62abe18bdaf6c0d9efa2a223f7480d14152438b70e36700f6099c1557d9c03be59e6977a87fbc93ee0e9459c231dc749a9fb5ff75df7712697084d6bd8a85e22bc07762720bb27ac8dc083066c3825838f1169d00947da1f20adcbdb68c77b082edad20c37679ba7c2ca9e01d4533ddb3092']
appId = ['86b8be06f56ba55e9fa7dff134c6b16c39b031d931057a9a5d8963f3ec7d40872272e9dd68eab9b9fd37ece944afab3b55edfe66c37dc5dd268070010cf2cc600294a3a862bd1ca39f85d25cfc83f5b4']
url_1 = 'https://m.client.10010.com/welfare-mall-front/mobile/show/bj2207/v1'

def start():
    for Token_online,appid in zip(token_online,appId):
        res = requests.post('https://m.client.10010.com/mobileService/onLine.htm', data='token_online=' + Token_online + '&appId=' + appid + '&version=iphone_c@7.0500').json()
        if res['code'] in '0':
            cookie = 'ecs_token=' + res['ecs_token']
            phone = res['default']
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': cookie,
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 unicom{version:iphone_c@7.0500}{systemVersion:dis}{yw_code:}'
            }
            a = phone + '|2380'
            b = base64.b64encode(a.encode('utf-8'))
            res_1 = requests.get(url_1, headers=headers)
            number = res_1.json()['resdata']['Fnumber']
            x = '8a29ac8a75a30e4e0175ba89c3dc1009'
            y = '8a29ac8a75a30e4e0175b721ae490a5a'
            z = '8a29ac89747dfeed01747e48e50c0024'
            if int(number) > 500:
                if int(number) > 2000:
                    test = z
                elif int(number) > 1000:
                    test = y
                else:
                    test = x
                res2 = requests.get('https://m.client.10010.com/welfare-mall-front/mobile/show/bj2200/v2/' + test + '/0000')
                SHOP_INTEGRAL = res2.json()['resdata']['goods']['SHOP_INTEGRAL']
                GOODS_NAME = res2.json()['resdata']['goods']['GOODS_NAME']
                res_2 = requests.post('https://m.client.10010.com/welfare-mall-front/mobile/api/whetherNeedVerificationCodeNew/v1', headers=headers, data='reqdata={"pip":"0.0.0.0","goodsIdOrOrderNo":"' + test + '","phone":"' + str(b,'utf-8') + '"}')
                #print(GOODS_NAME + phone + res_2.json()['msg'])
                res__2 = requests.post('https://m.client.10010.com/welfare-mall-front/mobile/api/bj2402/v1', headers=headers, data='reqdata={"goodsId":"' + test + '","reChangeNo":"' + phone + '","saleTypes":"TY","points":' + SHOP_INTEGRAL + ',"smsCode":null,"imei":"","sourceChannel":"KYJF9990000010001","proFlag":"","scene":"","promoterCode":"","sign":"","oneid":"","twoid":"","threeid":"","maxcash":"","floortype":"undefined","launchId":""}')
                print(GOODS_NAME + phone + res__2.json()['msg'])

            else:
                print(phone + '_number*' + str(number))
        else:
            print(res['msg'])
        
        

def main_handler(event, context):
    return start()

if __name__ == '__main__':
    start()