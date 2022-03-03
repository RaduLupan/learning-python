def rocket_parts():
    print("payload, propellant, structure")

rocket_parts()

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"

result=distance_from_earth("Moon")
print(result)

result=distance_from_earth("Jupiter")
print(result)