import customtkinter as ct
import easygui as eg
import winsound as ws
from dictionary import d_h

def decimal_hexadecimal():
    new_root = ct.CTk()
    new_root.resizable(height=False, width=False)
    new_root.title("Decimal To Hexadecimal Converter")

    header = ct.CTkLabel(new_root, width=0, height=28, text= "Decimal to Hexadecimal", font=("Roboto", 20))
    header.pack(pady = 20, padx = 20)

    entry_box = ct.CTkEntry(new_root,width=210, height=28, placeholder_text="Please write the decimal number")
    entry_box.pack(pady = 20, padx = 20)

    def converter():

        value = entry_box.get()
        lenght = len(value) - 1
        right_input = True

        while (lenght >= 0):
            if(value[lenght] < '0' or value[lenght] > '9'):
                right_input = False
                ws.PlaySound('ping.wav', ws.SND_FILENAME)
                eg.msgbox(msg = "Only numbers", title="WRONG INPUT", ok_button="Try Again")
                break
            lenght = lenght - 1
        
        if(right_input):

            lenght = len(value) - 1

            hexadecimal_number = ""
            number = int(value)

            while (number > 0):
                        
                    remain = number % 16
                    number = number - remain
                    number = number // 16

                    hexadecimal_number = d_h[remain] + hexadecimal_number
            
            text.configure(text = f"Hexadecimal number is {hexadecimal_number}")


    text = ct.CTkLabel(new_root, width=0, height=0, text = "")
    text.pack(pady = 20, padx = 20)

    button = ct.CTkButton(new_root, width=140, height=28, text= "Convert", command= converter)
    button.pack(pady = 20, padx = 20)

    new_root.mainloop()