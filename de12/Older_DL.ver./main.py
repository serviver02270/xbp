from utils_text_mining import text_mining
import importlib
importlib.reload(text_mining)

# 除外する単語の指定
stopwords = ["する", "ある", "あと", "いる", "いう", "なる", "思う", "言う", "できる",
             "ない","都","県","本名"
             
             
             
             ]
# 除外する頻出上位の指定
stop_n_top = 0

# 除外する頻出回数以下の指定
stop_min_freq = 3
# 除外するノードのエッジ数の指定
min_edge_frequency = 3

text_mining.create(stopwords, stop_n_top, stop_min_freq, min_edge_frequency)

