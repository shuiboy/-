import os
def save_data(data, date):
    if not os.path.exists(r'2021_data_%s.csv' % date):
        with open("2021_data_%s.csv" % date, "a+", encoding='utf-8') as f:
            f.write("标题,热度,时间,url\n")
            for i in data:
                title = i["title"]
                extra = i["extra"]
                time = i['time']
                url = i["url"]
                row = '{},{},{},{}'.format(title,extra,time,url)
                f.write(row)
                f.write('\n')
    else:
        with open("2021_data_%s.csv" % date, "a+", encoding='utf-8') as f:
            for i in data:
                title = i["title"]
                extra = i["extra"]
                time = i['time']
                url = i["url"]
                row = '{},{},{},{}'.format(title,extra,time,url)
                f.write(row)
                f.write('\n')

