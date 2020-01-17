import requests
from lxml import etree
import time
import random

url = 'http://www.job5156.com/qiye/hebei-0/'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}
# 设置代理池 为防止网页出现  频繁登录 而不能获取部分源码的情况
procxy = [
    {'https':'36.6.147.197:28546'},
    {'https':'223.241.117.118:18118'},
    {'https':'114.239.172.141:38001'},
    {'https':'116.113.27.170:47849'},
    {'https':'223.241.116.9:8010'}
]
#随机获取代理
http = random.choice(procxy)
#返回请求
response = requests.get(url = url,headers = headers,proxies = http)
random = random.randint(3,10)
# time.sleep(random)  之前出现频繁登录无法获得部分源码的情况：  1.未设置代理2.响应时间一直相同，被检测为机器人   结果是1影响的  


#对html自动修正（如缺失节点可以自动填上），并构造一个xpath对象
html = etree.HTML(response.text)
# print(response.text)

#xpath对象可以获取节点
com_name = html.xpath('//div[@class = "line_com"]/a[@class = "com_name"]/text()')
com_job = html.xpath('//div[@class = "line_cate"]/a/text()')
# print(type(com_name),com_name)   可以发现com_name的类型是个list，com_job同理 那么我们可以进行遍历打印或者存储至文档及其他介质中
for i in range(0,len(com_name)):
    print(str(i)+"  "+com_name[i]+"   "+com_job[i])

#上述是对第一页网页进行爬取，那么后面的网页可以发现规律，每点击  下一页  网页的路径会变，兄弟姐妹们实操下就能发现规律
for j in range(2,67):
    #发现规律之后 对网页进行遍历 range的范围是[2,67),左闭右开  剩下的就是按上面的逻辑来了
    url = 'http://www.job5156.com/qiye/hebei-0/pn'+str(j)
    response = requests.get(url = url,headers = headers,proxies = http)
#     time.sleep(random)
    html = etree.HTML(response.text)

    com_name = html.xpath('//div[@class = "line_com"]/a[@class = "com_name"]/text()')
    com_job = html.xpath('//div[@class = "line_cate"]/a/text()')
    for k in range(0,len(com_name)):
        print(str(k)+"  "+com_name[k]+"   "+com_job[k])
    
