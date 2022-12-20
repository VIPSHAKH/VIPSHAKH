# 1. Standart input orqali vergul bilan ajratilgan sonlarni o'qing va u yerda nechta son qatnashganini ekranga chiqaring (takrorlanishlar inobatga olinmasin). 
# Misollar:
# Input: 2,3,3,4 
# Natija: 3 

son=input()
son=son.split(',')
necha=[]
for i in son:
    if i in son and not(i in necha):
        necha.append(i)
print(len(necha))