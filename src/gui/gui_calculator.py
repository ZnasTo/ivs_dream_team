##
# @author xkovacj00, Jakub Kováčik
# @file gui_calculator.py
# @brief This file contains working Graphical User Interface for the calculator
#

from tkinter import *
from tkinter import messagebox
import re
import importlib

root = Tk()

root.title("Calculator")
root.configure(bg = 'Black')

valid_opperands = ["+", "-", "*", "/", "!", "^", "abs", "\u221A", "."]

##  @brief This functions opens a window with help for the user on how to use the calculator
#
def show_help():
    help_text = (
        "Welcome to the Calculator Help!\n\n"
        "Supported operations:\n"
        "  +   Addition\n"
        "  -   Subtraction\n"
        "  *   Multiplication\n"
        "  /   Division\n"
        "  ^   Exponentiation\n"
        "  !   Factorial\n"
        "  abs Absolute value\n"
        "  \u221A  Root\n"
        "  .   Decimal point\n\n"
        "Buttons:\n"
        "  AC  Clear all input\n"
        "  LC  Clear last character\n"
        "  =   Evaluate expression\n\n"
        "Usage:\n"
        "  Addition  N + M : N, M can be negative or positive numbers.\n"
        "  Subtraction  N - M : N, M can be negative or positive numbers.\n"
        "  Multiplication  N * M : N, M can be negative or positive numbers.\n"
        "  Division  N / M : N, M can be negative or positive numbers (M ≠ 0).\n"
        "  Factorial  N! : N must be a non-negative integer.\n"
        "  Power  N ^ M : N can be any number, M should be a non-negative integer.\n"
        "  Absolute value  abs N : Absolute value of N.\n"
        "  Root  N\u221AM : N (positive number) is the degree of the root, M is the number to be rooted.\n"
        "  Decimal number  N.M : N can be can be negative or positive number, M should be non-negative integer.\n\n"
        "Read before using:\n"
        "- Do not use spaces between characters.\n"
        "- To indicate a positive number, there's no need to use '+'. The calculator automatically treats numbers as positive unless stated otherwise.\n"
        "- Calculator supports keyboard inputs, simply click on the box, where numbers and opperations are displayed.\n"
        "- Decimal numbers must be written as '3.14', etc.\n"
        " (Examples of invalid decimal numbers: 1. , .2 , 1.-2)\n"
        "- Absolute value must be followed by a number or negative number.\n"
        "- When Error occurs simply delete the message.\n"
        "- Keyboard Shortcuts: Press enter to evaluate the formula, press backspace to delete last character.\n"
    )
    messagebox.showinfo("Calculator Help", help_text)

##  @brief This function splits user input into array
#
#   @param input everything that user typed into calculator
#   @return it returns either splitted array of opperands and numbers, or 1 in case of invalid input
#
def split_formula(input):
    pattern = r"(\d+|\^|abs|\.|\u221A|[+\-*/!])"        #splitting the array by these opperands
    numbers__and_opperands = re.findall(pattern, input)
    joined = "".join(str(character) for character in numbers__and_opperands)        #joining splitted opperands, for validation

    if joined != input:     #if the strings are not equal, it means there were invalid characters 
        return 1
    
    return numbers__and_opperands

##  @brief This function collets inputs as units
#   @param character input of user
#
def getchar_from_button(character):
    match character:
        case "=":
            splitted_formula = split_formula(entry.get())
            if splitted_formula == 1:
                result = "ERROR: invalid input"
                entry.delete(0, END)
                entry.insert(0, result)
            if not splitted_formula == 1:
                result = count_everything(splitted_formula)
                entry.delete(0, END)
                entry.insert(0, result)
        case "AC":
            entry.delete(0, END)
        case "LC":
            entry.delete(len(entry.get()) - 1, END)
        case _:
            entry.insert(END, character)

