import imp
from T1axi import TaxiCompany
from taximeneger import manager
from Place import Place
my_taxi_company = TaxiCompany("Taxi")
my_taxi_company.add_taxi(1)
my_taxi_company.add_taxi(2)
my_taxi_company.add_taxi(3)
my_taxi_company.book_taxi(1)
my_taxi_company.display_info()
my_taxi_company.return_taxi(1)
my_taxi_company.display_info()



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
