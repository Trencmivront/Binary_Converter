import customtkinter as ct
from dictionary import h_b
import easygui as eg
import winsound as ws

def hexadecimal_binary():

    new_root = ct.CTk()
    new_root.resizable(width=False, height=False)

    header = ct.CTkLabel(new_root, width=0, height=28, text="Hexadecimal to Binary", font=("Roboto", 20))
    header.pack(pady = 20, padx = 20)

    entry_box = ct.CTkEntry(new_root,width=210,height=28,placeholder_text="Please write the hexadecimal number")
    entry_box.pack(pady = 20, padx =20)

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

            binary_number = ""

            while(s >= 0):
                binary_number = h_b[value[s]] + binary_number
                s = s - 1
            
            text.configure(text = f"Binary number is {binary_number}")    

    text = ct.CTkLabel(new_root, width=0,height=0,text = "")
    text.pack(pady=10, padx=10)

    button = ct.CTkButton(new_root, width=140, height=28, text = "Convert", command=converter)
    button.pack(pady = 20, padx = 20)

    new_root.mainloop()