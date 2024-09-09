"""
1. 采集网址 https://haokan.baidu.com/tab/gaoxiao_new

2. 采集目标
	- 采集当前页面, "时下热门" 里面的数据
	- 需要需要采集以下数据:
		title 视频标题
		duration 视频时长
		comment  评论数量
		fmplaycnt 播放量

    - 用正则表达式采集
"""

import requests
import re

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'BIDUPSID=871B5343601006A25DF883DB5FC8F24D; PSTM=1642380109; BAIDUID=871B5343601006A27A54D56E5753F52C:FG=1; __yjs_duid=1_bfbcc45f613b52c2cf7535cfc4f30dbc1642380234804; BDUSS=jc2REsyQ0VqM3Z5NnFTUHBIczdHYWlkSW5ZU1l2bkEtUzFibEhKUnNlSE52QXhpRVFBQUFBJCQAAAAAAAAAAAEAAADQaQhax-HH4bXYxq65~XNreQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM0v5WHNL-VhY; BDUSS_BFESS=jc2REsyQ0VqM3Z5NnFTUHBIczdHYWlkSW5ZU1l2bkEtUzFibEhKUnNlSE52QXhpRVFBQUFBJCQAAAAAAAAAAAEAAADQaQhax-HH4bXYxq65~XNreQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM0v5WHNL-VhY; BAIDUID_BFESS=2DA5989B0CE3285B0300DDA9CD2D7BE7:FG=1; delPer=0; BDPASSGATE=IlPT2AEptyoA_yiU4VKC3kIN8efjZrm4Ae3GSEpT3lStfCaWmhH3BrVMSEnHN-a8AiTM-Y3fo_-5kV8PQlxmicwdggYTpW-H7CG-zNSF5aTvL_NgzbIZCb4jQUZqqvzxkgl-zuEHQ49zBCstpBTbpuo4ivKl73JQb4r56kCygKrl_oGm2X8My88bOXVfYZ0APNu594rXnEpKLDm4Y3mtT9PecSIMR7QEy0u5n0MG2hPT7SUsJefjWMQFDpaJA72AX4WPS3ytu1Gs_EoS68xuSkIx-ESI5uDxN5-Q2LbpfK; H_WISE_SIDS=107314_110085_127969_131862_164870_174441_179349_184716_185239_185268_185638_186635_188332_188842_189034_189094_189326_189755_189802_191068_191253_191287_192206_192407_192957_193284_193291_193557_194085_194511_195003_195187_195342_196045_196428_197242_197286_197472_197711_197783_197831_197955_198034_198071_198080_198265_198393_198514_198650_198929_199082_199157_199276_199469_199583_199642_199752_199797_200034_200127_200193_200275_200450_200490_200530_200553_200577_200744_200968_201054_201232_201328_201361_201444_201533_201705_201729_201734_201914_201947_201972_201979_202115_202146_202177_202234_202554_202561; SE_LAUNCH=5%3A1643081470; PSINO=2; PC_TAB_LOG=video_details_page; COMMON_LID=ed8049b046727394d138ded8c9149582; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1642742025,1642742083,1642751465,1643082119; BDRCVFR[0idcJUX_hP6]=mk3SLVN4HKm; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ariaDefaultTheme=default; ariaReadtype=1; ariaStatus=false; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=31253_26350; BA_HECTOR=2001208484a100245o1guvbou0r; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1643098741; ab_sr=1.0.1_MzdiN2JjZTI5MzQ3OGUwYzI1ZGYzODBlYWFmN2EwZWQ3ZTNlZjU5NzI2MGNiOWI4YmEyYmE0ZmMzYWY2NGRjMDRiNmZkMTZmMmQxY2RkOGU5MWMyMTc2YzM4YTYxZjU5; reptileData=%7B%22data%22%3A%227518d16f65155518a9ad73e1bc5100a901e5c70c32198b55358a86bae4321ee81a8ed0463a0cf93df76dbdd843d3b15ca1df929d4b18a2fc77ecdc89bfcfefafcc2b3943957d0a7b26857ec4db404a3bfd7843e7942d8e9af1531b3f4e876153%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%22d184671c%22%7D; RT="z=1&dm=baidu.com&si=1vy79pqk1xm&ss=kytuj6ks&sl=4&tt=2ad&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=19jj"',
    'pragma': 'no-cache',
    'referer': 'https://haokan.baidu.com/tab/gaoxiao_new',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}
req = requests.get(
    url='https://haokan.baidu.com/web/video/feed?tab=gaoxiao_new&act=pcFeed&pd=pc&num=100&shuaxin_id=1643098741322',
    headers=headers)


req_j = req.json()
req_data = str(req_j)
tihuan = "\{'id': '.*?', 'title': '(.*?)',.*?'duration': '(.*?)', .*?'comment': '(.*?)', .*?'fmplaycnt': '(.*?)',.*?\}"
num = 0
title = re.findall(tihuan, req_data, re.S)
for it in title:
    num += 1
    print(f'{num}.视频标题:{it[0]},视频时长:{it[1]},评论数量:{it[2]},播放量:{it[3]}.')