##  @brief This function evaluates the formula
#   @param formula array of nubers and opperands
#   @return formula, result of the whole formula, or error message
#
def evaluate_formula(formula):
    math_module = importlib.import_module("math_lib")

    if len(formula) > 0:
        if formula[0] == "+":       #just in case when + at the beginning is indicating positive number, i remove the +
            del formula[0]

    indexes_to_delete = []
    numbers= []
    index_to_append = 0
    string_to_int = 0
    for i,element in enumerate(formula):        #converting string, to integers
        if element.isdigit():
            string_to_int = int(formula[i])
            del formula[i]
            formula.insert(i, string_to_int)
    
    for i,element in enumerate(formula):        #joining floating numbers start
        if element == ".":
            indexes_to_delete.extend([i - 1, i, i + 1])
            whole_part = formula[i -1]
            fractional_part = formula[i + 1]
            numbers.append(float(f"{whole_part}.{fractional_part}"))
    numbers.reverse()       #the first number i will be adding is the last in the original array
    
    for indexes in reversed(indexes_to_delete):
        index_to_append += 1
        if (index_to_append % 3 == 0):
            del formula[indexes]
            formula.insert(indexes, numbers[int((index_to_append/3) -1)])        
            continue      
        del formula[indexes]            #joining floating numbers end
    

    indexes_to_delete = []       #start of abs
    negative_indexes_to_delete = []
    numbers= []
    negative_numbers= []
    for i,element in enumerate(formula):       
        if element =="abs":
            if(formula[i + 1] == "-"):
                negative_indexes_to_delete.extend([i, i + 1, i + 2])
                negative_numbers.append(math_module.abs(float(f"{formula[i+1]}{formula[i+2]}")))
            else:
                indexes_to_delete.extend([i, i+ 1])
                numbers.append(math_module.abs(float(formula[i+1])))
    
    numbers.reverse()
    index_to_append = 0
    for indexes in reversed(indexes_to_delete):         #if i make absolute value of positive number, i have to change the way i delete and insert to array
        index_to_append += 1
        if (index_to_append % 2 == 0):
            del formula[indexes]
            if (((index_to_append/2) -1) == len(formula) - 2):
                formula.append(numbers[float((index_to_append/2) -1)])
                continue
            else:
                formula.insert(indexes, numbers[int((index_to_append/2) -1)])        
                continue      
        del formula[indexes]                
        
    negative_numbers.reverse()
    index_to_append = 0
    for indexes in reversed(negative_indexes_to_delete):
        index_to_append += 1
        if (index_to_append % 3 == 0):
            del formula[indexes]
            formula.insert(indexes, negative_numbers[int((index_to_append/3) -1)])        
            continue      
        del formula[indexes]            #end of abs

    indexes_to_delete = []
    numbers= []
    index_to_append = 0
    for i,element in enumerate(formula):        #start of factorial
        if element == "!":
            indexes_to_delete.extend([i - 1, i])
            number_for_factorial = formula [i - 1]
            number_after_factorial = math_module.factorial(number_for_factorial)
            if number_after_factorial == "Error!":
                result = "ERROR: Invalid number (factorial)"
                return result
            numbers.append(number_after_factorial)
    numbers.reverse()       #the first number i will be adding is the last in the original array
    
    for indexes in reversed(indexes_to_delete):
        index_to_append += 1
        if (index_to_append % 2 == 0):
            del formula[indexes]
            formula.insert(indexes, numbers[int((index_to_append/2) -1)])        
            continue      
        del formula[indexes]            #end of factorial
    
    indexes_to_delete = []          #start of exponent
    numbers= []
    index_to_append = 0
    for i, element in enumerate(formula):
        if element == "^":
            indexes_to_delete.extend([i - 1, i, i + 1])
            base = formula[i - 1]
            exponent = formula[i + 1]
            number_after_exp = math_module.expon(base, exponent)
            if number_after_exp == "Error!":
                result = "ERROR: Invalid number (exponent)"
                return 1
            numbers.append(number_after_exp)
    numbers.reverse()

    for indexes in reversed(indexes_to_delete):
        index_to_append += 1
        if (index_to_append % 3 == 0):
            del formula[indexes]
            formula.insert(indexes, numbers[int((index_to_append/3) -1)])        
            continue      
        del formula[indexes]        #end of exponent

    for i,element in enumerate(formula):        #placement after factorial etc. because it would result in invalid   
        if element == "-" and (isinstance(formula[i + 1], int) or isinstance(formula[i + 1], float)):
            if i + 2 < len(formula) - 1:
                if formula[i + 2] == "\u221A":
                    continue
            if i == 0:
                negative_number = -formula[i + 1]
                formula[i: i + 2] = [negative_number]
            if not i == 0:
                if (formula[i - 1] == "+") or (formula[i - 1] == "*") or (formula[i - 1] == "/") or (formula[i - 1] == "-"):
                    negative_number = -formula[i + 1]
                    formula[i: i + 2] = [negative_number]
                    continue
                formula[i+1]=-(formula[i+1])
                formula[i] = "+"

    indexes_to_delete = []          #start of root
    numbers= []
    index_to_append = 0
    for i,element in enumerate(formula):        
        if element == "\u221A":
            if formula[i + 1] == "+":
                del formula[i + 1]
            indexes_to_delete.extend([i - 1, i, i + 1])
            radicant = formula [i + 1]
            root_index = formula [i - 1]
            number_after_root = math_module.root(radicant, root_index)
            if number_after_root == "Error!":
                result = "ERROR: Invalid number (roof)"
                return result
            numbers.append(number_after_root)
    numbers.reverse()       #the first number i will be adding is the last in the original array
    
    for indexes in reversed(indexes_to_delete):
        index_to_append += 1
        if (index_to_append % 3 == 0):
            del formula[indexes]
            formula.insert(indexes, numbers[int((index_to_append/3) -1)])        
            continue      
        del formula[indexes]            #end of root


    while "*" in formula:       #start of multiplication
        for i, element in enumerate(formula):
            if element == "*":
                if formula[i + 1] == "+":
                    del formula[i + 1]
                first_number = formula[i - 1]
                second_number = formula[i + 1]
                number_after_multiplication = math_module.multiplication(first_number, second_number)
                formula[i - 1:i + 2] = [number_after_multiplication]
                break           #end of multiplication
            
    while "/" in formula:       #start of division
        for i, element in enumerate(formula):
            if element == "/":
                if formula[i + 1] == "+":
                    del formula[i + 1]
                first_number = formula[i - 1]
                second_number = formula[i + 1]
                number_after_division = math_module.division(first_number, second_number)
                if number_after_division == "Error!":
                    result = "ERROR: Invalid number (division)"
                    return result
                formula[i - 1:i + 2] = [number_after_division]
                break       #end of division

    while "+" in formula:       #start ot addition
        for i, element in enumerate(formula):
            if element == "+":
                first_number = formula[i - 1]
                second_number = formula[i + 1]
                number_after_addition = math_module.addition(first_number, second_number)
                formula[i - 1:i + 2] = [number_after_addition]
                break       #end of addition

    while "-" in formula:       #start of subtraction
        for i, element in enumerate(formula):
            if element == "-":
                first_number = formula[i - 1]
                second_number = formula[i + 1]
                number_after_subtraction = math_module.subtraction(first_number, second_number)
                formula[i - 1:i + 2] = [number_after_subtraction]
                break       #end of subtraction
    return formula




