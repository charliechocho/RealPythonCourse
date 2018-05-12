cats_ring = {}

for i in range(1,101):
    cat_assign = {'cat%d' % (i): 'nhat'}
    cats_ring.update(cat_assign)


def hat_job(x):
    y = 1
    while y <= 100:
        if cats_ring['cat%d' % (y)] == 'nhat':
            cats_ring['cat%d' % (y)] = 'Hat'
            y += x
        else:
            cats_ring['cat%d' % (y)] = 'nhat'
            y += x


for i in range(1,101):
    hat_job(i)

for name in cats_ring:
    if cats_ring[name] == 'Hat':
        print '%s %s' % (name, cats_ring[name])
