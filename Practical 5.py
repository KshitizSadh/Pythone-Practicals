def frequency_of_character(input_string, char_to_find):
    frequency = input_string.count(char_to_find)
    print(f"The frequency of '{char_to_find}' in the string is: {frequency}")

def replace_character(input_string, old_char, new_char):
    modified_string = input_string.replace(old_char, new_char)
    print(f"String after replacing '{old_char}' with '{new_char}': {modified_string}")

def remove_first_occurrence(input_string, char_to_remove):
    modified_string = input_string.replace(char_to_remove, '', 1)
    print(f"String after removing the first occurrence of '{char_to_remove}': {modified_string}")

def remove_all_occurrences(input_string, char_to_remove):
    modified_string = input_string.replace(char_to_remove, '')
    print(f"String after removing all occurrences of '{char_to_remove}': {modified_string}")

# Accepting input from the user
user_string = input("Enter a string: ")
user_char = input("Enter a character: ")

# Performing operations
frequency_of_character(user_string, user_char)
replace_character(user_string, user_char, '*')
remove_first_occurrence(user_string, user_char)
remove_all_occurrences(user_string, user_char)

