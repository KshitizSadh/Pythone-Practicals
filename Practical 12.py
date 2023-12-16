t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# a) Print half the values of the tuple in one line and the other half in the next line.
half_length = len(t1) // 2
print("Half of the values in one line:", t1[:half_length])
print("Other half of the values in the next line:", t1[half_length:])

# b) Print another tuple whose values are even numbers in the given tuple.
even_numbers_tuple = tuple(x for x in t1 if x % 2 == 0)
print("Tuple with even numbers:", even_numbers_tuple)

# c) Concatenate a tuple t2=(11,13,15) with t1.
t2 = (11, 13, 15)
concatenated_tuple = t1 + t2
print("Concatenated tuple:", concatenated_tuple)

# d) Return maximum and minimum value from this tuple.
max_value = max(t1)
min_value = min(t1)
print("Maximum value in the tuple:", max_value)
print("Minimum value in the tuple:", min_value)
