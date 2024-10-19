def extract_numbers(user_input):

    numbers_only = ''. join([char for char in user_input if char.isdigit()])
    return numbers_only


user_input = input("Enter a string with numbers: ")
result = extract_numbers(user_input)
print(f'Extracted numbers: {result}')