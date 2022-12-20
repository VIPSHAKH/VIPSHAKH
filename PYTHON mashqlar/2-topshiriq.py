# 2. Standar input orqali son qabul qiling, agar bu son 3ga qoldiqsiz bo'linsa ekranga "Fiz", 5ga qoldiqsiz bo'linsa "Buzz", ham 5ga ham 3ga qoldiqsiz bo'linsa "FizBuzz" ni ekranga chiqaring. Agar son hech qaysi shartni bajarmasa sonni o'zini ekranga chiqaring. 

son=int(input())
if son%3==0 and son%5==0:
    print('FizBuzz')
elif son%5==0:
    print('Buzz')
elif son%3==0:
    print('Fiz')
else: print(son)