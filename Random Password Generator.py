import random
import string

#def generate_pass()
letters =string.ascii_letters
digits = string.digits
symbols = string.punctuation

#upper, lower, sym, digi = True, True, True, True
password = ""

characters = letters+digits+symbols
    
for i in range(3):
    char = random.choice(characters)
    while not (char.islower() or char.isupper() or char.isdigit() or char in string.punctuation):
        char = random.choice(characters)
    password += char

print(password)
#print(string.punctuation)

