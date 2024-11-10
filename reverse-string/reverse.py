def reverse_string(input_string):
    """Reverse a string using a loop."""
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string  # Prepend the character
    return reversed_string

# Main execution
if __name__ == "__main__":
    # Get user input
    original_string = input("Enter a string to reverse: ")
    reversed_result = reverse_string(original_string)
    print(f"Original String: {original_string}")
    print(f"Reversed String: {reversed_result}")