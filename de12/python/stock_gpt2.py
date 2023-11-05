import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# データを読み込む（例：AAPL株価データ）
data = pd.read_csv('AAPL.csv')  # データファイルのパスを指定

# 必要な特徴量を選択
data = data[['Open', 'High', 'Low', 'Volume', 'Adj Close']]

# 予測対象の特徴量を選択（例：Adj Closeを予測）
forecast_col = 'Adj Close'
data['label'] = data[forecast_col].shift(-1)

# 欠損値を削除
data = data.dropna()

# 特徴量とラベルを分割
X = np.array(data.drop(['label'], 1))
y = np.array(data['label'])

# データをトレーニングセットとテストセットに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 線形回帰モデルをトレーニング
clf = LinearRegression()
clf.fit(X_train, y_train)

# 未来の株価を予測
forecast_set = clf.predict(X_lately)

# 予測結果を表示
print(forecast_set)
