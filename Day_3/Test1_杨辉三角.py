def yanghui(t):
    #打印第一行和第二行
    print([1])
    line=[1,1]
    print(line)
    #打印第三行开始的其他行
    for i in range(2,t):
        #清空r,因为line变了，r=line[i]+line[i+1]
        r=[]
        #按规律生成该行除两端以外的数字
        for i in range(0,len(line)-1):
            r.append(line[i]+line[i+1])
            #把两端的数字连上
        line=[1]+r+[1]
        print(line)
yanghui(10)
