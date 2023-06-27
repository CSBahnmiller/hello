import sys 

try:

    x = int(input("X: "))
    y = int(input("Y: "))
except ValueError as e:
    print(f"Invalid input, we only work with integers here, you idiot, ⚠️ {e} ⚠️")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError as e:
    print(f"Hey, moron dividing by zero is unacceptable, ⚠️ {e} ⚠️")
    sys.exit(1)


print(f"{x} / {y} = {result}")