import pandas as pd
count = 0
for year in range(2000, 2019): # 2015 ... 2016
    for month in range(5, 6): # 1 ... 12
        for day in range(1, 7): # 1 ... 31

            csv_input = pd.read_csv(filepath_or_buffer='data/'+str(year)+'_'+str(month)+'_'+str(day)+'hour=9_wind.csv',index_col = 0,encoding="UTF-8", sep=",")
            #csv_file = open('data/'+str(year)+'_'+str(month)+'_'+str(day)+'hour=9_wind.csv', "r", encoding="UTF-8", errors="", newline="" )
            # インプットの項目数（行数 * カラム数）を返却します。
            # 指定したカラムだけ抽出したDataFrameオブジェクトを返却します。
            #header = next(csv_file)
            #print(csv_input)
            #for row in csv_file:
            #    print(row[4:7])
            #print(csv_input[["1","2"]])
            wind_velocity = csv_input[["2"]]

            if(count == 0):
                df = csv_input[["1"]]
                df2 = csv_input[["2"]]
                df = df.drop(0,axis = 0)
                df2 = df2.drop(0,axis = 0)
                avg_altitude = df
                avg_velocity = df2
                #print(avg_altitude)
                count = count + 1
            else:

                #print(avg_altitude)
                df = csv_input[["1"]]
                df2 = csv_input[["2"]]
                df = df.drop(0,axis = 0)
                df2 = df2.drop(0,axis = 0)

                #avg_altitude = avg_altitude.append(df)
                altitude = pd.concat([avg_altitude,df], axis = 1)
                velocity = pd.concat([avg_velocity,df2], axis = 1)
                #print(df)
                #avg_altitude = avg_altitude.fillna(0)
                #print(altitude)
                avg_altitude = altitude
                avg_velocity = velocity
                #avg_altitude = altitude.mean(axis = '1',numeric_only=True)
                #print(avg_altitude)
                count = count + 1
            print(count)
print(count)
print(wind_velocity)
altitude.to_csv('altitude_wind.csv')
velocity.to_csv('velocity_wind.csv')
altitude = altitude.applymap(type)
#altitude = altitude.dtype(float32)
#avg_altitude = altitude.mean(axis = 1)
print(avg_altitude)
