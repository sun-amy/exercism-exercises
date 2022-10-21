""" 
Learn the basics of Python by cooking Guido's Gorgeous Lasagna.
"""

EXPECTED_BAKE_TIME = 40

def bake_time_remaining(time_in_oven):
    """By subtracting time already in the oven from the total cooking time, this function return how much time is left before the lasagna is ready."""
    return EXPECTED_BAKE_TIME - time_in_oven

def preparation_time_in_minutes(layers):
    """Each layer takes 2 minutes to prepare, this function takes the number of layers and muliplies it by 2 to calculate the total preparation time."""
    return layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """This function takes two numbers representing the number of layers & the time already spent baking and calculates the total elapsed time in minutes."""
    return number_of_layers * 2 + elapsed_bake_time
