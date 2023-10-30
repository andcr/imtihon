class InvalidTaxiName(Exception):
    pass

class Taxi:
    def __init__(self, taxi_id):
        self.id = taxi_id
        self.driver_name = ""
        self.car_model = ""
        self.license_plate = ""

    def set_driver_info(self, driver_name, car_model, license_plate):
        self.driver_name = driver_name
        self.car_model = car_model
        self.license_plate = license_plate

    def __str__(self):
        return f"Taxi ID: {self.id}\nDriver: {self.driver_name}\nCar Model: {self.car_model}\nLicense Plate: {self.license_plate}"

class TaxiCompany:
    def __init__(self, name):
        self.name = name
        self.available_taxis = []
        self.used_taxis = []

    def add_taxi(self, taxi_id):
        if taxi_id in [taxi.id for taxi in self.available_taxis + self.used_taxis]:
            raise InvalidTaxiName(f"Taxi with ID {taxi_id} already exists.")
        
        new_taxi = Taxi(taxi_id)
        self.available_taxis.append(new_taxi)

    def get_available_taxis(self):
        return self.available_taxis

    def get_used_taxis(self):
        return self.used_taxis

    def book_taxi(self, taxi_id):
        for taxi in self.available_taxis:
            if taxi.id == taxi_id:
                self.available_taxis.remove(taxi)
                self.used_taxis.append(taxi)
                return taxi

        raise InvalidTaxiName(f"No taxi found with ID {taxi_id} in {self.name} company.")

    def return_taxi(self, taxi_id):
        for taxi in self.used_taxis:
            if taxi.id == taxi_id:
                self.used_taxis.remove(taxi)
                self.available_taxis.append(taxi)
                return taxi

        raise InvalidTaxiName(f"No used taxi found with ID {taxi_id} in {self.name} company.")

    def display_info(self):
        print(f"Taxi Company: {self.name}")
        print(f"Available Taxis: {len(self.available_taxis)}")
        print(f"Used Taxis: {len(self.used_taxis)}")

my_taxi_company = TaxiCompany("T1")
my_taxi_company.add_taxi(1)
my_taxi_company.add_taxi(2)
my_taxi_company.add_taxi(3)
my_taxi_company.book_taxi(1)
my_taxi_company.display_info()
my_taxi_company.return_taxi(1)
my_taxi_company.display_info()
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
class TaxiManager:
    def __init__(self):
        self.available_taxis = []
        self.used_taxis = []
        self.lost_trips = 0

    def add_taxi(self, taxi_id):
        if taxi_id in [taxi.id for taxi in self.available_taxis + self.used_taxis]:
            raise InvalidTaxiName(f"Taxi with ID {taxi_id} already exists.")
        
        new_taxi = Taxi(taxi_id)
        self.available_taxis.append(new_taxi)

    def get_lost_trips(self):
        return self.lost_trips

    def call_taxi(self, passenger):
        for taxi in self.available_taxis:
            if taxi.passenger is None:
                taxi.begin_trip(passenger)
                self.available_taxis.remove(taxi)
                self.used_taxis.append(taxi)
                return taxi
        self.lost_trips += 1
        return None

    def terminate_trip(self, taxi):
        if taxi not in self.used_taxis:
            raise InvalidTaxiName(f"This taxi is not in the used taxis list.")
        taxi.terminate_trip()
        self.available_taxis.append(taxi)
        self.used_taxis.remove(taxi)

manager = TaxiManager()

manager.add_taxi(1)
manager.add_taxi(2)
manager.add_taxi(3)
home = Place("Yunusobod", "Ming Urik")
work = Place("Mirzo-Ulug'bek", "Mustaqillik Maydoni")

passenger1 = home
passenger2 = work

trip1 = manager.call_taxi(passenger1)
trip2 = manager.call_taxi(passenger2)

manager.terminate_trip(trip1)
manager.terminate_trip(trip2)

print("Available Taxis:")
for taxi in manager.available_taxis:
    print(taxi)
print("\nUsed Taxis:")
for taxi in manager.used_taxis:
    print(taxi)
print(f"\nLost Trips: {manager.get_lost_trips()}")
