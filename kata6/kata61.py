from numpy import append


planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']

print (planets, len(planets), 'planets in our solar system')

planets.append('pluto') # add pluto to the end of the list

print (len(planets), 'planets in our solar system and the last planet is: ', planets[-1])
