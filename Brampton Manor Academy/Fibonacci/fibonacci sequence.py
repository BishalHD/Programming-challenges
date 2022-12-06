import json

def fibonacci(array):
    for i in range(0,33):
        if i > 1:
            array.append(array[i-2]+array[i-1])
        else:
            array.append(i)
    return array

def check(array, user_input, num, calculation):
    for item in array:
        if item<= user_input:
            sublist = []
            sublist.append(item)
            num = sublist[0]
    calculation = 100 - int(num)
    return num, calculation

def loop(array, calculation, num):
    final_list = []
    for each in array:
        if calculation == each:
            final_list.append(num)
        else:
            user_input = calculation
            num, calculation = check(array, user_input, num, calculation)
            final_list.append(num)
    return final_list



if __name__ == "__main__":
    array = []
    num = 0
    calculation = 0
    user_input = int(input("..."))
    sequence =fibonacci(array)

    #with open('Fibonacci_sequence', 'w') as f:
        #f.write(json.dumps(sequence))

    #with open('Fibonacci_sequence', 'r') as f:
        #sequence = json.loads(f.read())

    num, calculation = check(array, user_input, num, calculation)
    print(num)
    print(calculation)
    final_list = loop(array, calculation, num)
    print (final_list)

