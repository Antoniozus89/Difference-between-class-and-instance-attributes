class Building:
    Total = 0
    def __init__(self):
        Building.Total += 1

    def __str__(self):
        return f'Building{Building. Total}'

for i in range(40):
    building = Building()
    print(building)
