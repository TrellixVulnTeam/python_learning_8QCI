# 能被4整除但是不能被100整除 或 能被400整除
year = int(input("输入一个年份："))

if (year % 4 ==0 and year % 100 !=0) or year % 400==0:
    print("是闰年")
else:
    print("不是闰年")