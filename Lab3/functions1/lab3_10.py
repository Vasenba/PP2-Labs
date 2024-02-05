def uniq(tl):
    ul = []

    for a in tl:
        if a not in ul:
            ul.append(a)

    return ul

thelist = [int(x) for x in input("List: ").split()]
result = uniq(thelist)
print(result)
