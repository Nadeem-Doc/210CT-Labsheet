sequence = [1,2,3,2,6,1,5,7,8,19,]

def submax(sequence):
    head = 0
    for i in range(len(sequence)):
        if i+1 == len(sequence):
             sequence[head:i]
        elif sequence[i] < sequence[i-1]:
             sequence[head:i]
             head = i 
 


def subMax2(sequence):
    tempList = []
    for i in range(len(sequence)):
        if sequence[i] < sequence[i-1]:
            tempList.append(sequence[i])
            elseif 

    return(tempList)
        
print(subMax2(sequence))




"""
if the number is larfer than the previous then add to tempList which is then
used to compare the length of the sublistsuntil the lenght of
the list is reached

"""



