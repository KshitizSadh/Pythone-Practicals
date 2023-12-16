def create_cubes_dictionary():
    cubes_dict = {key: key ** 3 for key in range(1, 6)}
    return cubes_dict

# Example usage:
result_dict = create_cubes_dictionary()

# Printing the dictionary
print("Dictionary with keys as numbers between 1 and 5 and values as cubes:")
print(result_dict)
