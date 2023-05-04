import string
import random
import time

print('Welcome to Password Generator v1.0\n***************************\n')     # Output at launch of the script
one = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation     # What will be used by the generator such as letters numbers or punctuation from string module
time.sleep(1)#To let the user read a little bit!
choice = str(input(('Choose your password option\n 1- Generate Password\n 2- Exit\n'))) # Let the user choose between 1 or two for the option to generate a password or exit the program

if choice == str('2'):      # if choice answer is 2 then user will get an out put of have a great day then exit the program
    print('Have a great day!')
    exit()
elif choice == str('1'):    #if the user choose 1 then he will get an
    long = int(input('What will be your password length 6- 20')) #The length of the password will be asked to the user to input a value then store to long variable

    def generate(long):  #I set the function with the length parameter
        password = ""   #I set the password variable
        for i in range (long):
            password += random.choice(one) # it will randomly choose letters / symbols / numbers i added to the one variable to make it simple.
        return password # it will return the password variable to all the scrip

    pass2 = generate(long) #The variable pass2 will then execute the function generate with the length parameter (long)
    print('Your new password:\n' + pass2 + '\n') #It will print the string Your new password: followed with the pass2 variable that will contain the random password
    print('Thanks for testing the program\n') #Just a nice words :)
else: #This is reduct error that the user could possibly make when not choosing between option 1 or 2
    print('Choose between 1 or 2')
    exit()
#the reason i did the option 2 before 1 is because the option two was less coding making it faster to make

#If you wanted to make an upgrade to this script you should surely make a code block to refuse non integer (numbers) values given by the user to create an error.