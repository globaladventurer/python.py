#function to print multiplication table of a given number

def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

number = int(input("Enter a number: "))

print_multiplication_table(number)

# print fibbonacci sequence 
def print_fibonacci_series(n):
    a, b = 0, 1
    count = 0

    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print(f"Fibonacci series up to {n} term:")
        print(a)
    else:
        print(f"Fibonacci series up to {n} terms:")
        while count < n:
            print(a, end=" ")
            nth = a + b
            a = b
            b = nth
            count += 1

num_terms = int(input("Enter the number of terms: "))

print_fibonacci_series(num_terms)