"""
    使用 css 选择器将快代理中我需要的信息提取出来。
    目标网址：https://www.kuaidaili.com/free/
    
    需要解析以下数据:
        ip、
        port、
        类型
	
	提取出来print（）打印即可
"""
import requests
import parsel

headers = {
    'Connection': 'keep-alive',
    'Cookie': 'channelid=0; sid=1642822575732762; _gcl_au=1.1.274058625.1642822945; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1642822945; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1642822945',
    'Host': 'www.kuaidaili.com',
    'Pragma': 'no-cache',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

url = 'https://www.kuaidaili.com/free/'

response = requests.get(url=url, headers=headers)
html_data = parsel.Selector(response.text)
html_data1 =html_data.css('body tbody')

ip = html_data1.css('tr>td:nth_child(1)::text').getall()
port = html_data1.css('tr>td:nth_child(2)::text').getall()
lei = html_data1.css('tr>td:nth_child(4)::text').getall()

shuju =zip(ip,port,lei)
for shu in shuju:
    print(f"ip:{shu[0]},port:{shu[1]},类型:{shu[2]}.")
"""
需要解析以下数据:
        ip、
        port、
        类型
"""

