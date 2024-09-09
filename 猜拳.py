import random


def suijishu():
    return random.randint(1, 3)


def caiquan(a):
    if a == 1:
        cai = '剪刀'
    elif a == 2:
        cai = '布'
    else:
        cai = '石头'
    return cai


def panduan(jia, yi):
    if jia == yi:
        print('平了')
    else:
        if jia == '剪刀' and yi == '布' or jia == '布' and yi == '石头' or jia == '石头' and yi == '剪刀':
            print('你胜了')
        else:
            print('电脑胜')



yonghu = int(input('请输入1-3，分别代表：1、剪刀，2、布，3、石头：'))

print('你输入的数字是：', yonghu,'出的是：',caiquan(yonghu))
jia=caiquan(yonghu)
yi = caiquan(suijishu())
print('电脑出的是：',yi)
panduan(jia,yi)
