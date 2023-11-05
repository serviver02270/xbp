import datetime
import pandas_datareader.data as web

# 株価データを取得する関数
def get_stock_data(meigara_cd:str, from_date:str, to_date:str):
    
    """
    ====================================================
    引数情報
    ・meigara_cd(str): 銘柄コード
    ・from_date(str):  株価取得期間（開始日）
    ・to_date(str):    株価取得期間（終了日）
    ====================================================
    """

    # 株価データを取得
    df = web.DataReader(name        = meigara_cd + ".jp",  # 銘柄コード 
                        data_source = 'stooq',             # 株価データソース
                        start       = from_date,           # 株価取得期間（開始日）
                        end         = to_date,             # 株価取得期間（終了日）
                       )
    
    return df

# 本日日付を取得する関数
def today() -> str:
    return str(datetime.date.today())
    # ==========================================================
# 関数実行
# ==========================================================

# 引数情報
meigara_cd  = "7974"         # <<任天堂>>　銘柄
from_date   = "2023-01-01"   # 開始日
to_date     = today()        # 終了日

# 関数実行
data = get_stock_data(meigara_cd,from_date,to_date)


# ==========================================================
# 結果確認
# ==========================================================

# 出力
print(data)

# 出力イメージ
#              Open   High    Low  Close   Volume
# Date                                           
# 2023-08-17  12000  12140  11920  12130  2960800
# 2023-08-16  12200  12205  12010  12010  3069300
# 2023-08-15  12285  12320  12195  12220  3326700
# 2023-08-14  12415  12490  12075  12175  6287400
# 2023-08-10  12385  12635  12115  12565  7794900

import matplotlib.pyplot as plt

# ==========================================================
# データ取得
# ==========================================================

# 引数情報
meigara_cd  = "7974"         # 京都のおもちゃ屋さんから世界規模へ<任天堂>　銘柄
from_date   = "2023-01-01"   # 開始日
to_date     = today()        # 終了日

# 関数実行
data = get_stock_data(meigara_cd,from_date,to_date)

# ==========================================================
# グラフ可視化
# ==========================================================

# グラフ描画
plt.plot_date(data.index, data["Close"], linestyle='solid')

# 書式設定
plt.xlabel("Date")            # X軸ラベル
plt.ylabel("Stock(yen)")           # Y軸ラベル
plt.gcf().autofmt_xdate()     # X軸値を45度回転
plt.show()                    # グラフ表示
