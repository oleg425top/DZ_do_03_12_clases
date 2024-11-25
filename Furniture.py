class Furniture:
    def __init__(self, type, material, prise):
        self.type = type
        self.material = material
        self.prise = prise


    def __str__(self):
        return f'Это {self.type} из материала {self.material}, цена изделия {self.prise} рублей'


    def buy(self):
        return f'вы купили {self.type} за {self.prise} рублей'

    def diskount(self, diskount):
        self.prise -= (self.prise / 100) * diskount
        return f'вы купили {self.type} за {self.prise} рублей cо скидкой в {diskount} процентов'

