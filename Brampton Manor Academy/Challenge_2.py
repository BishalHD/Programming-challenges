print("Richter         Joules                          TNT")
print("1                1995262.3149688789      0.00047687913837688307")
print("5.0              1995262314968.8828      476.87913837688404")
print("9.1              2.818382931264449e+18   673609687.2046962")
print("9.2              3.981071705534953e+18   951498973.5982201")
print("9.3              5.623413251903491e+18   1344028023.8775074")
print("")

richter_measurement = float(input("Please enter a Richter scale value:"))
print(f"Richter value {richter_measurement}")
def richter_measurement_to_energy (richter_measurement):
    energy = 10**((1.5*richter_measurement)+4.8)
    return energy
print(f"Equivalence in joules: {richter_measurement_to_energy (richter_measurement)}")

def richter_measurement_to_ton (richter_measurement):
    ton = (10**((1.5*richter_measurement)+4.8))/(4.184*(10**9))
    return ton
print(f"Equivalence in tons of TNT: {richter_measurement_to_ton (richter_measurement



