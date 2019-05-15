import pandas as pd
for year in range(2000, 2019): # 2015 ... 2016
    for month in range(5, 6): # 1 ... 12
        for day in range(1, 7): # 1 ... 31
            csv_input = pd.read_csv(filepath_or_buffer='data/'+str(year)+'_'+str(month)+'_'+str(day)+'hour=9_wind.csv', encoding="UTF-8", sep=",")
            # インプットの項目数（行数 * カラム数）を返却します。
            print(csv_input.size)
            # 指定したカラムだけ抽出したDataFrameオブジェクトを返却します。
            print(csv_input[["1", "2"]])
