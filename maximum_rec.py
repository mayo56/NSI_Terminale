
def maximum_rec(tab, debut, fin):
    if debut == fin:
        return tab[debut]
    
    milieu = (debut + fin) // 2
    x = maximum_rec(tab, debut, milieu)
    y = maximum_rec(tab, milieu + 1, fin)

    if x > y:
        return x
    else:
        return y

print(maximum_rec([7,4,2,1,8,5,6,3], 0, ))