class Place:
    def __init__(self, district, neighborhood):
        self.district = district
        self.neighborhood = neighborhood

    def __str__(self):
        return f"{self.district}, {self.neighborhood}"

class Passenger:
    def __init__(self, current_place):
        self.current_place = current_place

    def get_place(self):
        return self.current_place

home = Place("Yunusobod", "123")
work = Place("Mirzo-Ulug'bek", "Mustaqillik Maydoni")

passenger1 = Passenger(home)
passenger2 = Passenger(work)

current_place1 = passenger1.get_place()
current_place2 = passenger2.get_place()

print(f"Passenger 1's current place: {current_place1}")
print(f"Passenger 2's current place: {current_place2}")