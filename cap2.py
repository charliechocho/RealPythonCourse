from capitals import capitals_dict
import random

answ = False
stat = False

while stat is False or answ is False:
    #print random.choice(capitals_dict)
    cap = random.choice(capitals_dict.keys())
    answ = raw_input("What's the capital of %s? " % (cap))
    if answ == capitals_dict[cap]:
        print '\nCorrect!!'
        stat = True
    elif answ == 'exit':
        print '\nGoodbye!'
        stat = True
    else:
        pass


#print capitals_dict[cap]
