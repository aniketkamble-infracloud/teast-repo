def is_permutation_of_557(a, b, c):
    # This only checks if the sum is correct, not the actual values or counts
    if a + b + c == 17:
        return True
    else:
        return False

# Fails for input (1, 8, 8) because sum is 17 but it's not (5, 5, 7)
