'''Example of data
    name = "Moon"
    gravity = 0.00162 # in kms
    planet = "Earth"
'''

name = input("Name of moon? ")
gravity = float(input("Gravity of moon? "))
planet = input("Name of planet? ")

title = f'Gravity of {name} from {planet}'

facts = f"""{'-'*len(title)}
Planet name: {planet} 
Gravity on {name}: {gravity * 1000} m/s2 
"""

template = f"""{title.title()} 
{facts} 
""" 
new_template = """
Gravity of {name} from {planet}
--------------------------------
Planet name: {planet}
Gravity on {name}: {gravity} m/s2
"""

print(new_template.format(name=name, planet=planet, gravity=gravity*1000))
