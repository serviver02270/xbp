for i in range(1,4): #コロンが入っていることに注意

    print(i,"人目") #タブでずらしていることに注意！

   
    #シャープは文字として認識されない。裏方メモとして使えるよ。
    
    #if文ここからーーーーーーーーーー

    name=input("名前を教えて下さい")
    waist=float(input("腹囲は？"))
    age=int(input("年齢は？（整数でね）"))

    #floatは実数、intは整数、「型違い」はあるある


    print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")


    if waist>=85 and age>=40:
        print(name,"さん、内臓脂肪蓄積注意です")
    else:
        if waist <=40:
            print(name,"さん、痩せすぎ。もっと食べい！")
        else:
            print(name,"さん、健康です。清濁併せ呑めい。")


