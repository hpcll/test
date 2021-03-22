import requests
import os

branch = os.environ["branch"]
work_path = os.environ["work_path"]
if work_path == "H5_V2.0_DEV":
  system = "iOS"
elif work_path == "H5_V2.0_DEV-Andriod":
  system = "Android"



url = "https://open.feishu.cn/open-apis/bot/v2/hook/fb13c1dc-742a-4c5b-8479-08525e02a6b5"
payload = "{\n    \"msg_type\": \"post\",\n    \"content\": {\n        \"post\": {\n            \"zh_cn\": {\n                \"" \
          "title\": \"H5Baseline_V2.0-Test环境部署通知\",\n                \"content\": [\n                    [\n                    \t{\n                            \"tag\": \"at\",\n                            \"user_id\": \"all\" \n                        },\n                        \n                        {\n                            \"tag\": \"text\",\n                            \"text\": \" \\r\\n" \
          "【项     目】H5Baseline-Test环境部署已完成，\\r\\n" \
          "【分     支】"+branch+"\\r\\n" \
          "【系     统】"+system+"\\r\\n" \
          "【dist.prod.zip】正式环境文件。 \\r\\n===================\\r\\n\" \n                            \n                        },\n                        \n                        {\n                            \"tag\": \"a\",\n                            \"" \
          "text\": \"dist.prod.zip文件下载地址\",\n                            " \
          "\"href\": \"http://192.168.50.23:66/dist.prod.zip\"" \
          "\n                        }\n                         \n                    ]\n                ]\n            }\n        }\n    }\n}"
headers = {
  'Content-Type': 'application/json'
}
payload = payload.encode('utf8')
response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
