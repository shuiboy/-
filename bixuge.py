import requests
import parsel
import re

headers = {
#'Cookie': '__gads=ID=2cf2649fa6e1dc22-228f14fe3dd000f7:T=1643513953:RT=1643513953:S=ALNI_MbcHRJtaP5U2csLltBzttbzvNrmkg; UM_distinctid=17ea910c03f114-0ee8d6b4591cf5-f791539-144000-17ea910c040bd4; CNZZDATA4625776=cnzz_eid%3D43978719-1643512691-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1644204359',
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
