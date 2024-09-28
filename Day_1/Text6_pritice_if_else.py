import random
num=random.randint(1,10)
guess_num=int(input("请输入你要猜测的数字"))
if guess_num==num:
    print("恭喜你第一次就猜中了")
else:
    if guess_num>num:
        print("猜大了，请进行第二次猜测")
    else:
        print("猜小了，请进行第二次猜测")
    if int(input("请输入你要猜测的数字")==num):
        print("恭喜你第二次就猜中了")
    else:
        if guess_num>num:
            print("猜大了，请进行第三次猜测")
        else:
            print("猜小了，请进行第三次猜测")
    if int(input("请输入你要猜测的数字")==num):
        print("恭喜你第三次猜中了")
    else:
        if guess_num>num:
            print("猜大了，游戏结束")
        else:
            print("猜小了，游戏结束")
