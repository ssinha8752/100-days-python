def longest_consecutive_sequence(l1):
    if not l1:
        return 0

    l1 = sorted(set(l1))  # Sort and remove duplicates
    max_length = 1
    current_length = 1

    for i in range(1, len(l1)):
        if l1[i] == l1[i - 1] + 1:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    return max(max_length, current_length)


print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""