import random

cash = 10000
for i in range(1, 21):
    scores = random.randint(1, 10)
    if scores < 5:
        print(f"员工{i}的绩效分{scores},不满足，不发工资，下一位")
        continue

    if cash >= 1000:
        cash -= 1000
        print(f"第{i}个员工的绩效分为{scores},发放工资一千元，公司所剩余额{cash}")
    else:
        print(f"第{i}位员工绩效分不足，不发放工资，公司余额还剩{cash}")
        break
