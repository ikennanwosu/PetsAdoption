class Location:
    """
    The Location class defines the map coordinates of the Adoption Center.
    """
    def __init__(self, x, y):
        self.x = x # x-coordinates of the Aoption center location
        self.y = y # y-coordinates of the Aoption center location

    def get_X(self):
        return self.x

    def get_Y(self):
        return self.y