import csv
import os

my_path = "./book1-exercises/chp09/practice_files/"

my_indata = [['Movie', 'Rating'],
            ['Shawshank Redemption', 5],
            ['Tommyknockers', 2],
            ['Rocky IV', 3],
            ['Grease I', 4]]

with open(os.path.join(my_path, "movies2.csv"), 'w') as my_file:
    in_data = csv.writer(my_file)
    in_data.writerows(my_indata)
