birthdays = {'Luke Skywalder':'5/24/19', 'Obi-Wan Kenobi':'3/11/57', 'Darth Vader':'4/1/41'}
print birthdays.keys()

if 'Darth Vader' in birthdays:
    print 'The dark side is here'
else:
    print 'Long live the Jedi Knights'

if 'Yoda' in birthdays:
    print 'With you I am'
else:
    birthdays2 = {'Yoda':'Unknown'}
    birthdays.update(birthdays2)

for name in birthdays:
    print name, ' ', birthdays[name]

del birthdays['Darth Vader']

print birthdays
