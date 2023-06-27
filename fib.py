'''
In this program, we define a recursive function fibonacci(n, memo) that calculates the Fibonacci number for a given n. 
The memoization technique is used to store previously computed Fibonacci numbers in the memo dictionary, which helps avoid redundant calculations.

The while loop iterates from 0 to the inputted number, and within each iteration, 
it calls the fibonacci() function to get the Fibonacci number for the current count. The returned Fibonacci number is added to the total.

Finally, the program outputs the total sum of the Fibonacci sequence up to the inputted number.
        
'''
    
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    elif n <= 1:
        return n
    else:
        fib = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        memo[n] = fib
        return fib

number = int(input("Enter a number: "))
total = 0
count = 0

while count <= number:
    total += fibonacci(count)
    count += 1
    if total % 2 == 0:
        print(f"{total} 👹")
    else:
        print(f"{total} 🤔")

print("The total sum of the Fibonacci sequence is:", total)