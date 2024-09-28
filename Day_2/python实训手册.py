# x=float(input("请输入长方形的长"))
# y=float(input("请输入长方形的宽"))
# print("长方形的面积为",x*y)
# for i in range(0,33):
#     print("*",end="")
# print()
# print("欢迎来到“河北石油职业技术大学！")
# for j in range(0,33):
#     print("*",end="")
from pickle import PROTO

# name=input("请输入你的姓名")
# # math=int(input("请输入你的高数成绩"))
# # English=int(input("请输入你的英语成绩"))
# # sum=math+English
# # print(f"姓名：{name},两门成绩之和为{sum}");
# # print("d");print("ff")
# print('what\\'s happened to you?")
# print("What's happened to you?")
# print('What's happened to you?')
# # print(""oh!" it sounds terrible)
# numvalue=10
# print(numvalue)
# number=10
# str_number=str(number)
# # print(type(str_number))
# print("编号\t","星期")
# print("0     \t星期日\n"
#       "1     \t星期一\n"
#       "2     \t星期二\n"
#       "3     \t星期三\n"
#       "4     \t星期四\n"
#       "5     \t星期五\n"
#       "6     \t星期六\n")
# x=input("今天是星期几")
# z=input("经过多少天后？")
# str1=("星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六,"
#       ,"星期日","星期一", "星期二", "星期三", "星期四", "星期五", "星期六,")
# # d=int(z)%7
# # x=int(x)
# # print(f"今天是星期{x},经过{z}天后是",str1[x+d])
# x1=95;x2=68;x3=77;x4=83;x5=91
# G=(x1*x2*x3*x4*x5)**(1/5)
# print(G)
# LIST=[1,2,3,4,5]
# print(list.tail())
# list1=[1,2,3,4,57]
# for i in list1:
#     print(i)
# list1=[1,2,5,7,9]
# for i,item in enumerate(list1):
#     print(f"索引{i}的元素是{item}")

def pascal_triangle(rows):
    triangle = [[1] * i for i in range(1, rows + 1)]
    for r in range(1, rows):
        for i in range(1, r):
            triangle[r][i] = triangle[r - 1][i - 1] + triangle[r - 1][i]
    return triangle


rows = 10
triangle = pascal_triangle(rows)
for row in triangle:
    print(row)