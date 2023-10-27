for i in range(1,10): #コロンが入っていることに注意

    print(i,"回目")
    import random
    a = random.randint(50, 100)
    b = random.randint(50, 100)
    c = random.randint(50, 100)
    print(a, " ＋", b, "＋", c)
    Answer=int(input("いくら？"))

    if Answer == a+b+c:
        print("<<<<!!!やるやん正解!!!>>>>")
    else :    
        print("<<<<!!!ブブー!!!>>>>")
