def div_chk(x):
    for i in range(1,x+1):
        if x % i == 0:
            print i, ' is a evenly divided by', x
        

num_chk = raw_input('What number? ')

div_chk(int(num_chk))

    
