class Character:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def attack(self):
        # Βασική μέθοδος που αναμένεται να υπερκαλυφθεί (override)
        raise NotImplementedError(
            "Η μέθοδος attack πρέπει να υλοποιηθεί στις υποκλάσεις."
        )


class Warrior(Character):
    def attack(self):
        print(f"{self.name} επιτίθεται με σπαθί και προκαλεί 15 μονάδες ζημιάς!")


class Archer(Character):
    def attack(self):
        print(f"{self.name} ρίχνει ένα βέλος και προκαλεί 12 μονάδες ζημιάς!")


def play_turn(characters):
    print("== Γύρος παιχνιδιού ==")
    for character in characters:
        character.attack()


hero1 = Warrior("Valkar")
hero2 = Archer("Sylvaris")
party = [hero1, hero2]
play_turn(party)
