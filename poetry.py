import random
import os

noun_li = ['fossil', 'horse', 'aardvark', 'judge', 'chef', 'mango', 'extrovert', 'gorilla']
verb_li = ['kicks', 'jingles', 'bounces', 'slurps', 'meows', 'explodes', 'crudles']
adj_li = ['furry', 'balding', 'incredulous', 'fragrant', 'exuberating', 'glistening']
prep_li = ['against', 'after', 'into', 'beneath', 'upon', 'for', 'in', 'like', 'over']
adv_li = ['curiously', 'extravagantly', 'tantalizingly', 'furiously', 'sensuously']
words_li = []
vowels = 'a A e E i I o O u U y Y'



def ran_choice(x,y):
    while y > 0:
        z = random.choice(x)
        if z in words_li:
            pass
        else:
            words_li.append(z)
            y -= 1

def make_poem():
    os.system('clear')
    strt1 = str(words_li[6])
    if strt1[0] in vowels:
        strt = 'An'
    else:
        strt = 'A'
    print """
    %s %s %s

    %s %s %s %s %s the %s %s
    %s, the %s %s
    the %s %s %s a %s %s


    """ % (strt, words_li[6], words_li[0], strt, words_li[6], words_li[0],
        words_li[3], words_li[9], words_li[7], words_li[1], words_li[11],
        words_li[0], words_li[4], words_li[1], words_li[5], words_li[10],
        words_li[8], words_li[2])




ran_choice(noun_li, 3)
ran_choice(verb_li, 3)
ran_choice(adj_li, 3)
ran_choice(prep_li, 2)
ran_choice(adv_li, 1)

make_poem()
