text_file = open("motion/stand.txt", "r")
pos= []
for val in text_file.read().split('\n'):
    inpos=[]
    for num in val.split(' '):
        inpos.append(int(num))
    pos.append(inpos)
    text_file.close()


for list in pos:
    for i in range(1,11):
            print (list[i-1])

