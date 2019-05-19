a=input()

b = int(a[:2])
c = int(a[2:])

if 0< b < 13:
    a_month_flag = 1
    a_year_flag = 1
elif b == 0:
    a_month_flag = 0
    a_year_flag = 0
else:
    a_month_flag = 0
    a_year_flag = 1

if 0< c < 13:
    b_month_flag = 1
    b_year_flag = 1
elif c == 0:
    b_month_flag = 0
    b_year_flag = 0
else:
    b_month_flag = 0
    b_year_flag = 1

if a_month_flag ==1 and b_month_flag==1:
    print("AMBIGUOUS")
elif a_month_flag == 1 and b_month_flag == 0:
    print("MMYY")
elif a_month_flag == 0 and b_month_flag ==1:
    print("YYMM")
else:
    print("NA")
