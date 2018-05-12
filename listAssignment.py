universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institure of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def mean(x):
    y = 0
    for i in x:
        y = y+i

    return y, y/int(len(x))

def median(x):
    x.sort()
    y = int(round(float(len(x))/2)) - 1
    
    return x[y]

def enrollment_stats(x):
    stdts_only = []
    tuition = []
    for i in x:
        stdts_only.append(i[1])
        tuition.append(i[2])
        
    return stdts_only, tuition


tot_stud, tot_tui = enrollment_stats(universities)
total_stud, mean_stud = mean(tot_stud)
total_tui, mean_tui = mean(tot_tui)
med_stud = median(tot_stud)
med_tui = median(tot_tui)


print 'Total amount of students is: ', total_stud
print 'Average amount of students is: ', mean_stud
print 'Student median is: ', med_stud, '\n'
print 'Total tuition is: $', total_tui
print 'Average tuition is: $', mean_tui
print 'Tuition median is: $', med_tui, '\n'
tot_stud.sort()
tot_tui.sort()

print tot_stud, '\n', tot_tui


