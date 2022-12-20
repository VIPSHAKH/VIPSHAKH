# 10. O’zbekcha so’zlardan iborat satr va K soni (0<K<10) berilgan. Satr o’ngga siljish orqali kodlovchi dastur tuzing. Ya’ni alfavitdagi harflar o’zidan K ta keying turgan harf bilan almashtiriladi. Tinish belgilar va probel o’zgarishsiz qolsin.
a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',' ',' ',' ',' ',' ',' ',' ',' ',' ','.','.','.','.','.','.','.','.','.','.']
b=input()
k=int(input())
l=[]
for i in b:
    d=a.index(i)
    l.append(a[d+k])
for i in l:
	print(i,end='')