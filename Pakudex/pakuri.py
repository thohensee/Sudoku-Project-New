class pakuri:

    def __init__(self, species):
        self.__species = species
        self.__attack = (len(species) * 7) + 9
        self.__defense = (len(species) * 5) + 17
        self.__speed = (len(species) * 6) + 13

    def get_species(self):
        return self.__species

    def get_attack(self):
        return self.__attack

    def get_defense(self):
        return self.__defense

    def get_speed(self):
        return self.__speed

    def set_attack(self, new_attack):
        self.__attack = new_attack

    def set_species(self, species):
        self.__species = species

    def evolve(self):
        self.__attack *= 2
        self.__defense *= 4
        self.__speed *= 3