

import requests
import parsel


def baocun(title, abc):
    with open('bizhi//' + title, mode='wb') as f:
        f.write(abc)
    print(f'{title}保存完成')


def data_qudizhi(title_url):
    data_1 = requests.get(url=title_url, headers=headers)
    data_2 = data_1.text
    data_3 = parsel.Selector(data_2)
    list_1 = data_3.xpath('//*[@id="scroll"]/li')
    list_2 = list_1.xpath('./a/@href').getall()
    return list_2


def data_wj(url):
    data_1 = requests.get(url=url, headers=headers)
    data_2 = data_1.text
    data_3 = parsel.Selector(data_2)
    list_1 = data_3.xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[1]/div/a/img/@src').get()
    response2 = requests.get(list_1)
    data = response2.content
    title_wjm = list_1.split('/')[-1]
    baocun(title_wjm, data)


headers = {
    'Cookie': 't=1c3eaf0ab2cec95025617da325eb34f7; r=6148; XSRF-TOKEN=eyJpdiI6IlFcL3dSMVZsRU1ld25HaEZqWUc0d2xnPT0iLCJ2YWx1ZSI6IjRXamR0WTd5OHY5VEVMb3JERGdkZXVMMTQrK1gzQSt0aEY5Z1U1WVRUbUtXMWhLQlZyUmdFZVwvaDZDbDJNcmlCeENcL2NLcXJcL0JpUTY3SUZ3RVlTcFU5aVZpKzB2cmQ3aWdXT05jSVVzNEZWd1pzOHMrS21JV1FSdTdtRWJ6UVZVIiwibWFjIjoiNWQyOWMxNGFiZmMwNDllMmMwNWJhNWViOWE4NTJmMzAwZmJjOGRhZjdlZjlhYjQ5Y2Q5ZTZlZjliYzhhNzlmOSJ9; win4000_session=eyJpdiI6Ik5EYVRVaUx1eFlGenA4cldmeWdEc2c9PSIsInZhbHVlIjoiUUc3Rk05QVlYQ3ZKRFVmZkJ5TWJNRVd2aFRNQmc4RDJjTFE2eTlEUGJGUkZPVllYTmxlQlZxR294eTBuR0l3cTMwNno3NGJXK3NCS3JRNGRwY0k3VzZnZWxTVlhuc2N3bm9VSmFGb2tMWkNFUHczQVV0NGkwZWF3dXVOMFN5Z0IiLCJtYWMiOiJlMGJiMzUwMTEwMzI4YjczMTAwY2Y5MjBhM2Y5NTZiYzQ1YTZiYzcwOTk4MzNhNDU2ZThhY2UxZDNkMWZjY2FiIn0%3D; UM_distinctid=17e950fbb45a3-03848034ed2a0b-f791539-144000-17e950fbb461090; CNZZDATA1279885023=1778491656-1643177742-null%7C1643177742',
    'Host': 'www.win4000.com',
    'Referer': 'http://www.win4000.com/zt/dongman.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
}
url = 'http://www.win4000.com/zt/gou.html'
data1 = requests.get(url=url, headers=headers)
data_t = data1.text
data_1 = parsel.Selector(data_t)

list_1 = data_1.xpath('/html/body/div[3]/div/div[3]/div[1]/div[1]/div[2]/div/div/ul/li')

for li in list_1:
    title_url = li.xpath('./a/@href').get()

    liebiao = data_qudizhi(title_url)

    for li in range(0, len(liebiao)):
        data_wj(liebiao[li])
