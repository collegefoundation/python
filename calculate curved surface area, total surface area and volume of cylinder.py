#write a program to calculate curved surface area, total surface area and volume of cylinder.
radius= (float)(input("Enter the  radius of cylinder: " ))
height= (float)(input("Enter the height of the cylinder: "))

print("----------------------------------------------")
CurvedSurfaceArea=3.14*radius*height
TotalSurface=2*3.14*radius*(radius+height)
Volume=3.14*radius**2*height
print("curved surface area of cylinder: ", CurvedSurfaceArea)
print("Total surface area of cylinder: ", TotalSurface)
print("volume of cylinder: ", Volume)
