from adoption.adopter import Adopter
from adoption.allergic_adopter import AllergicAdopter

class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A Medicated Allergic Adopter is extremely allergic to a particular species.
    However, they have a medicine of varying effectiveness, which will be 
    given in a dictionary.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        """
        Initializes the name of the Medicated Allergic Adopter, the specie of interest,
        a list of species the adopter is allergic to, and the medicine effectiveness against
        each specie they are allergic to.
        The MedicatedAllergicAdopter class also inherits the Adopter class.

        args:
            desired_species: the specie of interest
            alllergic_species: a list of species the adopter is allergic to
            medicine_effectiveness: effectiveness of medication to allergies to 
                                    certain species
        """

        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness


    def get_score(self, adoption_center):
        """
        Computes the Adoption center's score for the Medicated Allergic Adopter.

        To calculate the score for a specific adoption center, the function determines
        the most allergy-inducing species that the adoption center has for a particular 
        Medicated Allergic Adopter, by first examining what species the Adoption Center has 
        that the Medicated Allergic Adopter is allergic to, then compares that to the 
        medicine_effectiveness dictionary. It then takes the lowest medicine_effectiveness 
        found for these species, and multiplies that value by the Adopter's score method.

        args:
            adoption_center: the name of the Adoption center
        returns:
            the Adoption center's score for what the Medicated Allergic Adopter is able to adopt.
            If the desired specie is not in the Adoption Centre, the function returns the 
            medicine effectiveness score for the species the Adopter is allergic to.
        """
        list_med_eff = []
        allergic_specie_in_center = []

        allergic_adopter = AllergicAdopter(self.name, self.desired_species, self.allergic_species)

        # Check if each specie the MedicatedAllergicAdopter is 
        # allergic to is in the Adoption center
        for allergic_specie in allergic_adopter.allergic_species:
            if allergic_specie in adoption_center.species_types:
                allergic_specie_in_center.append(allergic_specie)
        
        
        if len(allergic_specie_in_center) == 0: # no allergy specie in Adoption center
            med_effectiveness = 1
        else:
            # Get the effectiveness of each allergy specie in the Adoption center       
            for specie, med_eff in self.medicine_effectiveness.items():
                if specie in allergic_specie_in_center:
                    list_med_eff.append(med_eff)

            med_effectiveness = min(list_med_eff)

        # Check if desired specie is in the Adoption Center
        if allergic_adopter.desired_species in adoption_center.species_types:
            score = adoption_center.get_number_of_species(self.desired_species) * med_effectiveness
        else:
            score = med_effectiveness

        return score