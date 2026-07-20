nums = [1,2,3,3,5,6,4,7,0,9]

n = len(nums)

freq = {}

# Initialize frequency of numbers 0 to n
for i in range(n + 1):
    freq[i] = 0

# Mark numbers present in the array
for i in nums:
    freq[i] = 1

# Print missing number(s)
for key, value in freq.items():
    if value == 0:
        print(key)