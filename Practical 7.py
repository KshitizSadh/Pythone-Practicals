def find_occurrences_indices(main_string, sub_string):
    indices = []
    start_index = 0

    while True:
        index = main_string.find(sub_string, start_index)
        if index == -1:
            break
        indices.append(index)
        start_index = index + 1

    return indices if indices else -1

# Example usage:
string1 = "hello, hello, world, hello"
string2 = "hello"

result = find_occurrences_indices(string1, string2)

if result == -1:
    print(f"The second string '{string2}' is not present in the first string '{string1}'.")
else:
    print(f"The second string '{string2}' is present at indices: {result}")
