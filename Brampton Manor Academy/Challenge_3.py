import math
answer = int(input("Enter a number between 10 and 49"))
factor = 99 - answer

f_answer = int(input("Enter a number between 50 and 99"))
adding = f_answer + factor

def calculation (adding):
    adding = str(adding)
    hundreds_digit = adding[0]
    other_digits = adding[1:3]
    hundreds_digit = int(hundreds_digit)
    other_digits = int(other_digits)
    total = other_digits + hundreds_digit
    new_total = f_answer - total
    return new_total

print(f"I said the answer was {answer} and the calculation result is {calculation(adding)}")





