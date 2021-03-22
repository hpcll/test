import requests
import json
url = "https://dler.cloud/api/v1/information"

payload = 'email=xiaomayi0323@gmail.com&passwd=Kingson0323'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}
#流量查询h
response = requests.request("POST", url, headers=headers, data = payload)
dict = json.loads(response.text)
last_flow = dict['data']['unusedTraffic']#剩余流量
Used_flow = dict['data']['usedTraffic']#已使用流量
unused_flow = int(float(last_flow[0:-2]))
#飞书通知请求
url1 = "https://open.feishu.cn/open-apis/bot/v2/hook/df17bd6a-2a5d-4a40-8a05-393a045d641f"
payload1 = "{\n    \"msg_type\": \"post\",\n    \"content\": {\n        \"post\": {\n            \"zh_cn\": {\n                \"title\": \"Dler Cloud流量使用提醒\",\n                \"content\": [\n                    [\n                    \t{\n                            \"tag\": \"at\",\n                            \"user_id\": \"all\" \n                        },\n                        \n                        {\n                            \"tag\": \"text\",\n                            \"text\": \" \\r\\n【已用流量】"+Used_flow+"\\r\\n【剩余流量】"+last_flow+"。\\r\\n【温馨提示】请赶快充值哦。 \\r\\n===================\\r\\n\" \n                            \n                        },\n                        \n                        {\n                            \"tag\": \"a\",\n                            \"text\": \"点击这里，立马充值\",\n                            \"href\": \"https://dlercloud.com/user\"\n                        }\n                         \n                    ]\n                ]\n            }\n        }\n    }\n}"
headers1 = {
  'Content-Type': 'application/json'
}
payload1 = payload1.encode("utf8")

#判断剩余流量是否大于10GB
if unused_flow <= 10:
    response1 = requests.request("POST", url1, headers=headers1, data = payload1)