import customtkinter as ctk
import tkinter as tk
import sympy as sp

class DEChecker:

    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("900x600")
        self.window.title('Differential Equation Checker')

        self.inputVar = tk.StringVar()

        # -------- INPUT FRAME ------- #
        input_frame = ctk.CTkFrame(self.window, fg_color="transparent")

        input_label = ctk.CTkLabel(
            master=input_frame,
            text="Input equation here: ",
            font=('Verdana', 18)
        )

        self.input_entry = ctk.CTkEntry(
            master=input_frame,
            textvariable=self.inputVar,
            width=500,
            height=50,
            corner_radius=16,
            fg_color="transparent",
            font=('Verdana', 24),
        )

        input_clear = ctk.CTkButton(
            master=input_frame,
            command=lambda: self.inputVar.set(""),
            text="Clear",
            width=100,
            height=50, 
            corner_radius=16,
            fg_color="blue",
            font=('Verdana', 16),
        )

        input_frame.pack(
            pady = (50, 0)
        )
        input_label.pack(
            pady = (20, 15)
        )
        self.input_entry.pack(side=tk.LEFT, padx=(0, 10))
        input_clear.pack(side=tk.RIGHT)



        # -------- BUTTONS FRAME ------- #
        self.buttons_tabview = ctk.CTkTabview(
            master=self.window,
            width=550,
            height=240,
            corner_radius=24,
            anchor='nw'
        )

        basic_buttons_tab = self.buttons_tabview.add('Basic')
        func_buttons_tab = self.buttons_tabview.add('Advanced')

        self.button_list = {
            "numbers": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
            "operators": ['+', '-', '*', '/', '(', ')', '^', '='],
            "functions": ['sin()', 'cos()', 'tan()', 'x', 'dx', 'cot()', 'sec()', 'csc()', 'y', 'dy']
        }

        self.operators_frame1 = ctk.CTkFrame(basic_buttons_tab)
        self.operators_frame2 = ctk.CTkFrame(func_buttons_tab)
        self.numbers_frame = ctk.CTkFrame(basic_buttons_tab)
        self.functions_frame = ctk.CTkFrame(func_buttons_tab)

        def button_click(name, type):
            self.inputVar.set(self.inputVar.get() + name)
            if type == "functions":
                self.input_entry.icursor(len(self.inputVar.get()) - 1)
            else:
                self.input_entry.icursor(len(self.inputVar.get()))

        def create_buttons(btn_name, btn_root, btn_type):
            return ctk.CTkButton(
                master = btn_root,
                command= lambda: button_click(btn_name, btn_type),
                text=btn_name,
                font=('Verdana', 14),
                text_color='white',
                fg_color='#333333',
                width=50,
                height=40,
            )
        

        for index, btn in enumerate(self.button_list["numbers"]):
            row, col = divmod(index, 5) 
            create_buttons(btn, self.numbers_frame, "numbers").grid(row=row, column=col, padx=5, pady=5)

        for index, btn in enumerate(self.button_list["operators"]):
            row, col = divmod(index, 4)  
            create_buttons(btn, self.operators_frame1, "operators").grid(row=row, column=col, padx=5, pady=5)
            create_buttons(btn, self.operators_frame2, "operators").grid(row=row, column=col, padx=5, pady=5)

        for index, btn in enumerate(self.button_list["functions"]):
            row, col = divmod(index, 5)  
            create_buttons(btn, self.functions_frame, "functions").grid(row=row, column=col, padx=5, pady=5)

        self.numbers_frame.pack(side=tk.LEFT, padx=5, pady=5)
        self.operators_frame1.pack(side=tk.RIGHT, padx=5, pady=5)
        self.operators_frame2.pack(side=tk.RIGHT, padx=5, pady=5)
        self.functions_frame.pack(side=tk.LEFT, padx=5, pady=5)

        self.buttons_tabview.pack(pady=10)

        




if __name__ == '__main__':
    DEChecker().window.mainloop()


