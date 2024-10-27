import random
pass_length = 10 
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
   

    for i in range(pass_length):
        password += random.choice(elements)

    return password