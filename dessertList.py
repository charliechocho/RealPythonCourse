desserts = ['ice cream', 'cookies']
desserts.sort()
print desserts
print desserts.index('ice cream')
food = []
food.extend(desserts)
print food
food.append('turnips')
food.append('broccoli')
print desserts
print food
food.remove('cookies')
print food
breakfast = "cookies, cookies, cookies".split(", ")
print breakfast

def pick_nums(y):
    for i in y:
        if i <= 20:
            print i
        else:
            break


num_lst = [2, 4, 8, 16, 32, 64]

pick_nums(num_lst)
