class Property:
    def __init__(self, area: str, rooms: int, price, address: str ):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
    def __str__(self):
        return f"Region: {self.area}, Pokoje: {self.rooms}, Cena: {self.price}, Adres: {self.address}"

class House(Property):
    def __init__(self, area: str, rooms: int, price, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot
    def __str__(self):
        return f"Region: {self.area}, Pokoje: {self.rooms}, Cena: {self.price}, Adres: {self.address}, Rozmiar działki: {self.plot}"

class Flat(Property):
    def __init__(self, area: str, rooms: int, price, address: str, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor
    def __str__(self):
        return f"Region: {self.area}, Pokoje: {self.rooms}, Cena: {self.price}, Adres: {self.address}, Piętro: {self.floor}"

if __name__ == '__main__':

    house = House("wieś", 6, 250000, "Prosta 1", 60)
    flat = Flat("miasto", 3, 300000, "Długa 3", 7)

    print(house)
    print(flat)

