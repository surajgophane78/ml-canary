class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.speed = 0

    def accelerate(self):
        self.speed = self.speed + 10
        print(self.brand + " ki speed ab hai: " + str(self.speed))


# Ab Class se Object banate hain
car1 = Car("Honda", "Red")
car2 = Car("Swift", "Blue")

car1.accelerate()
car1.accelerate()

car2.accelerate()

my_info = {
    "name": "Suraj",
    "collage": "BCA",
    "year": 1
}

print(my_info["name"])
print(my_info["year"])

# Ab ek nayi key add karo dictionary main
my_info["skill"] = "python"
print(my_info)
