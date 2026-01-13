# Find sum of numbers from 1 to n using recursion

def find_sum(n):
    if n == 0:
        return 0
    return n + find_sum(n - 1)

result = find_sum(5)
print("Sum is:", result)
