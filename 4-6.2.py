from itertools import cycle

c = 0
for i in cycle('ldjggjbnrkjgnbrgnbr'):
    if c > 5:
        break
    else:
        print(i)
    c += 1
