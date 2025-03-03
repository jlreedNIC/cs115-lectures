# -----
# Debugging Example
# Program to count vowels in a string
# -----

# prompt the user for a string
input_string = input("Enter a string: ")

# init vowel count
vowel_count = 0

# loop through each character in the string
for letter in input_string:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        vowel_count += 1

# print the result
print(f"Number of vowels: {vowel_count}")