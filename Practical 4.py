def character_analysis(char):
    if char.isalpha():
        if char.isupper():
            print(f"The character '{char}' is an uppercase letter.")
        else:
            print(f"The character '{char}' is a lowercase letter.")
    elif char.isdigit():
        digit_names = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        digit_name = digit_names[int(char)]
        print(f"The character '{char}' is a numeric digit, and its name is {digit_name}.")
    else:
        print(f"The character '{char}' is a special character.")

# Accepting input from the user
user_input = input("Enter a character: ")

# Performing character analysis
if len(user_input) == 1:
    character_analysis(user_input)
else:
    print("Please enter a single character.")

