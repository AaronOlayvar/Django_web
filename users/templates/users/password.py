
import random


lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special ="!@£$%^&*"

used_for = lower_case + upper_case + numbers + special
pass_length = 8 

gen_pass = "".join(random.sample(used_for, pass_length))

print ("Your random generated password is",gen_pass)

