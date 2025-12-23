# Class daddy
class Vehicle:
    def delivery_cost(self, distance_km):
       return 0
# class son
class Bike(Vehicle):
    def delivery_cost(self, distance_km):
        mocua = 8000
        phi_km = 3000
        return mocua + phi_km * distance_km
class Motorbike(Vehicle):
    def delivery_cost(self, distance_km):
        mocua = 9000
        phi_km = 5000
        return mocua + phi_km * distance_km
class Car(Vehicle):
    def delivery_cost(self, distance_km):
        mocua = 15000
        phi_km = 10000
        return mocua + phi_km * distance_km
# in giá
def print_quote(vehicle, distance):
    cost = vehicle.delivery_cost(distance)
    print(f"chi phí là: {vehicle.__class__.__name__}: {cost} VND cho {distance} km")
# đa hình
vehicles = [Bike(),Motorbike(),Car()]
distance = int(input("nhập số km đi: "))
for i in vehicles:
    print_quote(i, distance)