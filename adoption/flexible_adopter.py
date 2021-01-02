from adoption.adopter import Adopter

class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter has one type of species that they desire,
    but they are also alright with considering other types of species.
    """
    def __init__(self, name, desired_species, considered_species):
        """
        Initializes the name of the flexible adopter, the specie of interest,
        and a list of other species that the flexible adopter is willing to
        adopt if the desired specie is not available.
        The FlexibleAdopter also inherits the Adopter class.

        args:
            desired_species: the specie of interest
            considered_species: a list of other species the adopter will consider
        """
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species


    def get_score(self, adoption_center):
        """
        Computes the Adoption center's score for the Flexible Adopter.
        The score is the number of desired species in the adoption center
        plus 0.3 times the number of other species the adopter is willing
        to consider in the Adoption center.

        args:
            adoption_center: the name of the Adoption center
        returns:
            the Adoption center's score for what the flexible adopter is able to adopt.
        """

        num_other = 0
        adopter = Adopter(self.name, self.desired_species)

        for specie in self.considered_species:
            if specie in adoption_center.species_types:
                num_other += adoption_center.get_number_of_species(specie)

        score = adopter.get_score(adoption_center) + 0.3 * num_other
        return round(score, 2)