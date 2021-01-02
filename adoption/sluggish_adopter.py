import math
from random import uniform
from adoption.adopter import Adopter

class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelling. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    """

    def __init__(self, name, desired_species, mylocation):
        """
        Initializes the name of the Sluggish Adopter, the specie of interest,
        and the Sluggish adopter's location.
        The SluggishAdopter class also inherits the Adopter class.

        args:
            desired_species: the specie of interest
            mylocation: the Sluggish adopter's location
        """
        Adopter.__init__(self, name, desired_species)
        self.mylocation = mylocation


    def get_linear_distance(self, adoption_center):
        """
        Computes the linear distance between the SluggishAdopter, and the 
        Adoption Center.
        args:
            adoption_center: the name of the Adoption Center
        returns:
            the distance between the Sluggish adopter and the
            adoption center

        """
        x = adoption_center.location.get_X() - self.mylocation.get_X()
        y = adoption_center.location.get_Y() - self.mylocation.get_Y()
        dist = math.sqrt(pow(x, 2) + pow(y, 2))
        return dist


    def get_score(self, adoption_center):
        """
        Computes the Adoption center's score for the Sluggish Adopter.
        The score is computed as follows:
            If distance < 1 return 1 x number of desired species
            elif distance < 3 return random between (.7, .9) times number of desired species
            elif distance < 5. return random between (.5, .7 times number of desired species
            else return random between (.1, .5) times number of desired species

        args:
            adoption_center: the name of the Adoption center
        returns:
            the Adoption center's score for what the Sluggish adopter is able to adopt.
        """
        adopter = Adopter(self.name, self.desired_species)
        dist = self.get_linear_distance(adoption_center)

        if dist < 1:
            score = 1 * adopter.get_score(adoption_center)
        elif dist < 3 and dist >= 1:
            score = uniform(0.7, 0.9) * adopter.get_score(adoption_center)
        elif dist < 5 and dist >= 3:
            score = uniform(0.5, 0.7) * adopter.get_score(adoption_center)
        else:
            score = uniform(0.1, 0.5) * adopter.get_score(adoption_center)

        return round(score, 2)