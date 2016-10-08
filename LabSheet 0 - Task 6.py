a = input ("1st: ")
z= input ("2nd: ")
e= input ("3nd: ")
r= input ("4nd: ")

L = [a,z,e,r]


a = max(L)
b = min(L)


def numfinder (w, L):
    count = 0
    found = 0
    while found!= 1:
        if w==L[count]:
            found = found+1
            count= count+1
            return str(count)
        else:
            count = count+1

print("max number is ", str(a), "and position is ", numfinder(a, L))
print("min number is ", str(b), "and position is ", numfinder(b, L))

