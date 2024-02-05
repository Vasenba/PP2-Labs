def pal(word):
    if (word == word[::-1]):
        print("Palindrome")
    else:
        print("Not palindrome")

a = input("Word: ")
pal(a)
