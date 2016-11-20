class Office_furniture(object):
    """
    This class defines a generic animal object
    Attributes: Material, Length, Width, Height, Price, Cuteness, Category
    """

    # in my __init__() function I am using "Hidden" attribute names
    def __init__(self, material, length, width, height, price, cute, category):
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price
        self.__cute = cute
        self.__category = category

    def __str__(self):
        if self.__cute:
            return 'The {0} is made of {1} and is very {2}.'.format(self.__category, self.__material,self.__cute)
        else:
            return 'The {0} is made of {1} and is not very {2}.'.format(self.__category, self.__material,self.__cute)

        # setters and getters
        # Set methods set a value for a hidden attribute
        # get methods return the value of a hidden value

    def set_material(self,material):
        self.__material = material      # don't forget to make it hidden!

    def get_material(self):
            return self.__material

    def set_length(self, length):
        self.__length = length

    def get_length(self):
            return self.__length

    def set_width(self, width):
        self.__width = width

    def get_width(self):
            return self.__width

    def set_height(self, height):
        self.__height = height

    def get_height(self):
            return self.__height

    def set_price(self, price):
        self.__price = price

    def get_price(self):
            return self.__price

    def set_cute(self, cute):
        self.__cute = cute

    def get_cute(self):
            return self.__cute

    def set_category(self, category):
        self.__category = category

    def get_category(self):
            return self.__category

# The class dog inherits Animal

class Desk(Office_furniture):
    """
    attributes: drawer_location, number_drawers
    inherited attribute: category, material, cute
    """



    # When I initialize my object I need to make sure both parent and child attributes are set
    def __init__(self, drawer_location, number_drawers):
        Office_furniture.__init__(self, 'wood', '35in', '30in', '15in', '$40', 'cute','Desk')       # this statement inits parent attribute
        self.__drawer_location = drawer_location
        self.__number_drawers = number_drawers

    # this method overrides the parent class method
    def __str__(self):
        desc = 'There are {0} drawers on the {1} side of the desk. '.format(self.__drawer_location, self.__number_drawers)
        desc += Office_furniture.__str__(self)
        return desc


    def set_drawer_location(self, drawer_location):
        self.__drawer_location = drawer_location

    def get_drawer_location(self):
        self.__drawer_location

    def set_number_drawers(self, number_drawers):
        self.__number_drawers = number_drawers

    def get_number_drawers(self):
        self.__number_drawers

