import random
lis=[]

characters = list(map(chr, range(0, 128)))
for i in range(8):
    val=random.choice(characters)
    for j in val:
        lis.append(j)
print("Your strong Password is",''.join(map(lambda x:str(x), lis)))