num=int(input())
def lap_year(num):
    if num%4==0 and num%100!=0:
        print("True")
    elif num%100==0 and num%400==0:
        print("True")
    else:
        print("False")
lap_year(num)