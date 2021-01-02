from adoption.adopter import Adopter

class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    """
    def __init__(self, name, desired_species, feared_species):
        """
        Initializes the name of the fearful adopter, the specie of interest,
        and a list of other species that the flexible adopter is fearful of.

        args:
            desired_species: the specie of interest
            feared_species: a list species the adopter is afraid of.
        """
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species


    def get_score(self, adoption_center):
        """
        Computes the Adoption center's score for the Fearful Adopter.
        The score is one times the number of desired species minus 0.3 times
        the number of feared species.

        args:
            adoption_center: the name of the Adoption center
        returns:
            the Adoption center's score for what the fearful adopter is able to adopt.
        """
        num_feared = 0
        adopter = Adopter(self.name, self.desired_species)

        for specie in self.feared_species:
            if specie in adoption_center.species_types:
                num_feared += adoption_center.get_number_of_species(specie)

        score = adopter.get_score(adoption_center) - 0.3 * num_feared
        return score