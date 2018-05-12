print("\n# -- part 2 -- #")
# Find a value for the `value` variable
# so that all print statements return True.
value = [2,4,6,8,10]

# DO NOT CHANGE ANYTHING BELOW THIS LINE #
# ------------------------------------ #
if type(value) is list:
    print(True)
else:
    print(False)

for x in value:
    if not type(x) is int:
        print(False)
    else:
        print(True)

num = 0
while num < value[2]:
    print(True)
    num += 1

for y in range(value[3]):
    if y in value:
        print(True)

try:
    value[5] = "Cat"
    while True:
        print(False)
except IndexError:
    print(True)


try:
    assert value[3] == -1
except AssertionError:
    print(True)
# -------------------------------------- #
