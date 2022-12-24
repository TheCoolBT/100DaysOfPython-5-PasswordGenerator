import random
import string
import secrets

# Defines alphabet of characters that will be used in password generation
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation


# pwdgen: function that takes in nothing and returns a password made up of the given ammount of letter numbers and
# symbols.
def pwdgen():
    pwd = ''  # blank string to be appended
    # takes in user input
    amtlet = int(input("How may letters in the password?:"))
    amtnum = int(input("How many numbers in the password?:"))
    amtsym = int(input("How many symbols in the password?:"))

    # Uses for loop to append the random characters to the empty string
    for i in range(amtlet):
        pwd += ''.join(secrets.choice(letters))

    for i in range(amtnum):
        pwd += ''.join(secrets.choice(numbers))

    for i in range(amtsym):
        pwd += ''.join(secrets.choice(symbols))

    # shuffles the password after the characters have been added
    fpwd = ''.join(random.sample(pwd, len(pwd)))

    print(fpwd)


# runs the function
pwdgen()
