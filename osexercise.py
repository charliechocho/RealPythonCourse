import glob
import os

my_path = "./book1-exercises/chp09/practice_files/*/*/*.png"

file_list = glob.glob(my_path)

for item_li in file_list:
    print item_li
