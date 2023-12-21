
def rebours(n:int) -> None:
    if n == -1:
        print("Partez !")
    else:
        print(n, end=" ")
        rebours(n - 1)
    
rebours(3)