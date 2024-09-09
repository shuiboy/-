import csv

import requests


# http://http.py.cn/ucenter/info/     手机号     名789

def huoqu():
    proxy_url = 'http://tiqu.pyhttp.taolop.com/getip?count=1&neek=23100&type=2&yys=0&port=1&sb=&mr=2&sep=0'
    proxy_data = requests.get(url=proxy_url).json()
    proxy_1 = proxy_data["data"][0]['ip'] + ':' + str(proxy_data['data'][0]['port'])
    return proxy_1


if __name__ == '__main__':
    proxy_data = huoqu()

    proxies = {
        "http": "http://" + proxy_data,
        "https": "https://" + proxy_data,
    }
    with open('proxy.csv', mode='a', encoding='utf-8',newline='') as f:
        csv_w = csv.writer(f)
        csv_w.writerow([proxy_data])
    print(proxies)
    # response = requests.get(url='http://httpbin.org/ip', proxies=proxies,verify=False)
    response = requests.get(url='http://ip.xpcha.com/myip.php', proxies=proxies, verify=False)
    response.encoding = 'utf-8'
    print(response.text)
