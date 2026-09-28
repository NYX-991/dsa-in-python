# Print 1 to N using recursion
def print_numbers(i,n):
    if i > n:
        return
    print(i)
    print_numbers(i + 1, n)
    
print_numbers(1, 10)

# Print N to 1 using recursion
# Head recursion
def print_numbers_reverse(i,n):
    if i < 1:
        return
    print(i)
    print_numbers_reverse(i - 1, n)

print_numbers_reverse(10, 1)

#Tail recursion
def print_numbers_reverse_tail(i,n):
    if i > n:
        return
    print_numbers_reverse_tail(i + 1, n)
    print(i)

print_numbers_reverse_tail(1, 10)

# Print sum of first N natural numbers using recursion
# Parameterized recursion
def sum_natural_numbers(i, n, sum):
    if i > n:
        print(sum)
        return 
    sum_natural_numbers(i + 1, n, sum + i)

sum_natural_numbers(1, 10, 0)

#Functional recursion
def sum_of_numbers(n):
    if n == 1:
        return 1
    return n + sum_of_numbers(n - 1)
sum_of_numbers(10)
x = sum_of_numbers(10)
print(x)

# Find factorial of a number using recursion
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)
factorial(5)
x = factorial(5)
print(x)


# Reverse an array using recursion
nums = [2, 9, 8, 3, 6, 7, 1, 4, 5]
def reverse_array(nums, start, end):
    if start >= end:
        return
    nums[start], nums[end] = nums[end], nums[start]
    reverse_array(nums, start + 1, end - 1)

reverse_array(nums, 0, len(nums) - 1)
print(nums)

# Check if a string is palindrome or not
s = "ANBCDDCBNA"
def is_palindrome(s, start, end):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return is_palindrome(s, start + 1, end - 1)
print(is_palindrome(s, 0, len(s) - 1))

# Find the Fibonacci number using recursion


