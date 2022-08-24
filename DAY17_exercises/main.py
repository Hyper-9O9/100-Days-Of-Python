# to create a class in python
class User:
    pass

# creating instance of an obj
user_1 = User()
# in python you can add attributes to an obj
# unlike java which you can only use the attributes given in the class
user_1.id = "001"
user_1.username = "Hersh"
print(user_1.id, user_1.username)


# in python to create a constructor you need to use the __inint__ function

class User:
    # creating constructor for the User class
    def __init__(self, username, id):
        # initializing the variable
        self.username = username
        self.id = id
        print(f"Welcome user: {self.username} with the ID of: {self.id}")

user_3 = User(username='Hersh', id='009')
user_4 = User(username='Bond', id='007')

# adding methods to a class

class User:
    def __init__(self,username, id):
        self.username = username
        self.id = id
        self.following = 0
        self.followers = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_5 = User(username='Hersh', id='009')
user_6 = User(username='Bond', id='007')

user_5.follow(user_6)
print(user_5.followers)
print(user_6.followers)
print(user_5.following)
print(user_6.following)