## @brief This function decides, if it should count the formula or return error message
#  @param formula the input
#  @return it returns either evaluated formula or an error message
#
def count_everything(formula):
    valid_formula = validity_check(formula)
    if valid_formula!=0:
        result = "ERROR: invalid input"
    if valid_formula == 0:
        result = evaluate_formula(formula)
    return result

##  @brief This function checks if the input is valid
#   @param formula the input string
#   @return 0 if the input is valid
#           number other than 0 if the input is invalid
#
def validity_check(formula):
    for i, element in enumerate(formula):
        if not (element.isdigit() or element in valid_opperands):
            return 1
        match element:
            case ".":
                if i == 0 or i == len(formula) -1:         #i is the current index in formula, if the last or first character is ., it is invalid 
                    return 2
                if not (formula[i -1].isdigit() and formula[i + 1].isdigit()):      #digit needs to be before and after .
                    return 3
            case "!":
                if i == 0:
                    return 4
                if not(formula[i -1].isdigit()):
                    return 5
            case "abs":
                if i == len(formula) -1:
                    return 6
                if formula[i + 1] == "-":
                    if i + 2 >= len(formula) or not formula[i + 2].isdigit():
                        return 7
                elif not formula[i + 1].isdigit():
                    return 8
            case "\u221A":
                if i == 0 or i == len(formula) -1:
                    return 9
                if not(formula[i -1].isdigit() and (formula[i + 1].isdigit() or formula[i + 1] == "-" or formula[i + 1] == "abs")):
                    return 10
                if i + 2 < len(formula):
                    if (formula[i + 1] == "-"):
                        if not (formula[i + 2].isdigit()):
                            return 11
            case "^":
                if i == 0 or i == len(formula) -1:
                    return 12
                if not(formula[i -1].isdigit() and formula[i + 1].isdigit()):
                    return 13
            case "*":
                if i == 0 or i == len(formula) - 1:
                    return 14
                if not((formula[i -1].isdigit() and formula[i + 1].isdigit()) or 
                        (formula[i -1].isdigit() and formula[i + 1] == "abs") or 
                        (formula[i -1].isdigit() and formula[i + 1] == "-") or
                        ((formula[i -1].isdigit() and formula[i + 1] == "+"))):
                    return 15
            case "/":
                if i == 0 or i == len(formula) - 1:
                    return 16
                if not((formula[i -1].isdigit() and formula[i + 1].isdigit()) or 
                        (formula[i -1].isdigit() and formula[i + 1] == "abs") or 
                        (formula[i -1].isdigit() and formula[i + 1] == "-") or
                        ((formula[i -1].isdigit() and formula[i + 1] == "+"))):
                    return 17
            case"+":
                if i == len(formula) - 1:
                    return 18
            case "-":
                if i == len(formula) - 1:
                    return 19
    return 0

