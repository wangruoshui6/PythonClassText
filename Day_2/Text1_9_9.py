print("hello",end="")
print("world",end="")#不换行
print("hello\tworld")#对齐
print("wangruoshui\t handsome")
i=1
while i<=9:
    j=1
    while j<=i:
        print(f"{j}*{i}={j*i}\t",end="")
        j+=1
    i+=1
    print()



