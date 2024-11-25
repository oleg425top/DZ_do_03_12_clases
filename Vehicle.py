class Vehicle:
    def __init__(self, name, mileage):
        self.mileage = mileage
        self.name = name
    def __str__(self):
        return f' марка {self.name}, с пробегом в {self.mileage} километров'
    def  get_vehicle_type(self, count_wheel):
        if isinstance(count_wheel, (int, float)):
            if count_wheel == 2:
                return f'это мотоцикл марки {self.name}'
            elif count_wheel == 3:
                return f'это трицыкл марки {self.name}'
            elif count_wheel == 4:
                return f'это автомобиль марки {self.name}'
            else:
                return f' неизвестный транспорт'
        else:
            raise ValueError('должно быть число')

    def get_vehicle_advice(self):
        if self.mileage <=50000:
            return f'неплохо {self.name} можно брать'
        elif 50001 < self.mileage < 100000:
            return f'{self.name} надо внимательно проверить'
        elif 100001 < self.mileage < 150001:
            return f'{self.name} надо провести полную диагностику'
        elif self.mileage > 150000:
            return f'{self.name} лучше не брать'




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



