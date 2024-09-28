def user_info(name,age,gender):
    print(f"姓名是{name},年龄是：{age},性别是{gender}")
user_info('小明',20,'男')
#关键字参数
user_info(name='小王',age=11,gender='女')
user_info(age=10,gender='女',name="xiaoxiao")
user_info('tiantian',gender='女',age=9)

#缺省参数
#注意：默认参数必须写到最后面，不然的话会出现报错
def user_info1(name,age,gender='男'):
    print(f"姓名是{name},年龄是：{age},性别是{gender}")
#不传递参数，默认有，
user_info1('小天',13)
#你要是传参的话可以完成参数的覆盖
user_info1('小天',13,'女')

