# dictionaries in python
# dictionaries work based on key and values

# how to create one
python_dictionary = {"key1": "hello",
                     "key2": "world"}
# each key holds a specific value

# to get the data of a key
print(python_dictionary["key1"])
print(python_dictionary["key2"])
# you need to write the name of the key correctly

# to add a key and value to a dictionary
python_dictionary["key3"] = "hello world"
print(python_dictionary["key3"])

# to clear a dictionary
# this part will clear the dictionary so the only item will be key3 because it is added after this
python_dictionary = {}

# to redefine a key value
python_dictionary["key3"] = "Programmers"
print(python_dictionary["key3"])

# to loop through the dictionary
for items in python_dictionary:
    print(python_dictionary[items])


# we can also create nested dictionaries
# they can contain other dictionaries or lists

countries = {
    "France": "Paris",
    "Germany": "Berlin"
}

# storing a list inside a dictionary
travel_log = {
    "France": ["Paris", "Dijon", "Lille"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}
print(travel_log)

# nesting a dictionary in dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Dijon", "Lille"]},
    "Germany": {"cities_visited":["Berlin", "Hamburg", "Stuttgart"], "cities_left": ["Munich"]}
}
print(travel_log)

# nesting a dictionary in a list

travel_log = [
    {"country": "France",
     "cities_visited": ["Paris", "Dijon", "Lille"],
     "total_visits": 12},
    {"country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 5},
]
print(travel_log)
