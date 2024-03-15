

def tri(L:list):
    if len(L) <= 1:
        return L[0]
    
    mid = len(L) // 2
    L1 = tri(L[0:mid])
    L2 = tri(L[mid:])

    if L1 > L2:
        return L1
    else:
        return L2

print(tri([7,4,2,1,8,5,6,3]))