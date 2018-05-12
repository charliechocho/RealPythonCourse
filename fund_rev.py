print "\n# -- part 1 -- #"
# Modify the variable value so that all of the
# `print` statements return `True`.
zero = 1
one = 2
two = [5, 4, 3, 2, 1, 0]
three = "I love Python!"
four = [["P", "y", "t", "h", "o", "n"],["i", "s"],["h", "a", "r", "d"]]
five = {"happy":"birthday"}
six = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
days = ("Fri", "Sat", "Sun")
x, y, seven = days
# DO NOT CHANGE ANYTHING BELOW THIS LINE #
# -------------------------------------- #
print "zero: %s" % (zero == 1)
print "one: %s" % (one < 22)
print "two: %s " % (len(two) == 6)
print "three: %s " % (three[2] == "l")
print "four: %s " % (
    four[0][5] == 'n' and four[0][0] == "P" and four[2][1] == "a"
)
print "five: %s " % (five.get("happy") == "birthday")
print "five: %s " % (len(five) == 1)
print "six: %s " % (len(six & {2,5,7}) == 3)
print "seven: %s " % (seven == "Sun")
# -------------------------------------- #
