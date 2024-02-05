def generate_permutations(instring, index=0):
    if index == len(instring) - 1:
        print(''.join(instring))
    else:
        for i in range(index, len(instring)):
            instring[index], instring[i] = instring[i], instring[index]
            generate_permutations(instring, index + 1)
            instring[index], instring[i] = instring[i], instring[index]
a = input("Enter a string: ")
listb = list(a)
print(generate_permutations(listb))
