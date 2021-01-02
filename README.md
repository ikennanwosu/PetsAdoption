# Introduction
This project is to help people find their forever friends! It creates a representation of both pet adoption centers and the pet adopters, and assigns scores to each adopter relative to a certain adoption center. A higher score means a specific adopter is more likely to adopt a pet from a specific adoption center.

## Objective
The goal of this problem is to learn about the use of classes, methods, and class inheritance.

## Elements of the Project
The diagram below shows the classes and inheritance flow of the Adoption Center and the Adopters, and are explained in details;

![alt text](https://github.com/ikennanwosu/pet_adoption/blob/master/inheritance_flow.png)

### PART 1: The Adoption Center 
The adoption center class will hold information specific to each adoption center, as well as methods for fetching information from or modifying the adoption center. Such information include:

##### Adoption Center Initialization
- `name`- A string that represents the name of the adoption center.
- `location`- A tuple (x,y) that represents the x and y as floating point coordinates of the adoption center location.
- `species_types`- A string:integer dictionary that represents the number of specific pets that each adoption center holds. An example would be: `{"Dog": 10, "Cat": 5, "Lizard": 3}`, and another example would be `{"Cat": 10, "Horse": 8}`. Species names will always begin with a capital letter followed by lowercase letters, so you do not have to check for the case of the species name ('Cat' will never be stored as 'cat' or 'cAT' etc). Note that the specific animals tracked depend on the adoption center. If an adoption center does not have any of a specific species up for adoption, it will not be represented in the dictionary

##### Adoption Center Methods
- `get_name()`- Returns the name of the adoption center
- `get_location()`-Returns the location of the adoption center
- `get_species_count()`- Returns a copy of the full list and count of the available species at the adoption center.
- `get_number_of_species(species_name)`- Returns the number of a given species that the adoption center has.
- `adopt_pet(species_name)`- Decrements the value of a specific species at the adoption center and does not return anything.

### PART 2: The Adopter
There are a few types of potential adopters. The base class of the adopters is simply called "Adopter". The Adopter class will contain information that will be shared among all types of adopters.

##### Adopter Initialization
- `name`- A string that represents the name of the adopter
- `desired_species`- A string that represents the desired species to adopt

##### Adopter Methods
- `get_name()`- Returns the name of the adopter
- `get_desired_species()`- Returns the desired species of the adopter
- `get_score(adoption_center)`- Returns the score (details below)

##### About Scoring
Each `Adopter` class, and each `Adopter` subclass will have its own scoring methods. The minimum value that a score can be is 0, and there is no upper bound. The score method will take in an `adoption_center` as its argument, and will do some calculations to determine how good of a fit the specific adopter is to the specific adoption center.

For the base `Adopter` class, this score will be **1 * _num_desired_**, where **_num_desired_** is the number of the adopter's desired species that the adoption center has.
With the adopter class defined, we want to represent different personalities and traits, which will be subclasses of the base `Adopter` class.

### The Flexible Adopter
The `FlexibleAdopter` varies from the regular Adopter because a `FlexibleAdopter` is able to specify more than one specie that they are interested in, but will still have one preferred specie. The `FlexibleAdopter` is a **subclass of the** Adopter **class**, and should inherit from it and only it.

All of the inputs are the same as the `Adopter` class, _except_ that `considered_species` is a **list of strings** of alternative species that the person is interested in adopting.

The `FlexibleAdopter`'s scoring method also differs from the `Adopter`'s scoring method, in that a score calculated on a `FlexibleAdopter` will return a value that is the result of **_adopter_score_ + 0.3 * _num_other_** where:

- **_adopter_score_** is the value that the `Adopter` class's score method returns
- **_num_other_** is the number of animals the adoption center has of all the other considered species

### The Fearful Adopter
The `FearfulAdopter` varies from the regular `Adopter` because a `FearfulAdopter` is afraid of one certain specie of animal. While they may visit an `AdoptionCenter` that houses one or more of the feared species, their enthusiasm to visit the `AdoptionCenter` is reduced. The `FearfulAdopter` is a **subclass of the** `Adopter` **class**, and should inherit from it and only it.

All of the inputs are the same as the `Adopter` class, _except_ that `feared_species` is a **string** that is the name of the feared species.

The `FearfulAdopter`'s scoring method also differs from the `Adopter`'s scoring method, in that a score calculated on a `FearfulAdopter` will return a value that is the result of **_adopter_score_ - 0.3 * _num_feared_**  where:
- **_adopter_score_** is the value that the `Adopter` class's score method returns
- **_num_feared_** is the number of animals the adoption center has of the feared species


### The Allergic Adopter
The `AllergicAdopter` varies from the regular `Adopter` because an `AllergicAdopter` is extremely allergic to one or more particular species and cannot be around them even a little bit! If the adoption center contains one or more of those animals, they will not be able to go there. The `AllergicAdopter` is a **subclass of the* `Adopter` **class**, and should inherit from it and only it.

All of the inputs are the same as the `Adopter` class, _except_ that `allergic_species` is a **list of strings** of one or more species that the adopter is allergic to.

The `AllergicAdopter`'s scoring method also differs from the `Adopter`'s scoring method, in that a score calculated on an `AllergicAdopter` will return a value that is 0 if the adoption center has one or more of a species that the adopter is allergic to, otherwise it should calculate score based on the `Adopter`'s score method return value. 

### The Medicated Allergic Adopter 
The `MedicatedAllergicAdopter` varies from the `AllergicAdopter` as they have medicine to lessen their allergies. The `MedicatedAllergicAdopter` is a **subclass of the** `AllergicAdopter` **class**.

All of the inputs are the same as the `AllergicAdopter` class, _except_ that medicine_effectiveness is a **dictionary of {string: float}** of the medicines effectiveness to certain species. The effectiveness can range from 0.0 (no effectiveness against allergies) to 1.0 (full effectiveness against allergies).

For example, medicine_effectiveness may look like `{"Dog": 0.5, "Cat": 0.0, "Horse": 1.0}`, which means there is a medium effectiveness against dog allergies, no effectiveness against cat allergies, and full effectiveness against horse allergies.

The `MedicatedAllergicAdopter`'s scoring method also differs from the `AllergicAdopter`'s scoring method. Since the `MedicatedAllergicAdopter` is able to prevent against some allergies, they are now able to enter some `AdoptionCenters` they could not before. To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular `MedicatedAllergicAdopter`. [**Hint**: To do this, first examine what species the `AdoptionCenter` has that the `MedicatedAllergicAdopter` is allergic to, then compare them to the medicine_effectiveness dictionary. Take the lowest medicine_effectiveness found for these species, and multiply that value by the `Adopter`'s score method return value.]

Consider the following as an example:
Joe is allergic to dogs and horses, but wants a cat. He takes a medicine that has 0.5 effectiveness against dog allergies, and 1.0 effectiveness against horse allergies. He is considering going to an adoption center that has dogs, cats, and horses. Since the adoption center contains both of his allergies, to calculate his score, we will want to take the lowest effectiveness, that is, the 0.5 effectiveness against dogs, and multiply it by the normal Adopter score. The end score for his would be 0.5 * the base class `Adopter` score.
 
 
 ### The Sluggish Adopter
 The final type of adopter we will consider is the `SluggishAdopter`, and it will extend the base `Adopter` class. A `SluggishAdopter` really dislikes travelling. The further away the adoption center is linearly, the less likely they will want to visit it. Since we are not sure of the specific mood the `SluggishAdopter` will be in on a given day, we will assign their score with a random modifier depending on distance as a guess.
 
The `SluggishAdopter` is a **subclass of the** `Adopter` **class**, and should inherit from it and only it.
 
All of the inputs are the same as the `Adopter` class, _except_ that location is a **tuple of floats** of the (x, y) coordinates, similar to the `AdoptionCenter`'s location variable. The range for the coordinates are -5.0 to 5.0 [could be value really!].

For this adopter, you will have to write an additional class method called `get_linear_distance(to_location)`, which will calculate the linear distance between two points, (x1,y1), (x2,y2) . You will want to calculate the distance by using the following formula:

![alt text](https://github.com/ikennanwosu/pet_adoption/blob/master/formula.png)
 
This will be used calculate the linear distance between the `SluggishAdopter`, and the `AdoptionCenter`.

The `SluggishAdopter`'s scoring method also differs from the `Adopter`'s scoring method. You should override the method so that a score calculated on a `SluggishAdopter` will return a value that is:

- **1 * _the_number_of_desired_species_**, if the distance is less than 1
- **_random_value_between_0.7_and_0.9 * _the_number_of_desired_species_**, if the distance is less than 3 but greater than or equal to 1
- **_random_value_between_0.5_and_0.7 * _the_number_of_desired_species_**, if the distance is less than 5 but greater than or equal to 3
- **_random_value_between_0.1_and_0.5 * _the_number_of_desired_species_**, if the distance is greater than or equal to five.
 
 
 
 ### PART 3: Connecting Adopters and Adoption Centers
 After implementing the above, it's time to try adopting some pets. Two scenarios will be considered, from the `Àdopter`'s perspective and `Àdoption Center`perspective.
 
 #### Help an Adopter visit AdoptionCenters in the Best Order
An Adopter or Adopter Subclass has a list of AdoptionCenters in the area, as well as information on what animals each AdoptionCenter has that day. `get_ordered_adoption_center_list(adopter, list_of_adoption_centers)`method returns a list of an organised `adoption_center`such that the scores for each `Àdoptioncenter`to the `Adopter`will be ordered from the highest score to the lowest score.

#### Help an AdoptionCenter Select Adopters
We want to help organize a list of Adopter types for an AdoptionCenter to send advertisements which will invite them to visit the AdoptionCenter. The AdoptionCenters may have limited funds and can only send out mail to a select few Adopters in their database, so want to select the best candidates to advertise to in order to increase the odds of adoption.

The method, `get_adopters_for_advertisement(adoption_center, list_of_adopters, n)` should return a list of length up to n that represents the highest scoring Adopters/Adopter Subclasses for the specific AdoptionCenter, with the following parameters:

- `adoption_center` - A single `AdoptionCenter` instance
- `list_of_adopters` - A list of `Adopter` (or a subclass of `Adopter`) instances.
- `n` - The number of adopters, up to a maximum of n, who will be sent advertisements. Note that n >= 0 and may be longer than the `list_of_adopters`, in which case less than n advertisements will be sent out.
