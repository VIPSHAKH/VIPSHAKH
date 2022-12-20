# 4. Bo'shliq bilan ajratilgan ikkita satrdan bitta satr olish uchun Python dasturini yozing va har bir satrning dastlabki ikkita belgisini almashtiring.

satr=input()
satr=satr.split()
satr1=[]
satr2=[]
for i in satr[0]:
    satr1.append(i)
for i in satr[1]:
    satr2.append(i)
satr1[0],satr1[1]=satr1[1],satr1[0]
satr2[0],satr2[1]=satr2[1],satr2[0]
satr1.append(' ')
for i in satr1:
    print(i,end='')
for i in satr2:
    print(i,end='')