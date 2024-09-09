
import time
import requests
import concurrent.futures


def send_requests(url):
    response = requests.get(url)
    return response


def parse_data(data):
    str = data['data']['object_list']
    strs = []
    if str[0]['photo']:
        for st in str:
            strs.append(st['photo']['path'])
    else:
        for st in str:
            strs.append(st['album']['covers'][0])
    return strs


def save_data(filename, img_data):
    with open('img\\' + filename, mode='wb') as f:
        f.write(img_data)
        print('保存完成:', filename)


def save_one_pic(img_url):
    file_name = img_url.split('/')[-1]  # 文件名
    img_data = send_requests(img_url).content  # 图片数据
    save_data(file_name, img_data)



def main(url):
    html_data = send_requests(url).json()
    imgUrl_list = parse_data(html_data)

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        for imgUrl in imgUrl_list:
            # print(imgUrl)
            executor.submit(save_one_pic, imgUrl)


if __name__ == '__main__':

    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        main('https://www.duitang.com/napi/blogv2/list/by_search/?kw=美女')
        for page in range(24, 1200, 24):
            url = f'https://www.duitang.com/napi/blogv2/list/by_search/?kw=美女&after_id={page}&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&_={int(time.time() * 1000)}]'
            # print(url)
            executor.submit(main,url)
    print("程序花费时间: ", time.time() - start_time)