word = "I like houses"

def vowelRemove(word):

    if  word== "":
        return word

    elif word[0] in "aeiou":
        return vowelRemove(word [1:] )
    else: return word[0] + vowelRemove(word [1:])

print(vowelRemove(word))



