air_temp = float(input("Enter the air temperature measurement"))
air_speed = float(input("Enter the wind speed measurement"))
windchill = 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16
print(windchill)

print("Temperature of 10 and the speed of 15 gives windchill of: -6.5895344209562525")
print("Temperature of 0 and the speed of 25 gives windchill of: -24.093780999553864")
print("Temperature of -10 and the speed of 35 gives windchill of: -41.16894662953316")
print(f"Temperature: {air_temp}")
print(f"Speed: {air_speed}")
print(f"Windchill: {windchill}")
