import customtkinter as ct
from binary_to_decimal import binary_decimal
from decimal_to_binary import decimal_binary
from hexadecimal_to_binary import hexadecimal_binary
from hexadecimal_to_decimal import hexadecimal_decimal
from decimal_to_hexadecimal import decimal_hexadecimal
from binary_to_hexadecimal import binary_hexadecimal
import easygui as eg
import winsound as ws

menu_root = ct.CTk()
menu_root.title("Converter Pro Max Ultimate Founders Edition")
menu_root.resizable(width=False, height=False)

def b_t_d():
    menu_root.destroy()
    binary_decimal()

def d_t_b():
    menu_root.destroy()
    decimal_binary()


def h_t_b():
    menu_root.destroy()
    hexadecimal_binary()


def h_t_d():
    menu_root.destroy()
    hexadecimal_decimal()


def d_t_h():
    menu_root.destroy()
    decimal_hexadecimal()


def b_t_h():
    menu_root.destroy()
    binary_hexadecimal()

to = ct.CTkLabel(menu_root, width=0, height=28, text = "➡️", font = ("Roboto", 40))
to.grid(row = 0, column = 1, pady = 20, padx = (70, 20), columnspan = 1)

first_variable = ct.CTkComboBox(menu_root, width=140, height=28, values=["Binary", "Decimal", "Hexadecimal"])
first_variable.grid(row = 0, column = 0, pady = 20, padx = (40,0), columnspan = 1)

second_variable = ct.CTkComboBox(menu_root, width=140, height=28, values=["Binary", "Decimal", "Hexadecimal"])
second_variable.grid(row = 0, column = 2, pady = 20 ,padx = (0,40), columnspan = 1 )

def selections(first = first_variable, second = second_variable):
    sel1 = first.get()
    sel2 = second.get()

    if(sel1 == sel2):
        ws.PlaySound('ping.wav', ws.SND_FILENAME)
        eg.msgbox(msg = "Selections can't be same", title="WRONG INPUT", ok_button="Try Again")
    elif((sel1 == "Binary") and (sel2 == "Decimal")):
        b_t_d()
    elif(sel1  == "Hexadecimal" and sel2 == "Decimal"):
        h_t_d()
    elif(sel1 == "Decimal" and sel2 == "Binary"):
        d_t_b()
    elif(sel1 == "Hexadecimal" and sel2 == "Binary"):
        h_t_b()
    elif(sel1 == "Decimal" and sel2 == "Hexadecimal"):
        d_t_h()
    elif(sel1 == "Binary" and sel2 == "Hexadecimal"):
        b_t_h()
    else:
        ws.PlaySound('ping.wav', ws.SND_FILENAME)
        eg.msgbox(msg = "Please don't play with inputs", title="What do you think you are doing?", ok_button="My apologies")
    

button_continue = ct.CTkButton(menu_root, width=140, height=28, text="Convert", command = selections)
button_continue.grid(row = 100, column = 1, pady = 20, padx = 0, columnspan = 1)

menu_root.mainloop()