# def mission_info(PreLaunchTime, FlightTime, Destination, ExternalTank, InternalTank):

#     return f"""
#     Destination: {Destination}.
#     Travel Time: {PreLaunchTime + FlightTime} minutes.
#     Fuel Left: {ExternalTank + InternalTank} gallons.
#     """
 
# def mission_info(Destination, *minutes, **fuel_reservoirs):
#     return f"""
#     Destination: {Destination}
#     Travel time: {sum(minutes)} minutes
#     Fuel left: {sum(fuel_reservoirs.values())}
#     """

# print(mission_info("Moon", 5, 20, 100, main=100, external=50))

def mission_info(Destination, *minutes, **fuel_reservoirs):
    report = f"""
    Destination: {Destination}
    Travel time: {sum(minutes)} minutes
    Fuel left: {sum(fuel_reservoirs.values())}
    """
    for tank, gallons in fuel_reservoirs.items():
        report += f"\n{tank}: {gallons} gallons"
    return report

print(mission_info("Moon", 5, 20, 100, Internal=100, External=50))

