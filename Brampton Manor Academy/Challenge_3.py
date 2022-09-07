print("We are going to play a game. I want you to pick a number then do a series of calculation. I bet I know what the result of those calculations will be!")

answer = int(input("*You* This will be the answer. Select a number between 10-49: "))
factor = 99 - answer

f_answer = int(input("*Player* Pick any number 50-99: "))
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

print("")
print(f"I said the answer was {answer} and the calculation result is {calculation(adding)}")





