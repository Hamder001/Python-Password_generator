import string
import random
import time

ALLOWED_CHARS = string.ascii_letters + string.digits + "!#$%&()*+,-./:;<=>?@[]^_`{|}~"

print('Welcome to Password Generator v1.0\n***************************\n')
time.sleep(1)
choice = input('Choose your password option\n1 - Generate Password\n2 - Exit\n')

if choice == '2':
    print('Have a great day!')
    exit()
elif choice == '1':
    while True:
        try:
            length = int(input('Enter password length (6-20): '))
            if 6 <= length <= 20:
                break
            else:
                print('Password length must be between 6 and 20 characters.')
        except ValueError:
            print('Invalid input. Please enter a number between 6 and 20.')

    while True:
        password = ''.join(random.choice(ALLOWED_CHARS) for i in range(length))
        confirm = input('Your new password: {}\nPress y to confirm, any other key to regenerate.\n'.format(password))
        if confirm.lower() == 'y':
            break
    print('Thanks for testing the program!')
else:
    print('Invalid input. Please choose option 1 or 2.')
    exit()
