#传入的是代码的执行逻辑
def test_func(compute):
    result=compute(1,2)
    print(f"compute参数的类型是：{type(compute)}")
    print(f"计算结果为{result}")

def compute(x,y):
    return x+y
test_func(compute)

#传入的是数据
# def add(x,y):
#     return x+y