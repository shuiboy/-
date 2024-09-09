import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import requests
import parsel

headers = {
    # 'Cookie': '__uuid=1645516962750.98; __tlog=1645516962775.27%7C00000000%7C00000000%7C00000000%7C00000000; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1645516963; __gc_id=928a9b57bd6e4d538ed74add39fa2a96; __s_bid=01b7b2d273faff9d39e1e194ef8f9ec7f53d; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1645517289; __session_seq=11; __uv_seq=11',
    'Host': 'monitor.liepin.com',
    'Origin': 'https://www.liepin.com',
    'Referer': 'https://www.liepin.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
}
driver = webdriver.Chrome()
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => false
    })
  """
})
url = 'https://www.liepin.com/zhaopin/?key=python'
data_all = driver.get(url=url)
driver.maximize_window()
driver.implicitly_wait(6)
liebiao = driver.find_elements(By.CSS_SELECTOR, 'div.left-list-box>ul>li')
with open('liepin.csv', mode='a', encoding='utf-8', newline='') as f:
    csv_w = csv.writer(f)
    csv_w.writerow(['名称', '地点', '薪资', '要求', '公司名称', '公司领域', '公司规模', '联系人', '联系人职务'])
for li in liebiao:
    title = li.find_element(By.CSS_SELECTOR,'.job-title-box>div').text
    didian = li.find_element(By.CSS_SELECTOR,'.job-dq-box>span:nth-child(2)').text
    xinzi = li.find_element(By.CSS_SELECTOR,'.job-salary').text
    yaoqius = li.find_elements(By.CSS_SELECTOR,'.job-labels-box>span')
    gongsi = li.find_element(By.CSS_SELECTOR,'.company-name.ellipsis-1').text
    lingyu = li.find_element(By.CSS_SELECTOR,'.company-tags-box.ellipsis-1>span:nth-child(1)').text
    guimo = li.find_element(By.CSS_SELECTOR,'.company-tags-box.ellipsis-1>span:nth-child(2)').text
    lianxiren = li.find_element(By.CSS_SELECTOR,'.recruiter-name.ellipsis-1').text
    lxrzw = li.find_element(By.CSS_SELECTOR,'.recruiter-title.ellipsis-1').text
    yaoqiu=[]
    for yq in yaoqius:
        y = yq.text
        yaoqiu.append(y)
    yaoqiu = ",".join(str(x) for x in yaoqiu)
    print(title,didian,xinzi,yaoqiu,gongsi,lingyu,guimo,lianxiren,lxrzw)

    with open('liepin.csv',mode='a',encoding='utf-8',newline='') as f:
        csv_w = csv.writer(f)
        csv_w.writerow([title,didian,xinzi,yaoqiu,gongsi,lingyu,guimo,lianxiren,lxrzw])

time.sleep(3)


driver.quit()