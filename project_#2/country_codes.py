from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    """Returns code of country in two letters."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        elif country_name == 'Yemen, Rep.':
            return 'ye'
    # If there is no country returns None.
    return None
