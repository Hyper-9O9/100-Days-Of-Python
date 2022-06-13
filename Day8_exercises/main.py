# function without a parameter
def greet():
    print("Hello")
    print("How do you do?\n")

greet()

# function with a parameter
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?\n")

greet_with_name("Hersh")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}\n")

greet_with("Hersh", "Kurdistan")

greet_with(location="Britain", name="Jack")