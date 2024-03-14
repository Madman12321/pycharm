month = int(input())
day = int(input())
if month <= 12 and day <= 28:
    print("valid date")
elif month == 1 and day <= 31:
    print("valid date")
elif month == 2 and day == 29:
    print("valid date")
elif month == 3 and day <= 31:
    print("valid date")
elif month == 4 and day <= 30:
    print("valid date")
elif month == 5 and day <= 31:
    print("valid date")
elif month == 6 and day <= 30:
    print("valid date")
elif month == 7 and day <= 31:
    print("valid date")
elif month == 8 and day <= 31:
    print("valid date")
elif month == 9 and day <= 30:
    print("valid date")
elif month == 10 and day <= 31:
    print("valid date")
elif month == 11 and day <= 30:
    print("valid date")
elif month == 12 and day <= 31:
    print("valid date")
elif month != range(1, 13) and day != range(1, 28):
    print("not valid date")