import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"

all = lower + upper + numbers
length = 10
password = "".join(random.sample(all, length))
print(password)