# 6. x,y haqiqiy sonlar berilgan. Agar x va y manfiy bo’lsa, ularning har birini kvadratlari bilan almashtiring: agar faqat bittasi manfiy bo’lsa, ikkala sonning har birini ularning o’rta arifmetigiga almashtiring, agar ikkalasi ham musbat bo’lsa o’zgarishlarsiz qoldiring.
x=int(input())
y=int(input())
if x<0 and y<0:
    x**=2
    y**=2
elif x<0 or y<0:
    x=(x+y)/2
    y=x
print(x,y)
