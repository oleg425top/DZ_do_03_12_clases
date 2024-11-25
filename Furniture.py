class Furniture:
    def __init__(self, material, class_of_furniture, address_of_magazine, prise):
        self.prise = prise
        self.address_of_magazine = address_of_magazine
        self.material = material
        self.class_of_furniture = class_of_furniture




class Chair(Furniture):
    def __init__(self, material, class_of_furniture, address_of_magazine, prise,count_legs):
        super().__init__( material, class_of_furniture, address_of_magazine, prise)
        self.count_legs = count_legs
    def __str__(self):
        return f'это {self.class_of_furniture} по адресу {self.address_of_magazine} , из материала {self.material} он стоит {self.prise} и у него {self.count_legs} ножки'

    def buy(self):
        return f'вы купили из {self.material}a {self.class_of_furniture} на {self.address_of_magazine} за {self.prise} рублей у него {self.count_legs} ножек'

    def diskount(self, discount):
        self.prise -= (self.prise / 100) * discount
        return f'вы купили {self.class_of_furniture} за {self.prise} рублей cо скидкой в {discount} процентов'


class Closet(Furniture):
    def __init__(self,material, class_of_furniture, address_of_magazine, prise,count_folders):
        super().__init__(material, class_of_furniture, address_of_magazine, prise)
        self.count_folders = count_folders
    def __str__(self):
        return f' это {self.class_of_furniture} по адресу {self.address_of_magazine} , из материала {self.material} он стоит {self.prise} и у него {self.count_folders} полок'
    def buy(self):
        return f'вы купили из {self.material}a {self.class_of_furniture} на {self.address_of_magazine} за {self.prise} рублей у него {self.count_folders} дверей'

    def discount(self, discount):
        self.prise -= (self.prise / 100) * discount
        return f'вы купили {self.class_of_furniture} за {self.prise} рублей cо скидкой в {discount} процентов'





