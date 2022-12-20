# 7-topshiriq: ax^2 + bx + c = 0 kvadrat tenglama nechta yechimga ega ekanligini hisoblaydigan dastur yozing. a, b va c o'zgaruvchilarini standart input orqali qabul qiling. 
a=int(input())
b=int(input())
c=int(input())
yechim=0
for x in range(1,1000):
    x=int(x)
    if a*x**2+b*x+c==0:
        yechim+=1
for x in range(-1000,-1):
    x=int(x)
    if a*x**2+b*x+c==0:
        yechim+=1
print(yechim)

