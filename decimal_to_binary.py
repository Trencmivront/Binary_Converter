import customtkinter as ct
import winsound as ws
import easygui as eg

def decimal_binary():

    new_root = ct.CTk()
    new_root.title("Decimal To Binary Converter")
    new_root.resizable(width=False, height=False)

    header = ct.CTkLabel(new_root, width=0, height=28, text="Decimal to Binary", font=("Roboto", 20))
    header.pack(pady = (20,10) ,padx = 40)

    entry_box = ct.CTkEntry(new_root, width=210, height=45, placeholder_text="Please write the decimal number")
    entry_box.pack(pady = 10, padx = 40)

    def convert():
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
                    
                    binary_number = ""
                    number = int(value)

                    if(number == 0):
                        binary_number = "0"

                    while (number > 0):
                        
                        remain = number % 2
                        number = number - remain
                        number = number // 2

                        binary_number = binary_number + str(remain)
                    
                    if(right_input):
                        message.configure(text = f"Binary number is {binary_number}")

    message = ct.CTkLabel(new_root, width=0, height=0, text= "")
    message.pack(pady = 10, padx = 50)

    button = ct.CTkButton(new_root, width=140, height=28, corner_radius=20, text="Convert", command=convert )
    button.pack(pady = 15, padx = 50)

    new_root.mainloop()