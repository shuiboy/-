import csv
import time
import requests
import parsel
import concurrent.futures
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': '__uuid=1645516962750.98; __gc_id=928a9b57bd6e4d538ed74add39fa2a96; __s_bid=01b7b2d273faff9d39e1e194ef8f9ec7f53d; acw_tc=276077c416455774431833204e29a41a25fc193631e19aa6940eb9e24709be; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1645516963,1645577444; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1645577444; __tlog=1645577443963.54%7C00000000%7C00000000%7C00000000%7C00000000; __session_seq=1; __uv_seq=1',
    'Host': 'www.liepin.com',
    'Pragma': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
}
def qingqiu(url):
    data_all = requests.get(url=url, headers=headers)
    return data_all

def jiexi(data_all):
    data_1 = parsel.Selector(data_all.text)
    lis = data_1.css('div.left-list-box>ul>li')
    return lis

def huoqu(lis):
    for li in lis:
        title = li.css('.job-title-box>div::text').get()
        didian = li.css('.job-dq-box>span:nth-child(2)::text').get()
        xinzi = li.css('.job-salary::text').get()
        yaoqius = li.css('.job-labels-box>span::text').getall()
        gongsi = li.css('.company-name.ellipsis-1::text').get()
        lingyu = li.css('.company-tags-box.ellipsis-1>span:nth-child(1)::text').get()
        guimo = li.css('.company-tags-box.ellipsis-1>span:nth-child(2)::text').get()
        lianxiren = li.css('.recruiter-name.ellipsis-1::text').get()
        lxrzw = li.css('.recruiter-title.ellipsis-1::text').get()
        yaoqiu=[]
        for yq in yaoqius:
            yaoqiu.append(yq)
        yaoqiu = ",".join(str(x) for x in yaoqiu)
        print(title,didian,xinzi,yaoqiu,gongsi,lingyu,guimo,lianxiren,lxrzw)
        d = [title,didian,xinzi,yaoqiu,gongsi,lingyu,guimo,lianxiren,lxrzw]
        savas(d)

def savas(d):
    with open('liepin.csv',mode='a',encoding='utf-8',newline='') as f:
        csv_w = csv.writer(f)
        csv_w.writerow(d)

def main(url):
    data_all = qingqiu(url)
    lis = jiexi(data_all)
    huoqu(lis)


if __name__ == '__main__':
    start_time = time.time()
    with open('liepin.csv', mode='a', encoding='utf-8', newline='') as f:
        csv_w = csv.writer(f)
        csv_w.writerow(['名称', '地点', '薪资', '要求', '公司名称', '公司领域', '公司规模', '联系人', '联系人职务'])
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        for i in range(0,10):
            url = f'https://www.liepin.com/zhaopin/?headId=417a3d1a00197675f46fcd87493355a5&ckId=0p29l5x6b9jp7972ni15vtu6r02464vb&oldCkId=417a3d1a00197675f46fcd87493355a5&fkId=5a866b508dacd7910366b53d76e3b8d3&skId=5a866b508dacd7910366b53d76e3b8d3&sfrom=search_job_pc&key=python&currentPage={i}&scene=page'
            print(url)
            executor.submit(main,url)
    print("程序花费时间: ", time.time() - start_time)
