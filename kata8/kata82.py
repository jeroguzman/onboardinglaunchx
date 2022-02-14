from numpy import average


planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

moons = planet_moons.values()
total_moons = sum(moons)

planets = planet_moons.keys()
total_planets = len(planets)

average_moons = total_moons / total_planets

print ('There are', total_planets, 'planets in our solar system and', total_moons, 'moons and the average number of moons per planet is', average_moons)