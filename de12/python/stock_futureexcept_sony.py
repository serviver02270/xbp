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



 #---------コード1----------   


# ==========================================================
# 関数実行
# ==========================================================

# 引数情報
meigara_cd  = "6758"         # Sony銘柄
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





#-------チャート分析のコード-----------

import matplotlib.pyplot as plt

# ==========================================================
# データ取得
# ==========================================================

# 引数情報
meigara_cd  = "6758"         # Sony銘柄
from_date   = "2023-01-01"   # 開始日
to_date     = "2024-06-01"      # 終了日

# 関数実行
data = get_stock_data(meigara_cd,from_date,to_date)


# ==========================================================
# グラフ可視化
# ==========================================================

# グラフ描画
plt.plot_date(data.index, data["Close"], linestyle='solid')

# 書式設定
plt.xlabel("Date")            # X軸ラベル
plt.ylabel("Stock")           # Y軸ラベル
plt.gcf().autofmt_xdate()     # X軸値を45度回転
plt.show()                    # グラフ表示


#--------時系列モデル作成予想コード----------



from prophet import Prophet
import pandas as pd
from prophet.plot import plot_plotly
import plotly.offline as py

# ==========================================================
# データ取得
# ==========================================================

# 引数情報
meigara_cd  = "6758"         # <-ここに銘柄コード四桁を入れましょう
from_date   = "2023-01-01"   # <-開始日（チャートの一番左端の日を設定しましょう）
to_date     = "2024-06-01"    # 終了日（ここにチャートの右端の日を設定しましょう）



# 関数実行
data = get_stock_data(meigara_cd,from_date,to_date)

# Prophet投入用インプットデータ作成
df = pd.DataFrame({"ds":data.index, "y":data["Close"]}).reset_index(drop=True)

# ==========================================================
# 時系列モデル作成
# ==========================================================

# モデルインスタンス
proph = Prophet()

# モデル学習
proph.fit(df)

# ==========================================================
# 予測
# ==========================================================

# 未来予測用のデータフレーム
future = proph.make_future_dataframe(periods=365)

# 時系列を予測
forecast = proph.predict(future)

# ==========================================================
# 予測（可視化）
# ==========================================================

py.init_notebook_mode()

figure = plot_plotly(proph,      # 時系列モデル
                     forecast,   # 予測結果
                    )

# 出力
py.iplot(figure)

