def gs():
    height = 80.0
    sum =80
    for i in range(2,11):
        sum+=(height/2)*2
        height/=2
    print(f"在第{i}次落地时共经过了{sum}米")
    print(f"第{i}次反弹有{height}高")


gs()


