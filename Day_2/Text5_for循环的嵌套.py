# #坚持100天，每天送十朵花
# for x in range(1,101):
#     print(f"今天是第{x}天给小美送玫瑰")
#     for i in range(1,11):
#         print(f"这个是第{x}天给小美送的第{i}朵玫瑰")
# print(f"在第{x}天表白成功")

#用while 和for之间的相互嵌套来完成
i=1
while i<100:
    print(f"今天是给小美表白的第{i}天")
    i+=1
    for x in range(1,11):
        print(f"第{i}天给小美送的第{x}朵玫瑰")
print(f"在第{i}天表白成功")