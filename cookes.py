#coding:utf-8
import requests

key = str(input("输入要查询的内容："))

url= "https://yaohuo.me"
header={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
"Cookie":"GUID=4181a83017354751; _ga=GA1.2.1015198034.1564479411; __gads=Test; ASP.NET_SessionId=v4phjr55nkur1y55ceznkl55; GET9423=; _gid=GA1.2.537718082.1571825545; sidyaohuo=734CDF9DFF8B37820_3_42_97907_700100-3-0-0-0-0; _gat_gtag_UA_88858350_1=1",
}
session = requests.Session()  #实例化session对象
# response = session.get(url,headers=header) #使用session对象发送get请求 就能获取服务端设置的session对象
# print(response.text)

url1 = "https://yaohuo.me/bbs/book_list.aspx?key="+key+"&type=title&siteid=1000&classid=0&action=search"
response = session.get(url1,headers=header)
print(response.text)
# r=requests.get(url,headers=header)
# print(r.text)