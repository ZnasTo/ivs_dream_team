##
#@author xkovacj00, Jakub Kováčik
#@file hui_calculator.px
#@brief This file contains Graphical User Interface for the calculator 
#@TODO 
#

from tkinter import *
import re
    

root = Tk()

root.title("Calculator")
root.configure(bg = 'Black')

valid_opperands = ["+", "-", "*", "/", "!", "^", "abs", "\u221A", "."]


##  This function splits user input into array
#
#   @param input everything that user typed into calculator
#   @return splitted array of opperands and numbers
#
def split_formula(input):
    pattern = r"(\d+|\^|abs|\.|\u221A|[+\-*/!])"        #splitting the array by these opperands
    numbers__and_opperands = re.findall(pattern, input)
    return numbers__and_opperands

##  This function collets inputs as units
#   @param character input of user
#
def getchar_from_button(character):
    match character:
        case "=":
            result = count_everything(split_formula(entry.get()))
            entry.delete(0, END)
            entry.insert(0, result)
        case "AC":
            entry.delete(0, END)
        case "LC":
            entry.delete(len(entry.get()) - 1, END)
        case _:
            entry.insert(END, character)
    

def count_everything(numbers):
    valid_formula = validity_check(numbers)
    result = 1
    return result

##  This function checks if the input is valid
#   @param formula the input string
#   @return 0 if the input is valid
#           1 if the input is invalid
#
def validity_check(formula):
    for element in formula:
        if not (element.isdigit() or element in valid_opperands):
            return 1        #return is 1 if it is not valid
    return 0

entry = Entry(root, width = 25, borderwidth= 0, font = ("Arial", 20))
entry.grid(row = 0, column = 0, columnspan = 4, rowspan= 2, padx= 10, pady= 10)
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
button_abs = Button(root, text = "abs",**button_size, command= lambda: getchar_from_button("abs"))
button_multiply = Button(root, text = "*",**button_size, command= lambda: getchar_from_button("*"))
button_fact = Button(root, text = "!",**button_size, command= lambda: getchar_from_button("!"))
button_exp = Button(root, text = "^",**button_size, command= lambda: getchar_from_button("^"))
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