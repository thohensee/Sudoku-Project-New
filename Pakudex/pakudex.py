from Pakudex import pakuri

class pakudex:

    def __init__(self, capacity=20):
        self.__capacity = capacity
        self.__num_pakuri = 0
        self.__pakuri_list = []

    def get_pakuri_list(self):
        return self.__pakuri_list

    def get_size(self):
        return self.__num_pakuri

    def get_capacity(self):
        return self.__capacity

    def get_species_array(self):
        species_array = []

        for item in self.get_pakuri_list():
            species_array.append(item.get_species())

        return species_array

    def get_stats(self, species):
        stats = []
        i = self.get_species_array().index(species)
        stats.append(self.get_pakuri_list()[i].get_attack())
        stats.append(self.get_pakuri_list()[i].get_defense())
        stats.append(self.get_pakuri_list()[i].get_speed())

        return stats

    def sort_pakuri(self):
        sort = sorted(self.get_species_array())

        for i in range(len(self.__pakuri_list)):
            self.__pakuri_list[i].set_species(sort[i])

        return sort

    def add_pakuri(self, species):
        _pakuri = pakuri.pakuri(species)
        self.__pakuri_list.append(_pakuri)
        self.__num_pakuri += 1

    def evolve_species(self, species):
        i = self.get_species_array().index(species)
        self.__pakuri_list[i].evolve()

