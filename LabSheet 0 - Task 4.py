word =  input ("Input a word: ")
start = int(input ("select starting point: "))
remove = int(input ("select starting point: "))

count=1
while count!= remove:
    word= word.replace (word[start],"")
    count=count+1

print(word)
