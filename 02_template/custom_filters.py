import datetime

def reverse(name):
    return name[::-1]

def calculate_birth_year(age):
    current_year = datetime.datetime.now().year
    birth_year = current_year - age
    return birth_year