entry = Entry(root, width = 20, borderwidth= 0, font = ("Arial", 20))
entry.grid(row = 0, column = 0, columnspan = 4, rowspan= 2, padx= 10, pady= 10)
entry.bind("<Return>", lambda event: getchar_from_button("="))
button_size_color = {"padx": 0, "pady": 0, "width": 10, "fg": "white"}

button_0 = Button(root, text = "0",**button_size_color, bg = "gray20", command= lambda: getchar_from_button(0))
button_1 = Button(root, text = "1",**button_size_color, bg = "gray20", command= lambda: getchar_from_button(1))
button_2 = Button(root, text = "2",**button_size_color, bg = "gray20", command= lambda: getchar_from_button(2))
button_3 = Button(root, text = "3",**button_size_color, bg = "gray20", command= lambda: getchar_from_button(3))
button_4 = Button(root, text = "4",**button_size_color, bg = "gray20", command= lambda: getchar_from_button(4))
button_5 = Button(root, text = "5",**button_size_color, bg = "gray20", command= lambda: getchar_from_button(5))
button_6 = Button(root, text = "6",**button_size_color, bg = "gray20", command= lambda: getchar_from_button(6))
button_7 = Button(root, text = "7",**button_size_color, bg = "gray20", command= lambda: getchar_from_button(7))
button_8 = Button(root, text = "8",**button_size_color, bg = "gray20", command= lambda: getchar_from_button(8))
button_9 = Button(root, text = "9",**button_size_color, bg = "gray20", command= lambda: getchar_from_button(9))

button_mode = Button(root, text = "mode",**button_size_color, bg = "gray20")
button_help = Button(root, text = "?",**button_size_color, bg = "gray20", command = show_help)
button_equal = Button(root, text = "=",**button_size_color, bg = "gray33", command= lambda: getchar_from_button("="))
button_ac = Button(root, text = "AC",**button_size_color, bg = "gray33", command= lambda: getchar_from_button("AC"))
button_lc = Button(root, text = "LC",**button_size_color, bg = "gray33", command= lambda: getchar_from_button("LC"))

button_float = Button(root, text = ".",**button_size_color, bg = "gray20", command= lambda: getchar_from_button("."))
button_plus = Button(root, text = "+",**button_size_color, bg = "dark orange", command= lambda: getchar_from_button("+"))
button_minus = Button(root, text = "-",**button_size_color, bg = "dark orange", command= lambda: getchar_from_button("-"))
button_sqrt = Button(root, text = "\u221A",**button_size_color, bg = "dark orange", command= lambda: getchar_from_button("\u221A"))
button_abs = Button(root, text = "abs",**button_size_color, bg = "dark orange", command= lambda: getchar_from_button("abs"))
button_multiply = Button(root, text = "*",**button_size_color, bg = "dark orange", command= lambda: getchar_from_button("*"))
button_fact = Button(root, text = "!",**button_size_color, bg = "dark orange", command= lambda: getchar_from_button("!"))
button_exp = Button(root, text = "^",**button_size_color, bg = "dark orange", command= lambda: getchar_from_button("^"))
button_div = Button(root, text = "/",**button_size_color, bg = "dark orange", command= lambda: getchar_from_button("/"))

button_0.grid(row = 7, column = 1)
button_1.grid(row = 6, column = 0)
button_2.grid(row = 6, column = 1)
button_3.grid(row = 6, column = 2)

button_4.grid(row = 5, column = 0)
button_5.grid(row = 5, column = 1)
button_6.grid(row = 5, column = 2)

button_7.grid(row = 4, column = 0)
button_8.grid(row = 4, column = 1)
button_9.grid(row = 4, column = 2)

button_mode.grid(row = 7, column = 0)
button_float.grid(row = 7, column = 2)
button_help.grid(row = 7, column = 3)

button_equal.grid(row = 6, column = 3)

button_plus.grid(row = 5, column = 3)

button_minus.grid(row = 4, column = 3)
button_lc.grid(row = 3, column = 0)
button_sqrt.grid(row = 3, column = 1)
button_abs.grid(row = 3, column = 2)
button_multiply.grid(row = 3, column = 3)

button_ac.grid(row = 2, column = 0)
button_fact.grid(row = 2, column = 1)
button_exp.grid(row = 2, column = 2)
button_div.grid(row = 2, column = 3)

root.mainloop()