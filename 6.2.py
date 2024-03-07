
def odszyfruj(word,key=0):
    key%=26
    temp=""
    for letter in word:
        l=ord(letter)-key
        if l>ord("Z"):
            l-=26
        elif l<ord("A"):
            l+=26
        temp+=chr(l)
    return temp

file=open("dane_6_2.txt","r")
words=[]
for line in file:
    line=line.rstrip()
    xd=line.split(" ")
    words.append(xd)
file.close()
odszyfrowane=[]
for word in words:
    if len(word)==1:
        odszyfrowane.append(str(word))
    else:
        odszyfrowane.append(odszyfruj(word[0],int(word[1])))
file2=open("wynik_6_2.txt","w")
for word in odszyfrowane:
    file2.write(word+"\n")
file2.close()
