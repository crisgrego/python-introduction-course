# class Vehicle:
#     'Base class of all vehicles'
#     def __init__(self, VIN, weight, manufacturer):
#         self.vin_number = VIN
#         self.weight = weight
#         self.manufacturer = manufacturer

#     def get_weight(self):
#         return self.weight
#     def get_manufacturer(self):
#         return self.manufacturer
#     def get_vehicle_type(self):
#         pass

# class Car(Vehicle):
#     def __init__(self, VIN, weight, manufacturer, seats):
#         self.vin_number = VIN
#         self.weight = weight
#         self.manufacturer = manufacturer
#         self.seats = seats
#     def get_number_of_seats(self):
#         return self.seats
#     def get_vehicle_type(self):
#         return 'CAR'

# class Truck(Vehicle):
#     def __init__(self, VIN, weight, manufacturer, capacity):
#         self.vin_number = VIN
#         self.weight = weight
#         self.manufacturer = manufacturer
#         self.capacity = capacity
#     def get_number_of_capacity(self):
#         return self.capacity
#     def get_vehicle_type(self):
#         return 'TRUCK'

# a = Car('ABC1', 1000, 'RENAULT', 4)
# b = Truck('BCD2', 1000, 'MAN', 10000)
# c = Car('TSTS', 1200, 'KIA', 4)
# d = Truck('ZZZ4', 11000, 'CITROEN', 15000)

# print("Car: " + a.get_vehicle_type())
# print("Truck: " + b.get_vehicle_type())