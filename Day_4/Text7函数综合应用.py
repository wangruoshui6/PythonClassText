money = 5000000

#要求客户输入姓名
name = input("请输入你的姓名")


#定义查询函数
def research(show):
    if show:
        print("-------查询结果--------")
    print(f"{name}你好，您的余额剩余{money}")


#定义存款函数
def saying():
    num = int(input("请输入你要存款的金额"))
    global money
    money += num


def earn():
    num = int(input("请输入你要取款的金额"))
    global money
    money -= num


#定义主菜单函数
def main():
    print(f"{name}，你好欢迎来到中国银行ATM机，请选择操作")
    print('查询余额\t\t [输入1]')
    print('存款\t\t[输入2]')
    print('取款\t\t[输入3]')
    print('退出\t\t[输入4]')

    return int(input("请输入您的选择"))


#设置无限循环，确保程序不退出
while True:
    x = main()
    if x == 1:
        research(True)
        continue
    elif x == 2:
        saying()
        research(False)
        continue
    elif x == 3:
        earn()
        research(False)
        continue
    else:
        print("程序退出")
        break
