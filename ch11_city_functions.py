"""module holding function that prints proper place name"""
# function for exercise 11-1
# def city_country(city, country):
#     """returns string featuring proper place name"""
#     combination = f"{city.title()}, {country.title()}"
#     return combination

# function for exercise 11-2a --> expect test failure
# def city_country(city, country, population):
#     """returns string featuring proper place name"""
#     combination = f"{city.title()}, {country.title()} - population"\
#                   f"{population}"
#     return combination


# function for exercise 11-2b --> modify function so population optional
def city_country(city, country, population=None):
    """returns string featuring proper place name"""
    if population:
        combination = f"{city.title()}, {country.title()} - population "\
                    f"{population}"
    else:
        combination = f"{city.title()}, {country.title()}"
    return combination
