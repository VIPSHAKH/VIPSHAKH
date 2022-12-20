# 5. Ikki xonali nisbiy-simmetrik sonlarning eng katta umumiy bo’luvchisi 1 dan kattalarini chop etuvchi dastur tuzing. (masalan nisbiy-simmetrik sonlar 23 va 32, 81 va 18)
import math
def nisbiysimmetrik(n):
    n=str(n)
    n=n[::-1]
    return n

ekub=0
nisbiy_simmetrik=[]
for i in range(10,100):
    if nisbiysimmetrik(i) in nisbiy_simmetrik or i in nisbiy_simmetrik:
        break
    else:
        if i>10 and int(nisbiysimmetrik(i))>10:
            nisbiy_simmetrik.append(i)
            nisbiy_simmetrik.append(nisbiysimmetrik(i))
for i in range(len(nisbiy_simmetrik)):
    nisbiy_simmetrik[i]=str(nisbiy_simmetrik[i])
for i in range(0,len(nisbiy_simmetrik),2):
    ekub=math.gcd(int(nisbiy_simmetrik[i]),int(nisbiy_simmetrik[i+1]))
    if ekub>1:
        print(nisbiy_simmetrik[i],'-',nisbiy_simmetrik[i+1], end=', ')


