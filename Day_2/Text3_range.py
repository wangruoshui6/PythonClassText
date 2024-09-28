# #range语法1，range()num
# for x in range(10):
#     print(x)

#range语法2 range(num1,num2)
# for x in range(5,10):
#     print(x)

#range语法3 range(num1,num2,step)
# for x in range(1,10,2):
#     print("送王若水五朵玫瑰")

#求1-100（不包括100）之间有多少个偶数
count=0
for x in range(1,100):
    if x%2==0:
        count+=1
print(f"1-100之间有{count}个偶数")
