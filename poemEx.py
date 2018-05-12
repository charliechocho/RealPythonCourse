with open('./outputs/poem.txt', 'r') as my_poem, open('./outputs/newPoem.txt', 'a') as my_new_poem:
    for row in my_poem.readlines():
        my_new_poem.write(row)

    my_new_poem.write('\nRoses are red, violets are blue...\n')
