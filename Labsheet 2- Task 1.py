
"""
Takes an input which is used as a max range. ‘root’ is then used as a count
which is continuously increased until its product is greater than the
input (number). The if statement then checks if the result of the ‘root’ is greater than the ‘number’ 
if so, ‘root’ is deducted by one. In any case ‘root’ is returned.
"""
def perfectSqaureFinder (number):
    root = 0
    while (root*root)< number:
        root+=1
    if (root*root) > number:
        root-=1    
    return root

number = int(input("Enter number: " ))

print(perfectSqaureFinder(number))
