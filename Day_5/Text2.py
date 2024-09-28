def day_income(unit_price,table_count):
    sum1=0

    for i in table_count:
        sum1=sum(table_count)
    print(f"今日的销售额为{sum1*unit_price}")
    print(f"今日所卖的荤素菜的总质量为{sum1}")




day_income(10,[12,9.7,10,7,6,11,9,8,11])

