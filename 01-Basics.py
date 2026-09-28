# Count the number of digits in an integer
n = 5382
count = 0
while n>0:
    count+=1
    n//=10
print(count)

# Check if a number is Palindrome
n = 1221
original = n
num = 0
while n>0:
    rev = n%10
    num = num*10 + rev
    n = n//10
if num == original:
    print("True")
else:
    print("False")

# Check if a number is Armstrong number
n = 153
og = n
nod = len(str(n))
total = 0
while n > 0:
    num = n % 10
    total = total + (num ** nod)
    n //= 10
if total == og:
    print("True")
else:
    print("False")

# Print Factors of a given number
# Basic
n = 36
for i in range (1,n + 1):
    if n % i == 0:
        print (i)
# Optimised
import math
n = 36
for i in range (1, int(math.sqrt(n) + 1)):
    if n % i == 0:
        print (i)
        if i != n//i:
            print(n//i)

# Reverse a number
n = 5382
reverse = 0
while n > 0:
    num = n % 10
    reverse = reverse*10 + num
    n //= 10
print(reverse)

# Find the sum of digits
n = 5382
sum = 0
while n > 0:
    sum = sum + n%10
    n//=10
print (sum)

# Find the product of digits
n = 5382
prod = 1
while n > 0:
    prod = prod * (n%10)
    n//=10
print(prod)

# Print every digit of a number
n = 5382
while n > 0:
     digit= n%10
     print(digit)
     n//=10

# Find the largest digit in a number
n = 5873

largest = 0

while n > 0:
    digit = n % 10
    largest = max(largest, digit)
    n //= 10

print(largest)

# Find the smallest digit in a number
n = 5873

smallest = n % 10

while n > 0:
    digit = n % 10
    smallest = min(smallest, digit)
    n //= 10

print(smallest)

# Count how many times a particular digit appears
n = 538323
target = 3
count = 0
while n > 0:
    digit = n % 10
    if digit == target:
        count += 1
    n//=10
print(count)