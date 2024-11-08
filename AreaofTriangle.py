#Write a program to calculate semiper area of triangle
side1=36
side2=25
side3=50
print("side 1: ", side1,"Side 2: ", side2, "Side 3:", side3)
semiper=(side1+side2+side3)/2
area=(semiper*(semiper-side1)*(semiper-side2)*(semiper-side3))**0.5
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("semiper: ",semiper,"area =", area)
