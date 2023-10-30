from taxi import InvalidTaxiName
from T1axi import Taxi
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