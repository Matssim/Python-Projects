

class Building:
    def __init__(self, square_footage, floors, address):
        self.square_footage = square_footage
        self.floors = floors
        self.address = address.index("OR")

Movie_theatre = Building(1000, 3, "8704 N Lombard St, Portland, OR 97203") 


# Step 243 Inheritance Challenge
class Restaurant(Building):
    pets_allowed: False


Burgerville = Restaurant(750, 1, "8671 N Ivanhoe St, Portland, OR 97203")










if __name__ == "__main__":
    print(Movie_theatre.address)
    print(Burgerville.square_footage)
