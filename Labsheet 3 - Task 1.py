sen = "aa bb cc"

"""
Takes a string as an input and returns a split list and length of list
to the reverse function.
"""
def strSplitLen(sen):
    return reverse(len(sen.split()), sen.split())
"""
Takes pos and sentence (which is a list)
appends the list with element at pos-1 (append automatically put
element at the back of list)
since there’s two elements (original and appended), the original
gets removed.
This is done until pos reaches 0 which returns new list 
"""
def reverse(pos, sentence):
    if pos == 0:
        return sentence
    sentence.append( sentence[pos-1] )
    sentence.remove( sentence[pos-1] )
    return reverse(pos-1, sentence)

print(strSplitLen(sen))
