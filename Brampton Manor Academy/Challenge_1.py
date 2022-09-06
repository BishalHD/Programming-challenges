rods = float(input("Enter the distance in rods"))

print(f"You input {rods} rods")

print("Conversion")
def conversion (rods):
    meters = rods * 5.0292
    feet = meters/0.3048
    miles = meters/1609.34
    furlongs = rods/40
    time_m_to_walk = miles/(3.1/60)
    return meters, feet, miles, furlongs, time_m_to_walk 

print(conversion(rods))
