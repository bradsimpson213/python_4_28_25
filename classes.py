


class Cat:
    breed = "American Shorthair"
    price = "5$"
    def __init__(self, color, age, name="Kitty"): 
        self.color = color
        self.age = age
        self.name = name

    def speak(self):
        return  "Meow, meow, meow..."

    def get_older(self):
        self.age += 1
        print(f"{self.name} just had a birthday and is now {self.age} years old!")


class Tiger(Cat):
    def __init__(self, color, age, name="Tony"):
        super().__init__(color, age, name)

    def speak(self):
        return "Rawr!!!"


# tigger = Tiger("orange", 20, "Tigger")
# print(tigger.name)
# print(tigger.speak())

# blue = Cat("black", 8, "Blue")
# patch = Cat("tuxedo", 8, "patch")
# print(blue.age)
# # print(blue.name)
# # print(blue.color)
# print(blue.speak())
# print(blue.get_older())
# print(blue.age)
# print(blue.breed)
# print(patch.breed)
# Cat.breed = "American Longhair"
# blue.breed = "Feisty Cat Ninja"
# print(blue.breed)
# print(patch.breed)


# blue = {
#     'name': "Blue",
#     "age": 8,
#     "color": "Black"
# }

class Listx:
    def __init__(self):
        self.list = []
        self.length = 0

    def append(self, new_item):
        self.list += [new_item]
        self.length += 1
        print(self.list)

    def __len__(self):
        return self.length
    
    def __str__(self):
        return f"< List Class: {self.list}>"
        
    def __repr__(self):
        return f"< List Class: {self.list}>"

new_listx = Listx()
new_listx.append(1)
new_listx.append(2)
print(len(new_listx))
print(new_listx)
