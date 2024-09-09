"""
    使用 css 选择器将猫眼 100 全部电影信息全部提取出来。
    目标网址：https://m.maoyan.com/board/4

    name（电影名）
    star（主演） 
    releasetime（上映时间）
    score（评分）
	
	提取出来print（）打印即可
"""
"""
	目标地址：https://m.maoyan.com/board/4

	要求：
		1、请求到目标网址数据，需要在请求到的数据中看到当前页面所有的电影名字、主演、上映时间、评分等信息
		2、请列举在请求不到数据时，需要添加几个常见请求头字段（课程讲过）

请在下方编写代码
"""
import parsel
import requests
import re

maoyan_url = 'https://m.maoyan.com/board/4'
headers = {
    'origin': 'https://m.maoyan.com',
    'Cookie': 'uuid_n_v=v1; iuuid=A05AA5A077F911ECB34881373B58C839CB357D67721C47B0B7C0C51AC51A90A8; webp=true; ci=1017%2C%E6%B3%97%E6%B0%B4; ci=1017%2C%E6%B3%97%E6%B0%B4; ci=1017%2C%E6%B3%97%E6%B0%B4; featrues=[object Object]; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1642467457; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1642467457; _last_page=undefined',
    'Host': 'm.maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}
shuju = requests.get(maoyan_url, headers=headers)
shuju.encoding = shuju.apparent_encoding
css_data =parsel.Selector(shuju.text)
name =css_data.css('div.info .title::text').getall()
star =css_data.css('div.info .actors::text').getall()
releasetime =css_data.css('div.info .date::text').getall()
score =css_data.css('span.number::text').getall()
abc = zip(name,star,releasetime,score)
for i in abc:
    print('电影名:',i[0],'主演:',i[1],'上映时间:',i[2],'评分:',i[3])

"""
    name（电影名）
    star（主演）
    releasetime（上映时间）
    score（评分）
"""

# shujut = shuju.text
# ming = re.findall('<div class="info" data-reactid=".*?"><h3 class="title" data-reactid=".*?">(.*?)</h3>', shujut, re.S)
# zhuyan = re.findall('<div class="actors" data-reactid=".*?">(.*?)</div>', shujut, re.S)
# pingfen = re.findall('<span class="number" data-reactid=".*?">(.*?)</span><span data-reactid=".*?">(.*?)</span></div>',
#                      shujut, re.S)
# sytime = re.findall('<div class="date" data-reactid=".*?">(.*?)</div>', shujut, re.S)
#
# b = []
# for i in pingfen:
#     bs = ' '.join(i)
#     b.append(bs)
#
# s = zip(ming, zhuyan, sytime[1:], b)
#
# for i in s:
#     print(i)
