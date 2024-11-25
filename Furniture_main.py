from Furniture import Furniture


chair = Furniture('стул', 'дсп', 1500)
closet = Furniture('шкаф', 'дерево', 25000)
print(chair)
print(chair.diskount(15))
print(closet)
print(closet.diskount(25))