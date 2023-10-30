from taxi import InvalidTaxiName
from taxi import Taxi
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