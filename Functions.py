import random
"""
In this repo, its basically the structure of the function and what it does:
"""
# function with no return type 
# def request(name):
#     ''' here def is the keyword used to define the function and (request) is the name of the function and (name) is the argument
#     that is passed to the function and use it for carrying out operations in the function'''
#     print("Hello ",name)

# request("Bipin")

#function with return type 
def request():
    return random.randint(1,10)

y=request()
print("The random integer is ",str(y))

