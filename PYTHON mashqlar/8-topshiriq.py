# 8. Farangeytdagi haroratni Selsiyga va selsiydagi haroratni farangeytga aylantirib beradigan uchun Python dasturini yozing. [Formula: c  = 5*(f-32)/9 [bu erda c = selsiydagi harorat va f = fahrenhaytdagi harorat]

harorat=input()
harorat=harorat.split()
harorat[0]=int(harorat[0])
if harorat[1]=='C' or harorat[1]=='c':
    print(9/5*harorat[0]+32)
elif harorat[1]=='F' or harorat[1]=='f':
    print(5*(harorat[0]-32)/9)