rods = float(input("Input rods"))

print(f"You input {rods} rods")
print("")
print("Conversion")

def rods_to_meters (rods):
    meters = rods * 5.0292
    return meters
print(f"Meters: {rods_to_meters (rods)}")

def rods_to_feet (rods):
    feet = (rods * 5.0292)/0.3048
    return feet
print(f"Feet: {rods_to_feet (rods)}")

def rods_to_miles (rods):
    miles = (rods * 5.0292)/1609.34
    return miles
print(f"Miles: {rods_to_miles (rods)}")

def rods_to_furlong (rods):
    furlongs = rods/40
    return furlongs
print(f"Furlongs: {rods_to_furlong (rods)}")

def minutes_to_walk (rods):
    time_m_to_walk = ((rods * 5.0292)/1609.34)/(3.1/60)
    return time_m_to_walk
print(f"Minutes to walk {rods} rods: {minutes_to_walk (rods)}")


