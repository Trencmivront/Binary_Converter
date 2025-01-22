import customtkinter as ct
from dictionary import d_h
import easygui as eg
import winsound as ws

def binary_hexadecimal():

    new_root = ct.CTk()
    new_root.title("Binary To Hexadecimal Converter")
    new_root.resizable(width=False, height=False)

    header = ct.CTkLabel(new_root, width=0, height=28, text = "Binary to Hexadecimal", font = ("Roboto", 20))
    header.pack(pady = 20, padx = 20)

    entry_box = ct.CTkEntry(new_root, width=140, height=28, placeholder_text="Please write the binary number")
    entry_box.pack(pady = 20, padx = 20)

    def converter():
        value = entry_box.get()
        lenght = len(value) - 1
        n = lenght
        right_input = True

        while(n >= 0):

            if (value[n] < '0' or value[n] > '9'):
                right_input = False
                ws.PlaySound('ping.wav', ws.SND_FILENAME)
                eg.msgbox(msg = "Numbers must made of zeros and ones", title="WRONG INPUT", ok_button="Try Again")
                break

            if int(value[n]) == 0:
                pass
            elif int(value[n]) == 1:
                pass
            else:
                ws.PlaySound('ping.wav', ws.SND_FILENAME)
                eg.msgbox(msg = "Numbers must made of zeros and ones", title="WRONG INPUT", ok_button="Try Again")
                right_input = False
                break
            
            n = n - 1
        
        if(right_input):
            lenght = len(value) - 1
            n = lenght
            sum = 0
            while(n >= 0):
                sum = sum + int(value[n]) * pow(2, lenght - n)
                n = n - 1
            
            hexadecimal_number = ""
            number = sum

            while (number > 0):
                        
                    remain = number % 16
                    number = number - remain
                    number = number // 16

                    hexadecimal_number = d_h[remain] + hexadecimal_number
            
            text.configure(text = f"Hexadecimal number is {hexadecimal_number}")
    
    text = ct.CTkLabel(new_root, width=0, height=0, text="")
    text.pack(pady = 20, padx = 20)

    button = ct.CTkButton(new_root ,width=140, height=28, text="Convert", command = converter)
    button.pack(pady = 10, padx = 50)

    new_root.mainloop()