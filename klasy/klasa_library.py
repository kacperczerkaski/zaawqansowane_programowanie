class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
    def __str__(self):
        return f"Biblioteka znajduje sie w {self.city}, przy ulicy {self.street}, {self.zip_code}. " \
               f"Biblioteka jest otwarta w godzinach {self.open_hours}. Numer kontaktowy: {self.phone}"
