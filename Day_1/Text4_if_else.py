'''print("欢迎来到黑马动物园")
heigh=int(input("请输入你的身高"))
if heigh>120:
    print("您的身高超出120cm，游玩需要购票10元")
else:
    print("您的身高未超出120cm，可以免费游玩")
print("祝您游玩愉快")'''

num=5
if int(input("请猜第一个数字："))==num:
    print("恭喜你第一次就猜对了")
elif int(input("猜错了，再猜一次"))==num:
    print("猜对了")
elif int(input("猜错了，再猜一次")) == num:
    print("恭喜，最后一次机会你猜对了")
else:
    print("垃圾，三次机会都没猜对")