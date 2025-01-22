import customtkinter as ct
from dictionary import h_d
import easygui as eg
import winsound as ws

def hexadecimal_decimal():

    new_root = ct.CTk()
    new_root.resizable(height=False, width=False)
    new_root.title("Hexadecimal To Decimal Converter")

    header = ct.CTkLabel(new_root, width=0, height=28, text= "Hexadecimal to Decimal")
    header.pack(pady = 20, padx = 20)

    entry_box = ct.CTkEntry(new_root,width=210, height=28, placeholder_text="Please write the hexadecimal number")
    entry_box.pack(pady = 20, padx = 20)

    def converter():
        right_input = True
        value = entry_box.get()
        s = len(value) - 1

        while(s >=0):

            if(value[s] < '0' or (value[s] > '9' and value[s] < 'A') or (value[s] > 'F' and value[s] < 'a') or value[s] > 'z'):
                right_input = False
                ws.PlaySound('ping.wav', ws.SND_FILENAME)
                eg.msgbox(msg = "I saw little piggies in your hexadecimal", title="WRONG INPUT", ok_button="Try Again")
                break

            s = s - 1
        
        s = len(value) - 1

        if(right_input):

            decimal_number = 0
            n = s
            while(s >= 0):
                decimal_number = (h_d[value[s]] * pow(16, n - s)) + decimal_number
                s = s - 1
            
            text.configure(text = f"Decimal number is {decimal_number}")
    

    text = ct.CTkLabel(new_root, width=0, height=0, text="")
    text.pack(pady = 20, padx = 20)

    button = ct.CTkButton(new_root, width=140, height=28,text="Convert", command=converter)
    button.pack(pady = 20, padx = 20)

    new_root.mainloop()