import csv
import os

my_path = "./book1-exercises/chp09/practice_files"

with open(os.path.join(my_path, "tabbed wonka.csv"), 'r') as my_file:
    output = csv.reader(my_file, delimiter='\t')
    next(output)
    for f_name, l_name, award in output:
        print '%s %s got: %s' % (f_name, l_name, award)
