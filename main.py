import customtkinter as ctk

window = ctk.CTk()
window.geometry("900x600")
window.title('Differential Equation Checker')

input_frame = ctk.CTkFrame(window)

input_label = ctk.CTkLabel(
    master=input_frame,
    text="Input equation here: ",
    font=('Verdana', 24)
)

input_label.pack()
input_frame.pack(
    pady = (50, 0)
)

button_screen = ctk.CTkFrame(window)
button_list = {
    "numbers": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
    "operators": ['dx', 'dy', '+', '-', '*', '/', '^', '(', ')', '=']
}

number_btns_frame = ctk.CTkFrame(button_screen)
operators_btns_frame = ctk.CTkFrame(button_screen)

def button_click():
    pass

def create_buttons(btn_name, btn_master):
    return ctk.CTkButton(
        master=btn_master,
        command= lambda: button_click(),
        text=btn_name,
        font=('Verdana', 12),
        text_color='white',
        fg_color='#333333',
        width=4,
        height=2
    )



    


window.mainloop()