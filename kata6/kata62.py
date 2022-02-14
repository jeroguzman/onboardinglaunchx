planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

planet = input('Enter a planet name with Capital Initial Letter: ')

index = planets.index(planet)

print (index, 'is the index of', planet)

print ('Planets closer to the sun than: ', planet, planets[:index])

print ('Planets farther from the sun than: ', planet, planets[index+1:])