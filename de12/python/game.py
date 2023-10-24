import random

# プレイヤーに麻雀の手を当てさせるゲーム
def mahjong_guess_hand():
    # 雀頭と面子のセットを作成
    tiles = ["1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "1s", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "1m", "2m", "3m", "4m", "5m", "6m", "7m", "8m", "9m", "東", "南", "西", "北", "白", "発", "中"]
    
    # ランダムに雀頭と面子を選択
    head = random.choice(tiles)
    tiles.remove(head)
    melds = random.sample(tiles, 4)
    
    print("以下の麻雀の手を当ててください:")
    print("雀頭:", head)
    print("面子:", melds)

    # プレイヤーの入力を受け取り、正解を確認
    player_head = input("雀頭を入力してください: ")
    player_melds = input("面子をカンマ区切りで入力してください: ").split(", ")

    # 正解をチェック
    if player_head == head and set(player_melds) == set(melds):
        print("正解です！")
    else:
        print("不正解です。正解は:")
        print("雀頭:", head)
        print("面子:", melds)

if __name__ == "__main__":
    mahjong_guess_hand()