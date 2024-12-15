import customtkinter as ctk
import tkinter as tk
from eq_parser import EQParser 
from test_exact_window import TestExactWindow
from test_homog_window import TestHomogWindow
from test_homog import TestHomogenous


class InputFrame(ctk.CTkFrame):
    def __init__(self, master, input_var):
        super().__init__(master, fg_color="transparent")
        self.input_var = input_var

        self.input_label = ctk.CTkLabel(
            master=self,
            text="Input equation here: ",
            font=('Verdana', 18)
        )
        self.input_label.pack(
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
            fg_color="#333333",
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
        self.window = ctk.CTk(fg_color='gray10')
        self.window.geometry("900x600")
        self.window.title('Differential Equation Checker')

        self.input_var = tk.StringVar()
        self.option_var = tk.StringVar(value="Select a Type")

        self.test_exact_window = None
        self.test_homog_window = None

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
        try:
            M, N = EQParser(self.input_var.get())
            if self.option_var.get() == "Select a Type":
                self.options_frame.option_label.configure(text="Please Select Type of Operation", text_color="red")
            else:
                checkType = self.option_var.get()
                self.options_frame.option_label.configure(text="Select Type of Operation to Perform", text_color="white")
                print(f"M: {M}, N: {N}, Type: {checkType}")
                if checkType == "Exact Check":
                    if self.test_exact_window is None or not self.test_exact_window.winfo_exists():
                        self.test_exact_window = TestExactWindow(M = M, N = N)
                elif checkType == "Homogenous Check":
                    if self.test_homog_window is None or not self.test_homog_window.winfo_exists():
                        self.test_homog_window = TestHomogWindow(M = M, N = N)

            self.input_frame.input_label.configure(
                text = "Input equation here: ",
            )
            self.input_frame.input_entry.configure(
                border_width = 1,
                border_color = "gray",
            )

        except TypeError:
            self.input_frame.input_label.configure(
                text = "Please enter a valid input",
            )
            self.input_frame.input_entry.configure(
                border_width = 3,
                border_color = "red",
            )
        

           
    
if __name__ == '__main__':
    DEChecker().window.mainloop()
