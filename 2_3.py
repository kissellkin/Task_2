print('x' ' ' 'y' ' ' 'z')
for x in (0,1):
    for y in (0,1):
        for z in (0,1):
            for w in (0,1):
                f = (( not x or not z) and ( y or not x))
                if f == 0:
                    print(x,y,z)