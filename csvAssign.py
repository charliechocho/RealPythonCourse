import csv
import os

my_path = './book1-exercises/chp09/practice_files/'

with open(os.path.join(my_path, 'pastimes.csv'), 'r') as my_file1, open(os.path.join(my_path, 'pasnewtimes.csv'), 'w') as my_file2:
    out_file = csv.reader(my_file1)
    in_data = csv.writer(my_file2)
    in_data.writerow(['Person', 'Action', 'Category'])
    next(out_file)
    for row in out_file:
        if 'fighting' in str(row[1]).lower():
            row.append('Combat')
            in_data.writerow(row)
        else:
            row.append('Other')
            in_data.writerow(row)
