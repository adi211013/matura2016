def check_if_wrong(first,second):
    wrong=True
    for key in range(0,26):
        result=""
        for i in first:
            result+=chr(((ord(i)-65+key)%26)+65)
        if result==second:
            wrong=False
            break
    return wrong


file=open("dane_6_3.txt","r")
pairs=[]
for line in file:
    line=line.rstrip()
    xd=line.split()
    pairs.append(xd)
file.close()
wrong=[]
for word in pairs:
    if check_if_wrong(word[0],word[1]):
         wrong.append(word[0])

file2=open("wynik_6_3.txt","w")
for w in wrong:
    file2.write(w+"\n")
file2.close()