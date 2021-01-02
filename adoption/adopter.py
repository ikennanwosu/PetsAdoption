class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        """
        Initializes the name of the Adopter, and the Adopter
        specie of interest.
        """
        self.name = name
        self.desired_species = desired_species


    def get_name(self):
        """
        Gets the name of the Adopter
        """
        return self.name


    def get_desired_species(self):
        """
            Gets the name of the Adopter's 
            specie of interest.
        """
        return self.desired_species
        

    def get_score(self, adoption_center):
        """
        Computes a score for the Adoption center
        based on the number of the Adopter's 
        specie of interest that the Adoption
        center has available.
        args:
            adoption_center: the name of the Adoption Center

        """
        try:
            # Get the score if the Adoption Center has the desired pet
            score = 1 * adoption_center.get_number_of_species(self.desired_species)
        except TypeError:
            # If Adoption Center does not have the desired, inform the user and set score is 0
            score = 0
            print("{} does not have a {} for {}.".format(adoption_center.get_name(), self.desired_species.title(), self.get_name()))
        return score