def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]
b = input("List: ")
c = list(map(int, b.split()))
d = filter_prime(c)
print(d)
