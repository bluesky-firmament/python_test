import datetime
import pandas as pd

all_df = pd.DataFrame()
columns = ('時分 現地気圧 海面気圧 降水量 気温 相対湿度 平均風速 平均風向 '
           '最大瞬間風速 最大瞬間風向 日照時間').split()

for year in range(2015, 2017): # 2015 ... 2016
    for month in range(5, 6): # 1 ... 12
        for day in range(1, 7): # 1 ... 31

            try:
                d = datetime.datetime(year, month, day)
            except ValueError:
                continue # incorrect date; e.g., 2007/2/31 etc.

            print(d) # this day
            #time.sleep(1) # wait for 1 sec
            url = 'http://www.data.jma.go.jp/obd/stats/etrn/upper/view/daily_uwd.php?year={d.year}&month={d.month}&day={d.day}&hour=9&atm=&point=47418&view='
            #url = 'http://www.data.jma.go.jp/obd/stats/etrn/view/10min_s1.php?' \
                 #f'prec_no=44&block_no=47662&year={d.year}&month={d.month}&day={d.day}'

            try:
                df = pd.read_html(url,
                                  # NaN: http://www.data.jma.go.jp/obd/stats/data/mdrr/man/remark.html
                                  na_values=['--', '///', '#', '×'],
                                  skiprows=2)[0]
            except HTTPError:
                continue # in case of 404

            df.columns = columns
            df.index = d + pd.to_timedelta(df.時分 + ':00')
            df.index.name = 'JST'

            all_df = all_df.append(df)

all_df.to_excel('wind_data.xlsx')
all_df.to_csv('wind_data.csv')
