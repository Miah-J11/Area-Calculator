print("==================")
print("Area Calculator 📐")
print("==================\n")
print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit\n")

shape=int(input("Which shape: "))
print("\n")

if shape==1:
  Base=int(input("Base: "))
  Height=int(input("Height: "))
  Area=(Base*Height*.50)
elif shape==2:
  Length=int(input("Length: "))
  Width=int(input("Width: "))
  Area=Length*Width
elif shape==3:
  Side=int(input("Side: "))
  Area=pow(Side,2)
elif shape==4:
  Radius=int(input("Radius: "))
  Area=3.141592654*pow(Radius,2)
else:
  print("No Shape Chosen.")

if (shape>=1 and shape<=4):
  print("The area is ", int(Area))
else:
  print("The area is not applicable.")

##print("Which shape: "+input(shape)"\n")

