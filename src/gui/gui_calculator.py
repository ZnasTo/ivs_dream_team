##
# @author xkovacj00, Jakub Kováčik
#
#   This file contains Graphical User Interface for the calculator
from tkinter import *

root = Tk()

root.title("Calculator")
root.configure(bg = 'Black')
#def show_screen(event=Nąone):
#    screen = entry.get()
#    print(screen)

position = 0       # 0 chosen for better work with 10,100, etc
numbers = []
tmp_opperands = []
opperands = []
valid_opperands = ["+", "-", "*", "/", "!", "exp: ", "abs: ", "\u221A", "."]
digits = []

def getchar_from_button(character):
    global position
    global digits

    current = entry.get()
    if current == '=':
        entry.delete(0, END)
        count_everything(numbers)
        digits.clear()

    entry.delete(0, END)
    entry.insert(0, str(current) + str(character))

    print(f"Button Pressed: {character}")   #DEBUG PRINT
    
    if isinstance(character, int):
        save_number(character, position)
        position += 1
        print(f"Numbers List: {numbers}")   #DEBUG PRINT
    
    if not (isinstance(character, int)):
        save_character(character, position)
        position = 0
        print(f"Operands List: {opperands}")   #DEBIG PRINT

def save_number(number, position):  #saves digits as one number
    global digits   
    global numbers 

    if position == 0:       
        tmp = save_num_to_list(digits)
        numbers.append(tmp) 
        print(f"Saved Number: {tmp}")   #DEBUG PRINT
        digits.clear()
        digits.append(number)
    else:
        digits.append(number)
        print(f"Digits Being Collected: {digits}")      #DEBUG PRINT
    
def save_character(character, position):
    global opperands
    global tmp_opperands
    global valid_opperands

    if position == 0:
        tmp = save_opp_to_list(tmp_opperands)
        if tmp in valid_opperands:
            opperands.append(tmp)
            print(f"Added Operator: {tmp}")     #DEBUG PRINT
        else:
            print(f"ERROR UNKNOWN OPERATOR: {tmp}")     ##if user writes unknown opperands, or writes them wrong
        opperands.append(tmp)
        tmp_opperands.clear()
        tmp_opperands.append(character)

    else:
        tmp_opperands.append(character)
        print(f"Building Operator: {tmp_opperands}")        #DEBUG PRINT

def save_num_to_list(digits):
    tmp = 0
    lenght = len(digits) - 1
    for digit in digits:
        tmp += digit*pow(10, lenght)
        lenght -= 1
    print(f"Final Number Built: {tmp}")     #DEBUG PRINT
    return tmp

def save_opp_to_list(opperands):
    tmp = ""
    for opperand in opperands:
        tmp += opperand
    print(f"Final Operator Built: {tmp}")       #DEBUG PRINT
    return tmp


def count_everything(numbers):
    return 


entry = Entry(root, width = 25, borderwidth= 0, font = ("Arial", 20))
entry.grid(row = 0, column = 0, columnspan = 4, rowspan= 2, padx= 10, pady= 10)
#entry.bind('<Return>', show_screen)
button_size = {"padx": 0, "pady": 0, "width": 5}

button_0 = Button(root, text = "0",**button_size, command= lambda: getchar_from_button(0))
button_1 = Button(root, text = "1",**button_size, command= lambda: getchar_from_button(1))
button_2 = Button(root, text = "2",**button_size, command= lambda: getchar_from_button(2))
button_3 = Button(root, text = "3",**button_size, command= lambda: getchar_from_button(3))
button_4 = Button(root, text = "4",**button_size, command= lambda: getchar_from_button(4))
button_5 = Button(root, text = "5",**button_size, command= lambda: getchar_from_button(5))
button_6 = Button(root, text = "6",**button_size, command= lambda: getchar_from_button(6))
button_7 = Button(root, text = "7",**button_size, command= lambda: getchar_from_button(7))
button_8 = Button(root, text = "8",**button_size, command= lambda: getchar_from_button(8))
button_9 = Button(root, text = "9",**button_size, command= lambda: getchar_from_button(9))


button_mode = Button(root, text = "mode",**button_size, bg="#4C4E4E")
button_help = Button(root, text = "?",**button_size, bg="#4C4E4E")
button_equal = Button(root, text = "=",**button_size, bg="#4C4E4E", command= lambda: getchar_from_button("="))
button_ac = Button(root, text = "AC",**button_size, bg="#4C4E4E", command= lambda: getchar_from_button("AC"))
button_lc = Button(root, text = "LC",**button_size, bg="#4C4E4E", command= lambda: getchar_from_button("LC"))


button_float = Button(root, text = ".",**button_size, command= lambda: getchar_from_button("."))
button_plus = Button(root, text = "+",**button_size, command= lambda: getchar_from_button("+"))
button_minus = Button(root, text = "-",**button_size, command= lambda: getchar_from_button("-"))
button_sqrt = Button(root, text = "\u221A",**button_size, command= lambda: getchar_from_button("\u221A"))
button_abs = Button(root, text = "abs",**button_size, command= lambda: getchar_from_button("abs: "))
button_multiply = Button(root, text = "*",**button_size, command= lambda: getchar_from_button("*"))
button_fact = Button(root, text = "!",**button_size, command= lambda: getchar_from_button("!"))
button_exp = Button(root, text = "exp",**button_size, command= lambda: getchar_from_button("exp: "))
button_div = Button(root, text = "/",**button_size, command= lambda: getchar_from_button("/"))


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