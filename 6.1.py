file=open("dane_6_1.txt")
words=[]
for line in file:
    words.append(line.rstrip())
file.close()
print(words)
k=107%26
szyfr=[]
for word in words:
    tempword=""
    for c in word:
        letter=k+ord(c)
        if letter>ord("Z"):
            letter-=26
        elif letter<ord("A"):
            letter+=26
        tempword+=chr(letter)
    szyfr.append(tempword)

file2=open("wynik_6_1.txt","w")
for word in szyfr:
    file2.write(word+"\n")
file2.close()
print(szyfr)