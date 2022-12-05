import json

def fibonacci(array):
    for i in range(0,30):
        if i > 1:
            array.append(array[i-2]+array[i-1])
        else:
            array.append(i)
    return array

def check(array, x, calculation,):
    for item in array:
        if item<= x:
            sublist = []
            sublist.append(item)
            num = sublist[0]
    calculation = 100 - int(num)
    return num, calculation

if __name__ == "__main__":
    array = []
    calculation = 0
    x = int(input("..."))
    sequence = fibonacci(array)

    with open('Fibonacci_sequence', 'w') as f:
        f.write(json.dumps(sequence))

    with open('Fibonacci_sequence', 'r') as f:
        sequence = json.loads(f.read())

    z = check(array, x, calculation = None)
    z = str(z)
    z = z[1]
    print(z)
    for j in range (len(array)):
        while z[1]!= array[j]:
            z = check(array, x, calculation = None)
            z = str(z)
            z = z[1]
            print(z)
            
    
