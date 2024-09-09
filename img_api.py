import base64
from constants import KUAI_USERNAME, KUAI_PASSWORD
import requests
# 一、图片文字类型(默认 3 数英混合)：
# 1 : 纯数字
# 1001：纯数字2
# 2 : 纯英文
# 1002：纯英文2
# 3 : 数英混合
# 1003：数英混合2
#  4 : 闪动GIF
# 7 : 无感学习(独家)
# 11 : 计算题
# 1005:  快速计算题
# 16 : 汉字
# 32 : 通用文字识别(证件、单据)
# 66:  问答题
# 49 :recaptcha图片识别
# 二、图片旋转角度类型：
# 29 :  旋转类型
#
# 三、图片坐标点选类型：
# 19 :  1个坐标
# 20 :  3个坐标
# 21 :  3 ~ 5个坐标
# 22 :  5 ~ 8个坐标
# 27 :  1 ~ 4个坐标
# 48 : 轨迹类型
#
# 四、缺口识别
# 18 : 缺口识别（需要2张图 一张目标图一张缺口图）
# 33 : 单缺口识别（返回X轴坐标 只需要1张图）
# 五、拼图识别
# 53：拼图识别

# 定义一个函数, 把你的用户名,密码 和图片路径传递进去
def base64_api(img):
    # 打开图片图片, 把图片转换成字符串形式
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": KUAI_USERNAME, "password": KUAI_PASSWORD, "typeid": 1003, "image": b64}
    result = requests.post("http://api.ttshitu.com/predict", data=data).json()
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]



if __name__ == "__main__":
    img_path = "validateCodeServlet.png"
    result = base64_api(img=img_path)
    print(result)

"""
接口更新了
"""
