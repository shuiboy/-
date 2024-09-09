"""
	- 课上的搜狗图片案例，先自己实现一遍, 构建查询参数请求数据
	- 将前三页的图片数据保存到文件夹里面
	    有错误需要解决报错<可以根据情况使用（异常捕获 + 请求参数）>
		
请在下方编写代码
https://pic.sogou.com/napi/pc/searchList?mode=1&start=48&xml_len=48&query=美女
"""
import os
import pprint
import requests

requests.packages.urllib3.disable_warnings()
if not os.path.exists('图片'):
    os.mkdir('图片')


def paramspage(page):
    params = {
        'mode': '1',
        'start': page,
        'xml_len': '48',
        'query': '美女'
    }
    return params


url = 'https://pic.sogou.com/napi/pc/searchList'
headers = {
    'Host': 'pic.sogou.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
nums = 0
for i in range(0, 300, 48):
    params = paramspage(i)
    response = requests.get(url=url, params=params, headers=headers)
    res_json = response.json()
    res_list = res_json['data']['items']
    print('===============================================================')

    for res in res_list:
        title = res['title']
        picUrl = res['picUrl']
        file_name = picUrl.split('/')[-1]
        # print(f'title:{title},picUrl:{picUrl},file_name:{file_name},')
        try:
            response2 = requests.get(picUrl, headers=headers, verify=False, timeout=1)
            data = response2.content
            with open('图片\\' + file_name, mode='wb') as f:
                f.write(data)
                nums += 1
                print(title, '下载完成！')
        except Exception as e:
            print(e)
    print('已爬取',nums,'张图片')

print('共爬取',nums,'张图片')
