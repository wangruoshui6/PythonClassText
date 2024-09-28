def fuck():
    num=100
    print(num)
fuck()
# print(num),局部变量不能在函数体之外被调用

#全局变量
# num=100
# def test_a():
#     print(f"test_a:{num}")
# def test_b():
#     print(f"text_b:{num}")
# test_a()
# test_b()

#在函数内部修改全局变量
# num=100
# def test_a():
#     print(f"test_a:{num}")
# def test_b():
#     num=500
#     print(f"text_b:{num}")
# test_a()
# test_b()
# print(num)

#global关键字，在函数内声明变量为全局变量

num=100
def test_a():
    print(f"test_a:{num}")
def test_b():
    global num
    num=500
    print(f"text_b:{num}")
test_a()
test_b()
print(num)



