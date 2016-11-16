alist=[21,32,14,12,23,4,54,23,44,5,4,3,2,1,2,3,13,45]

def subExtract(sequence):
    nextList=[] #new list to be compared
    head = 0 #start of splice

    for count in range(len(sequence)-1):
        if sequence[count] > sequence[count+1]:
            
            if len(sequence[head:count+1])> len(nextList):
                nextList = sequence[head:count+1]
                head=count+1
            else:
                head=count+1

        elif count==len(sequence)-2:
            if len(sequence[head:len(sequence)+1])> len(nextList):
               nextList = sequence[head:len(sequence)+1]

    return nextList

print(subExtract(alist)
