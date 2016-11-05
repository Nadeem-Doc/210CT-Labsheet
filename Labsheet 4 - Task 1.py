
alist = [1,5,7,18,19,21,25,37,39,89,214]
low = 25
high = 39

def binarySearch(alist, low, high): 
    first = 0 
    last = len(alist)-1 
    found= False 

    while first<= last and not found: 
       
        midpoint = (first + last)//2 
        if alist[midpoint] >= low and alist[midpoint] <= high: 
            found = True 
        else: 
            if high < alist[midpoint]:
                last = midpoint-1 
            else:
                first = midpoint+1 

    return found 

print(binarySearch(alist, low, high)) 
"""
 Big O notation for the adapted binary search is O(longn) as
 the worst case scenario remains the same as the orginal bigO for binary search.
 O(longn) as each instance decreases in time.
 https://en.wikipedia.org/wiki/Time_complexity#Logarithmic_time
"""
