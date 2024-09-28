
#传进的所有参数都会被args变量收集，
#它会根据传进参数的位置合并成为一个元组，args是元组类型，这就是位置传递
def user_info(*args):
    print(f"args参数的类型是{type(args)},内容是{args}")
user_info('tom')
user_info('tom',18)

#关键字传递
#参数是"键=值"形式的情况下，所有的“键=值”都会被kwargs接收
#同时会根据“键=值”组成字典
#kw key-word的意思
def user_info11(**kwargs):
    print(f"args参数的类型是{type(kwargs)},内容是{kwargs}")
user_info11(name='Tom',age=18,id=100000)