from Vehicle import Vehicle

BMW = Vehicle('BMW',150000)
Audi = Vehicle('Audi',200000)
Suzuki = Vehicle('Suzuki',50000)
SkyBord = Vehicle('SkyBord',30000)
print(Audi)
print(Audi.get_vehicle_type(4))
print(Audi.get_vehicle_advice())
print(BMW)
print(BMW.get_vehicle_type(4))
print(BMW.get_vehicle_advice())
print(Suzuki)
print(Suzuki.get_vehicle_type(2))
print(Suzuki.get_vehicle_advice())
print(SkyBord)
print(SkyBord.get_vehicle_type(3))
print(SkyBord.get_vehicle_advice())