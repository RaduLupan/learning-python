planet = {
    #'name': 'Earth',
    #'moons': 1
}

planet['name']='Jupiter'
planet['moons']=79

print(planet)

# pop return the value and removes the key
moons=planet.pop('moons')
print(moons)
print(planet)