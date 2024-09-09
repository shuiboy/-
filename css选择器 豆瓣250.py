"""
    使用 css 选择器将豆瓣250 十页的全部电影信息全部提取出来。
    目标网址：https://movie.douban.com/top250

    title（电影名）
    info（导演、主演、出版时间）
    score（评分）
    follow（评价人数）
	
	提取出来print（）打印即可
"""
import requests
import parsel

headers = {
    'Cookie': 'bid=iWYwU2-TFvo; __gads=ID=57b0506ac2f0ed84-222f36f4ffcf00ea:T=1642390701:RT=1642390701:S=ALNI_MZMF4l8onrUIiV-I1IfJfh9dE_ukA; viewed="35548345"; gr_user_id=fc621b6a-ff44-4f63-a419-47948c3925b6; __utmz=30149280.1642745314.3.3.utmcsr=guozhivip.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.534985532.1642390703.1642745314.1642816367.4; __utmb=30149280.0.10.1642816367; __utmc=30149280; __utma=223695111.385909688.1642816367.1642816367.1642816367.1; __utmb=223695111.0.10.1642816367; __utmc=223695111; __utmz=223695111.1642816367.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _pk_id.100001.4cf6=0b31784093bb3527.1642816367.1.1642817067.1642816367.',
    'Host': 'movie.douban.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'

}
num = 0
for page in range(0, 230, 25):
    url = f'https://movie.douban.com/top250?start={page}&filter='
    response = requests.get(url=url, headers=headers)
    html_data = parsel.Selector(response.text)
    data = html_data.css('div.article .grid_view')

    titles = data.css('span.title:nth-child(1)::text').getall()
    infos = html_data.css('div.item .info p:nth-child(1)::text').getall()
    scores = html_data.css('span.rating_num::text').getall()
    follows = html_data.css('div.star>span:nth-child(4)::text').getall()

    infos_1 = []
    infos_2 = []
    for i in infos:
        if infos.index(i) % 2 == 0:
            i1 = i.replace(' ', '').replace('\n', '').replace('\xa0\xa0\xa0', ' ')
            infos_1.append(i1)
        else:
            i2 = i.replace(' ', '').replace('\n', '')[:4]
            infos_2.append(i2)
    infos_0 = []
    for i in range(len(infos_1)):
        infos_0.append(infos_1[i] + "出版时间:" + infos_2[i])

    datas = zip(titles, infos_0, scores, follows)
    num += 1
    print(f"============================现在是第{num}页===================================")
    for da in datas:
        print(f'电影名：{da[0]}，导演、主演、出版时间：{da[1]}，评分：{da[2]}，评价人数：{da[3]}。')

"""
title（电影名）
    info（导演、主演、出版时间）
    score（评分）
    follow（评价人数）
"""
