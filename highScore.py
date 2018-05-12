import csv
import os

my_path = './book1-exercises/chp09/practice_files/'
scores = {}
scores2 = []

with open(os.path.join(my_path, 'scores.csv'), 'r') as score_file:
    hi_scores = csv.reader(score_file)


    for avatar, scored in hi_scores:
        #print avatar, scored
        if avatar in scores:
            #print scores[avatar]
            if int(scores[avatar]) > int(scored):
                #print scores[avatar], scored
                pass
            else:
                dict = {avatar:scored}
                scores.update(dict)
                dict.clear()
        else:
            dict = {avatar:scored}
            scores.update(dict)
            dict.clear()

    scores2 = scores.items()

    for i in sorted(scores2):
        print i[0], i[1]
