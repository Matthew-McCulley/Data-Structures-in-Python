"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 Spring 2021
__updated__ = "2021-05-17"
-------------------------------------------------------
"""
from Food import Food


def get_food():
    """
    -------------------------------------------------------
    Creates a food object by requesting data from a user.
    Use: f = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """

    name = input("Name: ")
    origin = int(input(Food.origins()))
    is_vegetarian = input("Vegetarian (Y/N): ")
    if is_vegetarian == "Y":
        is_vegetarian = True
    elif is_vegetarian == "N":
        is_vegetarian = False
    else:
        is_vegetarian = None
    calories = int(input("Calories: "))
    food = Food(name, origin, is_vegetarian, calories)
    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a food object from a line of string data.
    Use: f = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """

    properties = line.split("|")
    properties[1] = int(properties[1])
    if properties[2] == "True":
        properties[2] = True
    elif properties[2] == "False":
        properties[2] = False
    properties[3] = int(properties[3])
    food = Food(properties[0], properties[1],properties[2], properties[3])
    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """
    foods = []
    for line in file_variable:
        foods.append(read_food(line))
    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    for food in foods:
        food.write(file_variable)
    return


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian foods.
    foods is unchanged.
    Use: v = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """

    veggies = []
    for food in foods:
        if food.is_vegetarian == True:
            veggies.append(food)

    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of foods by origin.
    foods is unchanged.
    Use: v = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))


    origins = []
    for food in foods:
        if food.origin == origin:
            origins.append(food)

    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """

    n = 0
    total = 0
    
    for food in foods:
        total += food.calories
        n += 1
    
    avg = total // n
    
    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: a = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    v = by_origin(foods, origin)  
    avg = average_calories(v)

    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of foods, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    
    foods.sort()
    
    print("""Food                                Origin       Vegetarian Calories""")
    print("""----------------------------------- ------------ ---------- --------""")
    
    for food in foods:
        if food.is_vegetarian:
            vegetarian = "True"
        else:
            vegetarian = "False"
        print(f"""{food.name:35} {food.ORIGIN[food.origin]:12} {vegetarian:>10} {food.calories:8}""")
    return


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for foods that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))

    result = []
    
    for food in foods:
        if (origin == -1 or food.ORIGIN[origin] == food.ORIGIN[food.origin]) and (max_cals == 0 or max_cals > food.calories) and (is_veg and food.is_vegetarian or not is_veg):
            result.append(food)
            
    return result