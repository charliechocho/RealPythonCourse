import glob
import os
my_path = "./book1-exercises/chp09/practice_files/images"

for cur_fold, sub_fold, all_files in os.walk(my_path):
    if sub_fold:
        print sub_fold[0]



#file_list = os.path.join(my_path, "*/*.png")
#print '\n' * 2

#for item_li in glob.glob(file_list):
#    print item_li
