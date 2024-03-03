import time
import math

def invoke_square_root(millis):
    time.sleep(millis / 1000.0)  
    number = float(input())
    result = math.sqrt(number)
    print(f"The square root of {number} is {result}")

if __name__ == "__main__":
    milliseconds = int(input())
    invoke_square_root(milliseconds)
