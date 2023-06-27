from functions import square

for i in range(11):
    if square(i) % 2 == 0:
        print(f"The square of {i} is {square(i)} 🌃")
    else:
        print(f"The square of {i} is {square(i)} 👹")