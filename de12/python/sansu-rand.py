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

#時間制限のコピペーーーーーーーーーーー

import time
import timeout_decorator


def long_function(i):
    time.sleep(4)
    return i


class time_limit_class:
    def __init__(self):
        self.result = 0

    @timeout_decorator.timeout(5)
    def main(self):
        for i in range(10):
            self.result = long_function(i)
        return self.result

    def timeout(self):
        return self.result


if __name__ == "__main__":
    time_limit = time_limit_class()
    try:
        print(time_limit.main())
    except:
        print(time_limit.timeout())
