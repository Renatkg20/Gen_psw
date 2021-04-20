import random
from string import digits
from string import punctuation
from string import ascii_letters
# user_input = int(input("Please inputh the length the password "))

def gen_password(len_pass):
	symbols = ascii_letters + digits + punctuation
	secure_random = random.SystemRandom()
	password = ''.join(secure_random.choice(symbols)for i in range(len_pass))
	return password


# print(gen_password(user_input))

#https://github.com/renatkg20

import sys
c = sys.stdin.readlines()
t = (" ".join(c)).split(" ")


n, m = int(t[0]), int(t[1])

pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))