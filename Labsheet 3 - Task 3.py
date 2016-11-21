"""
Takes a word/sentence and recursively breaks it down until
it has nothing in the string. The elif statement checks
for a vowel in which case everything after the vowel is returned
else the element is concatenated with the return of the word and everything
that follows
"""

word = "I like houses"

def vowelRemove(word):

    if  word== "":
        return word

    elif word[0] in "aeiou":
        return vowelRemove(word [1:] )
    else: return word[0] + vowelRemove(word [1:])

print(vowelRemove(word))
