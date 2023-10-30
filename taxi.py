from T1axi import TaxiCompany
from Place import Place
from taximeneger import manager
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
