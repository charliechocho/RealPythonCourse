myfile = open("testfile.txt", 'r')
txt_inp = ['This is Line 1\n', 'This is Line 2\n', 'This is line 3\n']
nxt_line = ['Next line is 4\n']

#myfile.writelines(nxt_line)
for line in myfile.readlines():
    print line, 


myfile.close()
