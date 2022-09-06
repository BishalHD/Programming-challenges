richter_measurement = float(input("Enter Richter scale measurement"))

def conversion (richter_measurement):
    energy = 10**((1.5*richter_measurement)+4.8)
    ton = energy/(4.184*(10**9))
    return richter_measurement, energy, ton

print(conversion(richter_measurement))




