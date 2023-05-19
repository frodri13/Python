MIN_CHARACTERS = 7
SPECIAL_CHARS = ['!', '?', '#', '@', '$', '*']
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

PASSWORDS = ['helloWorld', 'imcisamazing69', 'ilovecookies!23', 'python1s@mazingLanguage']

HAS_SPECIAL_CHAR = False
HAS_NUMBER = False
HAS_7_CHARS = False

# Write a program that checks which of the passwords inside PASSWORDS meet the 3 following criteria:
# 1. Minimum characters of 7
# 2. Must contain at least one special character (defined in SPECIAL_CHARACTERS)
# 3. Must include at least one number
# Tip: You may want to loop over PASSWORDS and use multiple if conditions

def is_long_enough(password):
    if len(password) >= MIN_CHARACTERS:
        return True

def contains_special_char(password):
    for char in SPECIAL_CHARS:
        if char in password:
            return True

def contains_num(password):
    for num in NUMBERS:
        if str(num) in password:
            return True

def is_password_valid(password):
    if is_long_enough(password) and contains_special_char(password) and contains_num(password):
        print(f'{password} is a valid password')
    else:
        print(f'{password} is not a valid password')

for password in PASSWORDS:
    is_password_valid(password)