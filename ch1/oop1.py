class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def __str__(self):
        return f"Αυτοκίνητο μάρκας {self.make}, μοντέλου {self.model}, έτους {self.year} με {self.odometer} χιλιόμετρα."

    def update_odometer(self, new_km):
        print(f"Το αυτοκίνητο έχει {self.odometer} χιλιόμετρα. Επιχειρείται να αλλάξουν σε {new_km}.")
        if new_km > self.odometer:
            self.odometer = new_km
        else:
            print("Δεν επιτρέπεται να γυρίσουν πίσω τα χιλιόμετρα.")


a_car = Car("Opel", "Corsa", 2024)
print(a_car)
a_car.update_odometer(1000)
print(a_car)
a_car.update_odometer(900)
print(a_car)
