from Furniture import Furniture, Chair, Closet



closet_new = Closet('ЛДСП', 'шкаф', 'Ленина 48', 50000, 10)
print(closet_new)
print(closet_new.buy())
print(closet_new.discount(25))
chair = Chair('пластик', 'стул', 'Ленина 48', 2000, 4)
print()
print(chair)
print(chair.buy())
print(chair.diskount(15))