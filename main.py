import customtkinter as ctk
import tkinter as tk
from eq_parser import EQParser 
from check_exact import TestExact
from check_homogenous import TestHomogenous


class InputFrame(ctk.CTkFrame):
    def __init__(self, master, input_var):
        super().__init__(master, fg_color="transparent")
        self.input_var = input_var

        input_label = ctk.CTkLabel(
            master=self,
            text="Input equation here: ",
            font=('Verdana', 18)
        )
        input_label.pack(
            pady = (20, 15)
        )

        self.input_entry = ctk.CTkEntry(
            master=self,
            textvariable=self.input_var,
            width=500,
            height=50,
            corner_radius=16,
            fg_color="transparent",
            font=('Verdana', 24),
        )
        self.input_entry.pack(side=tk.LEFT, padx=(0, 10))

        input_clear = ctk.CTkButton(
            master=self,
            command=lambda: self.input_var.set(""),
            text="Clear",
            width=100,
            height=50, 
            corner_radius=16,
            fg_color="blue",
            font=('Verdana', 16),
        )
        input_clear.pack(side=tk.RIGHT)


class ButtonFrame(ctk.CTkFrame):
    def __init__(self, master, button_list, input_var, input_entry):
        super().__init__(master, fg_color='transparent')
        self.input_var = input_var
        self.button_list = button_list
        self.input_entry = input_entry
        self.tabview = ctk.CTkTabview(
            self, 
            width=650, 
            height=200, 
            corner_radius=24,
            anchor='nw',
            fg_color='transparent',
            border_width=3
        )

        basic_buttons_tab = self.tabview.add('Basic')
        func_buttons_tab = self.tabview.add('Advanced')

        self.operators_frame1 = ctk.CTkFrame(basic_buttons_tab, fg_color='transparent')
        self.operators_frame2 = ctk.CTkFrame(func_buttons_tab, fg_color='transparent')
        self.numbers_frame = ctk.CTkFrame(basic_buttons_tab, fg_color='transparent')
        self.functions_frame = ctk.CTkFrame(func_buttons_tab, fg_color='transparent')


        def create_buttons(btn_name, btn_root, btn_type):
            def button_click():
                self.input_var.set(self.input_var.get() + btn_name)
                if btn_type == "functions":
                    self.input_entry.icursor(len(self.input_var.get()) - 1)
                else:
                    self.input_entry.icursor(len(self.input_var.get()))


            return ctk.CTkButton(
                master = btn_root,
                command=button_click,
                text=btn_name,
                font=('Verdana', 14),
                text_color='white',
                fg_color='#333',
                width=50,
                height=40,
            )
        

        for index, btn in enumerate(self.button_list["numbers"]):
            row, col = divmod(index, 5) 
            create_buttons(btn, self.numbers_frame, "numbers").grid(row=row, column=col, padx=5, pady=5)

        for index, btn in enumerate(self.button_list["operators"]):
            row, col = divmod(index, 5)  
            create_buttons(btn, self.operators_frame1, "operators").grid(row=row, column=col, padx=5, pady=5)
            create_buttons(btn, self.operators_frame2, "operators").grid(row=row, column=col, padx=5, pady=5)

        for index, btn in enumerate(self.button_list["functions"]):
            row, col = divmod(index, 4)  
            create_buttons(btn, self.functions_frame, "functions").grid(row=row, column=col, padx=5, pady=5)

        self.numbers_frame.pack(side=tk.LEFT, padx=5, pady=5)
        self.operators_frame1.pack(side=tk.RIGHT, padx=5, pady=5)
        self.operators_frame2.pack(side=tk.RIGHT, padx=5, pady=5)
        self.functions_frame.pack(side=tk.LEFT, padx=5, pady=5)

        self.tabview.pack()


    
class OptionsFrame(ctk.CTkFrame):
    def __init__(self, master, change_check_type_callback, process_input_callback, option_var):
        super().__init__(master, fg_color='transparent')
        self.option_label = ctk.CTkLabel(
            master=self,
            text="Select Type of Operation to Perform",
            font=("Verdana", 10)
        )
        self.option_label.pack(pady=(10, 0))

        self.check_options = ctk.CTkOptionMenu(
            master=self,
            values=["Homogenous Check", "Exact Check"],
            command=change_check_type_callback,
            variable=option_var,
            width=200,
            font=('Verdana', 14),
            dynamic_resizing=False,
        )
        self.check_options.pack(pady=(0, 10))

        self.solve_button = ctk.CTkButton(
            master=self,
            text="Solve",
            command=process_input_callback,
            width=200,
            height=50,
            corner_radius=16,
            fg_color="green",
            font=('Verdana', 18),
        )
        self.solve_button.pack()


class DEChecker:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("900x600")
        self.window.title('Differential Equation Checker')

        self.input_var = tk.StringVar()
        self.option_var = tk.StringVar(value="Select a Type")

        # Input Frame
        self.input_frame = InputFrame(self.window, self.input_var)
        self.input_frame.pack(pady=(50, 0))

        # Button Grid
        self.button_frame = ButtonFrame(
            self.window,
            button_list={
                "numbers": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
                "operators": ['+', '-', '*', '/', '^', '(', ')', 'x', 'y', '='],
                "functions": ['sin()', 'cos()', 'tan()', 'dx', 'cot()', 'sec()', 'csc()', 'dy'],
            },
            input_var=self.input_var,
            input_entry=self.input_frame.input_entry
        )
        self.button_frame.pack(pady=10)

        # Options Frame
        self.options_frame = OptionsFrame(self.window, self.change_check_type, self.process_input, self.option_var)
        self.options_frame.pack()

    def change_check_type(self, option):
        self.check_type = option


    def process_input(self):
        M, N = EQParser(self.input_var.get())
        if self.option_var.get() == "Select a Type":
            self.options_frame.option_label.configure(text="Please Select Type of Operation", text_color="red")
        else:
            self.options_frame.option_label.configure(text="Select Type of Operation to Perform", text_color="white")
            checkType = self.option_var.get()
            print(f"M: {M}, N: {N}, Type: {checkType}")
            if checkType == "Exact Check":
                TestExact(M, N)
            elif checkType == "Homogenous Check":
                M_degree = TestHomogenous(M, 'M')
                N_degree = TestHomogenous(N, 'N')

                if M_degree == N_degree:
                    print(f"The differential equation is homogeneous of degree {M_degree}.")
                else:
                    print("The differential equation is not homogeneous.")

    

if __name__ == '__main__':
    DEChecker().window.mainloop()













# self.button_list = {
#     "numbers": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
#     "operators": ['+', '-', '*', '/', '(', ')', '^', '='],
#     "functions": ['sin()', 'cos()', 'tan()', 'x', 'dx', 'cot()', 'sec()', 'csc()', 'y', 'dy']
# }