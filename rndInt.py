from random import randint

toss_up = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

for i in range(1,100):
    x = randint(1,6)
    toss_up[x] +=1

for i in toss_up:
    print toss_up[i]
    
 
