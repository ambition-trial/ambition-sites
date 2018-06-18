from .sites import ambition_sites


def get_site_id(name):
    try:
        return [site for site in ambition_sites if site[1] == name][0][0]
    except IndexError:
        return [site for site in ambition_sites if site[2] == name][0][0]
