import re
import time

import requests
import concurrent.futures
"""
2.请求数据
3.解析数据
4.保存数据

可以把每个功能单独的封装成一个一个函数, 一个函数只做一件事情
"""


def send_requests(url):
    """发送请求的函数"""
    response = requests.get(url)
    return response  # 返回响应体对象, 不是图片数据, 不是文字数据


def parse_data(data):
    """数据解析的方法, 传入数据进行解析"""
    result = re.findall('<img class="ui image lazy" data-original="(.*?)" src=".*?".*?</a>', data, re.S)
    return result  # 返回所有图片地址列表


def save_data(filename, img_data):
    """
    保存数据的方法
    :param filename: 文件名
    :param img_data: 图片数据
    :return: None
    """
    with open('img\\' + filename, mode='wb') as f:
        f.write(img_data)
        print('保存完成:', filename)


def main(url):
    """主函数, 依次调度其他函数的统一执行"""
    # 1. 调用发送请求的函数
    html_data = send_requests(url).text
    # 2. 调用数据解析的方法
    imgUrl_list = parse_data(html_data)

    for imgUrl in imgUrl_list:
        file_name = imgUrl.split('/')[-1]  # 文件名
        img_data = send_requests(imgUrl).content  # 图片数据

        # 3. 调用保存数据的函数
        save_data(file_name, img_data)





if __name__ == '__main__':

    # 后面池子模块用的非常多
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        for page in range(1, 11):  # 10页  主线程 + 所有子线程 = 11个任务
            url = f'https://fabiaoqing.com/biaoqing/lists/page/{page}.html'
            executor.submit(main, url)   # 提交的任务

    # 记录池子运行时间
    print("程序花费时间: ", time.time() - start_time)

