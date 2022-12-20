# 9. Mijoz bankka B so’m pul qo’ydi. Bankdagi pulga yiliga M foiz ustama qo’shiladi. Necha yildan keyin mijozning puli A so’mdan oshishini aniqlovchi dastur tuzing.
B=int(input())
M=int(input())
A=int(input())
for i in range(1,1000):
    one_year=B/100*M
    if one_year*i>=A:
        print(i)
        break
