
for x  in (0,1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                A = (( x and w ) or ( w and z ))
                B = (( not z or y) and ( not y or x))
                F = A and B or not A and not B
                if F == 1:
                     print(x,y,z,w)