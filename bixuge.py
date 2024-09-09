import requests
import parsel
import re

headers = {
'Host': 'www.shengxu5w.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
}
url = 'https://www.shengxu5w.com/4_4676/'
res =requests.get(url=url,headers=headers)
res.encoding = res.apparent_encoding

res_data = parsel.Selector(res.text)
biaoti = res_data.xpath('//*[@id="list"]/dl/dd/a/text()').getall()[3520:]
lianjie = res_data.xpath('//*[@id="list"]/dl/dd/a/@href').getall()[3520:]
print(biaoti,lianjie)

def paneirong(bt,lj):
    url = 'https://www.shengxu5w.com'+lj
    res = requests.get(url=url, headers=headers)
    res.encoding = res.apparent_encoding
    res_data = parsel.Selector(res.text)
    neirong = res_data.xpath('//*[@id="content"]/text()').getall()
    neirong = [nr.strip() for nr in neirong]
    nrstr = "\n".join(neirong)
    nrstrt = re.sub("\n+", "\n", nrstr)

    with open('wangu.txt',mode='a',encoding='utf-8') as f:
        f.write(bt)
        f.write('\n')
        f.write(nrstrt)
        f.write('\n\n')

    print(bt,"保存完成。")

for i in range(len(lianjie)):
    paneirong(biaoti[i],lianjie[i])
