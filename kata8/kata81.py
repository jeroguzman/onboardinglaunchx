planet = {
    'name': 'Mars',
    'moons': 2
}

print ('The name of the planet is:', planet.get('name'), 'and it has', planet.get('moons'), 'moons')

planet['circumference'] = {'polar': '6752', 'equatorial': '6792'}

print ('The polar circumference of the planet is:', planet.get('circumference').get('polar'))

