#双层if的嵌套使用
# if int(input("你的身高是多少："))>120:
#     print("身高超出限制，不可以免费")
#     print("但是vip级别大于3，可以免费")
#     if int(input("你的vip级别是多少"))>3:
#         print("恭喜你，vip等级达标，可以免费")
#     else:
#         print("Sorry,你需要买票10元")
# else:
#     print("欢迎小朋友免费游玩")

age=20
year=1
level=4
if age>=18:
    print("你是成年人")
    if age<30:
        print("你的年龄符合条件")
    if year>2:
        print("你的年龄和入职时间符合要求，可以领取礼品")
    elif level>3:
        print("你的年龄和等级符合要求，可以领取礼品")
    else:
        print("尽管年龄达标，但是入职时间和级别都不达标")
else:
    print("都不符合条件，无法领取礼品")
