from sys import prefix


def say_hello():
    print("hello")
    #不写return None ,返回值自动还是return None

result=say_hello()
print(f"无返回值函数，返回的内容是：{result}")
print(f"无返回值函数，返回的内容类型是：{type(result)}")

def say_hello2():
    print("hello")
    return None
result=say_hello2()
print(f"无返回值函数，返回的内容是：{result}")
print(f"无返回值函数，返回的内容类型是：{type(result)}")

