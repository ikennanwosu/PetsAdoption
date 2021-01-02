class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        """
        Initializes the name, the types of 
        species and location of the Adoption center.
        """
        self.name = name
        self.species_types = species_types
        self.location = location


    def get_number_of_species(self, animal):
        """
        args:
            animal: a specific animal in the Adoption center

        returns:
            the number of a given species that the adoption center has
        """
        if animal in self.species_types:
            return self.species_types[animal]


    def get_location(self):
        """
        Returns the location of the adoption center
        """
        return self.location
        

    def get_species_count(self):
        """
        Returns a copy of the full list and count of the available 
        species at the adoption center
        """
        species_count = 0
        species = []
        for specie in self.species_types.keys():
            species_count += self.species_types[specie]
            species.append(specie.title())
        return [{"Number of Species" : species_count}, self.species_types.copy()]


    def get_name(self):
        """
        Returns the name of the adoption center
        """
        return self.name


    def adopt_pet(self, species):
        """
        Decrements the value of a specific species at the adoption 
        center and does not return anything.
        args:
            species: species in the Adoption center

        """
        for specie in species:
            if specie in self.species_types.keys():
                self.species_types[specie] -= 1
        self.species_types = {specie:count for specie, count in self.species_types.items() if count != 0}