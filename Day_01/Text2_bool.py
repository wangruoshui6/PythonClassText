num1=10
num2=10
print(f"10=10的结果是{num1==num2}")
#‌在Python中，print函数使用f前缀是因为它表示这是一个格式化字符串（f-string）
# 。‌ f-string是Python 3.6及以上版本引入的一种新的字符串格式化方法，
# 它允许在字符串中直接嵌入表达式，使得字符串格式化更加直观和方便。

#使用f-string可以让你在字符串中直接引用变量，并使用{}来表示这些变量的位置
name="zhangsan"
age=19
print(f"法外狂徒的名字是{name},年龄是{age}")