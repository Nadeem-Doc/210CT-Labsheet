p = input ("input point of reference: ")
a = input ("input coordinate 1: ")
b = input ("input coordinate 2: ")
c = input ("input coordinate 3: ")

ax = a[0]
ay = a[1]
by = b[1]
bx = b[0]
cx = c[0]
cy = c[1]
px = [0]
py = [1]

if px > ax and px > bx and px > cx:
          print("right")
elif  px < ax and px < bx and px < cx:
          print("Left")
elif py < ay and py < by and py < cy:
          print("above")
elif py > ay and py > by and py > cy:
          print("below")
else:
          print("Erorr")


