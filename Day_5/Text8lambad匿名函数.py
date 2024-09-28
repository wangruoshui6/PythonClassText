
def text_func(compute):
    result=compute(1,2)
    print(f"结果是：{result}")
#这种写法比较繁琐，不合适
# def add (x,y):
#     return x+y
# text_func(add)

#lambad的主体是一个表达式，而不是代码块，仅仅
#能在lambad的表达式中封装有限的逻辑
#匿名函数用于临时构建一个函数，只能用一次的场景
#匿名函数的定义中，函数体只能写一行代码，
#如果函数体要写多行代码，不可用lambda匿名函数，应使用def定义带名字的函数
text_func(lambda x,y:x+y)


