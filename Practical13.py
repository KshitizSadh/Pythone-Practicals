def validate_name(name):
    # Check for digits in the name
    if any(char.isdigit() for char in name):
        raise ValueError("Error: Name should not contain digits.")

    # Check for special characters in the name
    if any(not char.isalnum() and char not in [' ', "'"] for char in name):
        raise ValueError("Error: Name should not contain special characters.")

    return name

try:
    # Accepting input from the user
    user_name = input("Enter your name: ")

    # Validating the name
    validated_name = validate_name(user_name)

    # Printing the validated name
    print("Validated Name:", validated_name)

except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
