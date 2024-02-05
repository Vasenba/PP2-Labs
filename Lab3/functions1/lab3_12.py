def histogram(tl):
    for a in tl:
        print('*' * a)

b = [int(x) for x in input("List: ").split()]
histogram(b)
