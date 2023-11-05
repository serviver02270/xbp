import datetime
import pandas_datareader.data as web

# 株価データを取得する関数
def get_stock_data(meigara_cd:str, from_date:str, to_date:str):


    from prophet import Prophet
    import pandas as pd
    from prophet.plot import plot_plotly
    import plotly.offline as py

# ==========================================================
# データ取得
# ==========================================================



# 引数情報
meigara_cd  = "6758"         # 銘柄コード
from_date   = "2023-01-01"   # 開始日
to_date     = "2024-06-01"   # 終了日

# 関数実行
data = get_stock_data(meigara_cd, from_date, to_date)

# Prophet投入用インプットデータ作成
df = pd.DataFrame({"ds": data.index, "y": data["Close"]}).reset_index(drop=True)

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
future = proph.make_future_dataframe(periods=365)  # 365日先の予測を追加

# 未来の予測を含むデータフレームで予測を行う
forecast = proph.predict(future)

# ==========================================================
# 予測（可視化）
# ==========================================================

py.init_notebook_mode()

figure = plot_plotly(proph, forecast)

# 出力
py.iplot(figure)
