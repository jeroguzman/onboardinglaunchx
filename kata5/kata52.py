from turtle import distance


planet1 = int(input("Enter planet 1 distance to sun in KM: "))
planet2 = int(input("Enter planet 2 distance to sun in KM: "))

distance = planet2 - planet1
print("The distance between the two planets is", distance, "km")

distanceMiles = distance * 0.621371
print("The distance in miles is", abs(distanceMiles), "miles")
