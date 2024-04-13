#11.1
#11.2
def format_city_country(city, country, population=None):
    formatted_string = f"{city.title()}, {country.title()}"
    if population:
        formatted_string += f" - population {population}"
    return formatted_string