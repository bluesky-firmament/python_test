# https://pandas.pydata.org/pandas-docs/stable/io.html#io-read-html
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_html.html
# pip install lxml html5lib beautifulsoup4

import datetime
import pandas as pd

for year in range(2000, 2019): # 2015 ... 2016
    for month in range(5, 6): # 1 ... 12
        for day in range(1, 7): # 1 ... 31
            url = 'http://www.data.jma.go.jp/obd/stats/etrn/upper/view/daily_uwd.php?year=' + str(year)+'&month=' +str(month)+'&day='+str(day)+'&hour=9&atm=&point=47918&view='
            #url = 'http://www.data.jma.go.jp/obd/stats/etrn/upper/view/daily_uwd.php?year=2015&month=5&day=1&hour=9&atm=&point=47418&view='
            print(url)
            dfs = pd.read_html(url)
            #print(len(dfs))# 1
            print(dfs[0])
            dfs[0].to_csv('data/'+str(year)+'_'+str(month)+'_'+str(day)+'hour=9_wind.csv')
