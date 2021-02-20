import pandas as pd

importFilePath = r'pandas/import/'
importFileName = r'Trends_in_deaths.csv'
exportFilePath = r'pandas/export/'
exportFileName = r'data_result.csv'

def main():

# CSVファイルの読み込み
    readFile()

# 読み込んだCSVで加工・チェック等の処理
    check_rate()

#処理結果をOUTPUT
    outputFile()

def check_rate():
    
# Output用のDataframeを宣言する
    global df_deathRate_output
# Input用のDataframeを空で複製
    df_deathRate_output = pd.DataFrame().reindex_like(df_deathRate)
# Output用のDataFrameを初期化
    df_deathRate_output.drop(df_deathRate_output.index, inplace=True)

# loopの中で、やりたい処理を記述する
    for idx, ser in df_deathRate.iterrows():
        df_deathRate_output = df_deathRate_output.append(ser)
        continue

    print("check_rate completed")

def outputFile():

#CSVファイルへ書き出し
    df_deathRate_output.to_csv(exportFilePath + exportFileName)
    print("output completed")

def readFile():

# import用のDataframeを宣言
    global df_deathRate

# CSVファイルを読み込み
    df_deathRate = pd.read_csv(importFilePath + importFileName)

    print("readFile completed")

if __name__ == "__main__":
    
    main()