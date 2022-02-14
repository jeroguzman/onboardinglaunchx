new_planet = input('Enter a planet name: ')
planets = []

while new_planet.lower() != 'done':
    planets.append(new_planet)
    new_planet = input('Enter a planet name if you finish enter the word done: ')


print(planets)

