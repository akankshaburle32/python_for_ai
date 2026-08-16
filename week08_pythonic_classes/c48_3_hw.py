# c48:  que 2:
## User class mein from_dict(data) classmethod implement karo.

# step 1:
## User class mein from_dict(data) classmethod implement karo.

# step 2:

# step 3:

# 1: User ka class lo. def mai __init__ method lo.attribute lo.
# 2: @classmethod lo def mai method do usme cls, para do. return mai cls or para "para do".
# 3: user.method lo para or value do.
# 4: print mai class or para do.

# step 4:

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"])

U = User.from_dict({"name" : "Chaku", "age" : 17})

print("======")
print("Name :", U.name)
print("Age :", U.age)
print("======")            

# step 5: