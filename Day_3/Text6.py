user="wangruoshui"
password=123456789

user1=input("请输入你的用户名")
password1=int(input("请输入你的密码"))
if user==user1 and password==password1:
    print("登陆成功")
elif user==user1 and password!=password1:
    print("密码错误")
else:
    print("用户名错误")
