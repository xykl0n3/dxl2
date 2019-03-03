text_file = open("motion/walk.txt", "r")
pos= []
for val in text_file.read().split('\n'):
    inpos=[]
    for num in val.split(' '):
        inpos.append(int(num))
    pos.append(inpos)
    text_file.close()

print (pos)