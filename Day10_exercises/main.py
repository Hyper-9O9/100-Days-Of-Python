# functions with output

def format_name(fName, lName):
    result = fName.title() + " " + lName.title()
    return result
print(format_name("hersh", "hiwa"))


# docstring
# docstrings are used to show what a function does
# to create a docstring you need to write """ """ after the declaration of the function

def zero():
    """"Just gives back a zero, no special use """
    return 0

zero()