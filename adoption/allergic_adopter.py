from adoption.adopter import Adopter

class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    """
    def __init__(self, name, desired_species, allergic_species):
        """
        Initializes the name of the Allergic adopter, the specie of interest,
        and a list of other species that the Allergic adopter is allergic to.

        args:
            desired_species: the specie of interest
            allergic_species: a list of species the adopter is allergic to.
        """
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species


    def get_score(self, adopter_center):
        """
        Computes the Adoption center's score for the Allergic Adopter.

        args:
            adoption_center: the name of the Adoption center
        returns:
            the Adoption center's score for what the Allergic adopter is able to adopt.
            Score should be 0 if the center contains any of the animals the adopter is 
            allergic to, or number of desired animals in the adoption center if not.
        """
        score = 1
        adopter = Adopter(self.name, self.desired_species)

        # loop through all allegic species, if any in specie types 
        # in the adoption center, return 0
        for specie in self.allergic_species:   
            if specie in adopter_center.species_types:
                score = 0
                break
        # if the adoption center does not have any of the allegic species, 
        # return score of having desired specie
        if score != 0:                         
            score = adopter.get_score(adopter_center)
            
        return score