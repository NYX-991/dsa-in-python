# Count the frequency of each element in an array using a dictionary    
arr = [1, 2, 2, 3, 1, 4, 2, 3]
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)

# Find the element that occurs the most
arr = [1, 2, 2, 3, 1, 4, 2, 3]
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
most_frequent = max(freq, key=freq.get)
print(most_frequent)

# Find all duplicate elements
arr = [1, 2, 2, 3, 1, 4, 2, 3]
freq = {}
duplicates = []
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
for num, count in freq.items():
    if count > 1:
        duplicates.append(num)
print(duplicates)

# Find first non-repeating element
# Find the element that appears only once
# Check if two arrays have the same elements
# Check if two strings are anagrams
# Find the intersection of two arrays
# Two Sum
# Find pairs with a given sum
# Longest consecutive sequence
# Count distinct elements in every window of size K
# Longest subarray with sum K
# Count subarrays with sum K
# Longest substring without repeating characters

