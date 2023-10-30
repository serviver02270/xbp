win=0
lose=0
draw=0

# ＝＝＝＝＝＝＝＝＝繰り返しはじめ＝＝＝＝＝＝＝＝＝＝＝＝＝

# 5回する
for i in range(1,6):
    print("==================== ",i,"回目 ====================")

# 1めくり目
    import random
    a = random.randint(1, 13)
    print(a,"が出ました。次のカードはこれよりhigh？low？")

# high? low?
    expect=input("小文字の英語で記入してください>>>")

# 2めくり目
    import random
    b = random.randint(1, 13)
    print(b,"が出ました。")

# 勝ちor負け
    if expect=="high" or "low" or "draw":
        if expect=="high" :
            if a>b :
                print("あなたの負けです(T~T )")
                lose=lose+1
            if a<b:
                print("あなたの勝ちです( ^_^)b")
                win=win+1
        if expect=="low" :
            if a>b :
                print("あなたの勝ちです( ^_^)b")
                win=win+1
            if a<b:
                print("あなたの負けです(T~T )")
                lose=lose+1
        if a==b :
            print("ドロー！( ◎_◎ )")
            draw=draw+1

# ＝＝＝＝＝＝＝＝＝繰り返しおわり＝＝＝＝＝＝＝＝＝＝＝＝＝

print("==================== Finished! ====================")
print("あなたが勝った回数は",win,"回!負けた回数は",lose,"回!ドローの回数は",draw,"回でした!Have a nice day!")
