def sum_up_to_n(n):
    total = 0
    for i in range(n): # Bug: Should be range(1, n + 1) or range(n + 1)
        total += i
    return total

# Expected: sum_up_to_n(3) should be 6 (1+2+3)
# Actual: sum_up_to_n(3) returns 3 (0+1+2)
