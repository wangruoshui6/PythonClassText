def fun_a():
    print("---2---")
def fun_b():
    print("---1---")
    fun_a()
    print("---3---")

fun_b()