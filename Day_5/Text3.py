def odd_or_even(num_a,num_b):
    list1=list(range(num_a,num_b))
    for i in list1:
        if i%2==0:
            print(f"偶数：{i}")
        else:
            print(f"奇数：{i}")
odd_or_even(2,100)