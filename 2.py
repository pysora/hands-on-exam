import re

def is_palindrome(string):
    cleaned_string = re.sub(r'\W+', '', string.lower())
    reversed_string = cleaned_string[::-1]

    return cleaned_string == reversed_string

input_string = input("Enter a word or phrase: ")
if is_palindrome(input_string):
    print(input_string, "is a palindrome")
else:
    print(input_string, "is not a palindrome")
