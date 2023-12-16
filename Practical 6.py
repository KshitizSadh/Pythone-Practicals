def swap_first_n_characters(str1, str2, n):
    if n <= min(len(str1), len(str2)):
        swapped_str1 = str2[:n] + str1[n:]
        swapped_str2 = str1[:n] + str2[n:]
        return swapped_str1, swapped_str2
    else:
        print("Error: The specified value of 'n' is greater than the length of either string.")
        return str1, str2

# Accepting input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
swap_length = int(input("Enter the number of characters to swap (n): "))

# Performing the swap
result1, result2 = swap_first_n_characters(string1, string2, swap_length)

# Displaying the results
print(f"After swapping the first {swap_length} characters:")
print(f"String 1: {result1}")
print(f"String 2: {result2}")
