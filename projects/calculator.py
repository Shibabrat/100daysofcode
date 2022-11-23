from calculator_art import logo
# import only system from os
from os import system, name
  
def clear():
    # define our clear function: https://www.geeksforgeeks.org/clear-screen-python/
    
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


operations = ["+","-","*","/"]

def operate(operationPicked, numbers):

    if operationPicked == operations[0]:
        result = numbers[0] + numbers[1]
    elif operationPicked == operations[1]:
        result = numbers[0] - numbers[1]
    elif operationPicked == operations[2]:
        result = numbers[0] * numbers[1]
    elif operationPicked == operations[3]:
        result = numbers[0] / numbers[1]
    else:
        print("Invalid operation, please choose from available operations")
        return
    
    return result


continueCalc = 'n'
while continueCalc == 'n':
    print(logo)
    firstNum = float(input("What's the first number?: "))
    print("+" + "\n" + "-" + "\n" + "*" + "\n" + "/")
    
    continueCalc = 'y'
    while continueCalc == 'y':
        
        operationPicked = input("Pick an operation: ")
        nextNum = float(input("What's the next number?: "))
        result = operate(operationPicked, [firstNum, nextNum])

        if result != None:
            print(f"{firstNum} {operationPicked} {nextNum} = {result}")
        else:
            print("Restarting calculator ...")
            continueCalc = 'n'
            clear()
            break
        
        continueCalc = input(f"Type 'y' to continue calculating with {result} or type 'n' to start with a new calculation: ")
    
        if continueCalc == 'y':
            firstNum = result
        elif continueCalc == 'n':
            clear()
        

