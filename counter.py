num = int(input("Enter a positive number to the sum of all the integar from 0 to that number: "))
tot, i = 0, 0

while i <= num:
    tot += i
    i += 1

print (f"The result using the loop method to count is {tot}: ")

tot2 = (num + 1) * (num / 2)
print(f"The result using the (X + 1) * (X / 2) is {tot2}")