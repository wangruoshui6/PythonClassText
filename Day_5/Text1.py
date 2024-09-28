def su(n):
    sum=0
    sum1=0
    for i in range(1,n):
        sum+=i
        sum1+=sum
    print(sum)
    print(sum1)
su(10)