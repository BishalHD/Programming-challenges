def richter_measurement_to_energy (richter_measurement):
    energy = 10**((1.5*richter_measurement)+4.8)
    return energy

def richter_measurement_to_ton (richter_measurement):
    ton = (10**((1.5*richter_measurement)+4.8))/(4.184*(10**9))
    return ton

print("Richter         Joules                          TNT")
print(f"{1.0:<10}{richter_measurement_to_energy(1.0):<30}{richter_measurement_to_ton(1.0):<30}")
print(f"{5.0:<10}{richter_measurement_to_energy(5.0):<30}{richter_measurement_to_ton(5.0):<30}")
print(f"{9.1:<10}{richter_measurement_to_energy(9.1):<30}{richter_measurement_to_ton(9.1):<30}")
print(f"{9.2:<10}{richter_measurement_to_energy(9.2):<30}{richter_measurement_to_ton(9.2):<30}")
print(f"{9.3:<10}{richter_measurement_to_energy(9.3):<30}{richter_measurement_to_ton(9.3):<30}")
print("")




richter_measurement = float(input("Please enter a Richter scale value:"))
print(f"Richter value {richter_measurement}")

print(f"Equivalence in joules: {richter_measurement_to_energy (richter_measurement)}")

print(f"Equivalence in tons of TNT: {richter_measurement_to_ton (richter_measurement)}")



