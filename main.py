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
            hover_color="blue2",
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
            border_width=3,

            segmented_button_fg_color='#333333',
            segmented_button_selected_color='blue2'
        )

        basic_buttons_tab = self.tabview.add('Basic')
        func_buttons_tab = self.tabview.add('Advanced')

        self.operators_frame1 = ctk.CTkFrame(basic_buttons_tab, fg_color='transparent')
        self.operators_frame2 = ctk.CTkFrame(func_buttons_tab, fg_color='transparent')
        self.numbers_frame = ctk.CTkFrame(basic_buttons_tab, fg_color='transparent')
        self.functions_frame = ctk.CTkFrame(func_buttons_tab, fg_color='transparent')


        def create_buttons(btn_name, btn_root, btn_type):
            def button_click():
                cursor_position = self.input_entry.index("insert")
                self.input_var.set(
                    self.input_var.get()[:cursor_position] + btn_name + self.input_var.get()[cursor_position:]
                )
                if btn_type == "functions" and (btn_name != 'e' and btn_name != 'a'):
                    self.input_entry.icursor(len(self.input_var.get()) - 1)
                else:
                    self.input_entry.icursor(cursor_position + len(btn_name))


            return ctk.CTkButton(
                master = btn_root,
                command=button_click,
                text=btn_name,
                font=('Verdana', 14),
                text_color='white',
                fg_color='#333',
                hover_color='blue2',
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
    def __init__(self, master, change_check_type_callback, process_input_callback, option_var, utility_callback):
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
            dropdown_font=('Verdana', 12),
            dynamic_resizing=False,
            fg_color='#333333',
        )
        self.check_options.pack(pady=(0, 10))

        self.solve_button = ctk.CTkButton(
            master=self,
            text="Solve",
            command=process_input_callback,
            width=200,
            height=50,
            corner_radius=16,
            fg_color="blue2",
            hover_color="blue4",
            font=('Verdana', 18),
        )
        self.solve_button.pack(pady=(0, 10))

        self.tutorial_button = ctk.CTkButton(
            master=self,
            text="How to use the Program?",
            command=lambda: utility_callback("tutorial"),
            border_width=0,
            text_color="white",
            fg_color="transparent",
            hover_color="blue4",
            font=('Verdana', 12),
        )
        self.tutorial_button.pack(pady=(0, 10))

        self.about_button = ctk.CTkButton(
            master=self,
            text="About our Program",
            command=lambda: utility_callback("about"),
            border_width=0,
            text_color="white",
            fg_color="transparent",
            hover_color="blue4",
            font=('Verdana', 12),
        )
        self.about_button.pack()


class UtilityFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, titleText, content, currentFrames, initializeFrames):
        super().__init__(master, fg_color='gray15', width=900, height=675)
        self.titleText = titleText
        self.content = content
        self.currentFrames = currentFrames
        self.initializeFrames = initializeFrames

        for frame in currentFrames:
            frame.pack_forget()

        self.title_text_label = ctk.CTkLabel(
            master=self,
            text=self.titleText,
            font=("Verdana", 36, "bold"),
            text_color='white',
            justify="left",
        )
        self.title_text_label.pack(
            pady=(50, 20),
        )

        self.content_label = ctk.CTkLabel(
            master=self,
            text=content,
            font=("Verdana", 14),
            text_color='white',
            justify="left",
        )
        self.content_label.pack(
            pady=(30, 20),
        )

        self.back_button = ctk.CTkButton(
            master=self,
            text='Exit',
            command=self.exitFrame,
            font=("Verdana", 16, 'bold'),
            fg_color='blue2',
            hover_color='blue4',
        )
        self.back_button.pack(
            pady=(30, 50),
        )

    def exitFrame(self):
        self.title_text_label.pack_forget()
        self.content_label.pack_forget()
        self.back_button.pack_forget()
        self.initializeFrames()

    
class DEChecker:
    def __init__(self):
        self.window = ctk.CTk(fg_color='gray15')
        self.window.geometry("900x675")
        self.window.title('Differential Equation Checker')

        self.input_var = tk.StringVar()
        self.option_var = tk.StringVar(value="Select a Type")

        self.test_exact_window = None
        self.test_homog_window = None

        self.tutorial_frame = None
        self.about_frame = None

        # Input Frame
        self.input_frame = InputFrame(self.window, self.input_var)
        
        # Button Grid
        self.button_frame = ButtonFrame(
            self.window,
            button_list={
                "numbers": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
                "operators": ['+', '-', '*', '/', '^', '(', ')', 'x', 'y', '='],
                "functions": ['sin()', 'cos()', 'tan()', 'dx', 'cot()', 'sec()', 'csc()', 'dy', 'ln()', 'log()', 'e', 'a'],
            },
            input_var=self.input_var,
            input_entry=self.input_frame.input_entry
        )
        
        # Options Frame
        self.options_frame = OptionsFrame(self.window, self.change_check_type, self.process_input, self.option_var, self.utility_function)

        self.initialize_frames()
        

    def change_check_type(self, option):
        self.check_type = option

    def initialize_frames(self):
        self.input_frame.pack(pady=(50, 0))
        self.button_frame.pack(pady=10)
        self.options_frame.pack()

        if self.tutorial_frame != None:
            self.tutorial_frame.pack_forget()
        if self.about_frame != None:
            self.about_frame.pack_forget()

    def utility_function(self, window_name):
        if window_name == "tutorial":
            self.tutorial_frame = UtilityFrame(
                self.window,
                titleText="Tutorial Page",
                currentFrames=[self.input_frame, self.button_frame, self.options_frame],
                initializeFrames=self.initialize_frames,
                content="""
                Here is a complete guide of how to use the Differential Equation Checker.
                This program is designed to check whether first-order Differential Equations are 
                Homogenous or Exact, depending on the user's input.

                1. Using the Input Bar
                    a.) Our program only allows the following equation format as its input: 
                    M(x, y)dx + N(x, y)dy = 0

                    b.) The input bar is designed to look for this specific pattern, and an 
                    invalid input will be detected.

                    c.) Example of Valid Inputs:
                        • (2x + 2y)dx + (x - y)dy = 0
                        • x(x^2 + y^2)dx + 2(3x + y^3)dy = 0
                        • 2xydx + 3xydy = 0
                        • xdx + ydy = 0

                    d.) Example of Invalid Inputs:
                        • (2x + 2y)dx + (x - y)dy
                        • (2x + 2y) + 2(dx - dy) = 0
                        • 3(x^2 + 3)dx = 4xydy
                        • x(x^2 + y^2) + 2(3x + y^3) = 0
                        • 1 + 1, 2 / 3, anything that does not resemble a differential equation

                    e.) There are also inputs that are considered valid by the input bar, but 
                    are hard to process because of confusing formatting, example of these include:
                        • x^22x+5dx + y^33y+5dy = 0 (Always use parentheses for a more 
                        accurate result)
                        • xsec^2(2x)dx + ytan(2y)dy = 0 (As a best practice for equations with trig 
                        functions, use x*sin() instead of xsin())
                        • x^1/3 (For exponents, use parentheses if necessary)

                    f.) You can use the clear button to clear all the inputs in the input bar.

                2. Using the Input Keyboard
                    a.) If you are unsure about which keys and functions can be accepted 
                    by our program the input keyboard provides that list, as well as providing an 
                    alternative for inputting the equation with a keyboard

                    b.) The basic input keyboard offers arithmetic digits, as well as the 
                    basic operators
                    
                    c.) The functions input keyboard provide trigonometric, inverse trig, 
                    and log functions as of the moment.

                    d.) the 'a' key symbolizes the arc in inverse trigonometric
                    functions. Pair it with any of the trig functions if needed 
                    (e.g. asin())

                    e.) always include the * sign when multiplying a term with a function.

                    f.) Use the toggle on the left-most side of the input keyboard to 
                    switch between modes.

                3. Switch Modes
                    a.) Before proceeding on evaluating the equation, you must first choose 
                    which check to use, either Homogenous or Exact Check

                    b.) The Homogenous Check will check if the first order Differential Equation 
                    is a Homogenous Equation. A Homogenous Equation is when its functions are 
                    both homogenous. A homogeneous function is a mathematical function that has 
                    a multiplicative scaling behavior: 
                    if each variable in the function is multiplied by a constant, then the entire 
                    function is multiplied by some power of that constant. The power is called 
                    the degree of homogeneity.

                    c.) The Exact Check will check if the first order Differential Equation is 
                    exact. An equation is exact when the partial derivative of M(x, y) with 
                    respect to y is equal to the partial derivative of N(x, y) with respect to x.

                4. The Solve Button
                    a.) When everything is clear, click the Solve button and wait as the 
                    program evaluates the input you have given it.

                    b.) However, the Solve button will not run in the following cases:
                        • The input is incorrectly formatted, in which the input box will turn red.
                        • When there is no mode selected in order to evaluate the function.
                """
            )
            self.tutorial_frame.pack()

        elif window_name == "about":
            self.about_frame = UtilityFrame(
                self.window,
                titleText="About Us",
                currentFrames=[self.input_frame, self.button_frame, self.options_frame],
                initializeFrames=self.initialize_frames,
                content="""
                This program is a course requirement for the following courses:
                Object-Oriented Programming
                Differential Equations

                Our group members who have willingly contributed to this program are as follows:
                AGUSTIN, IAN KENNETH - Lead Programmer
                ALBERTO, RISHIED - Documentation
                ANGCAO, JAMES LENARD - UML / Project Planner, Tester
                FULO, JOSE, - Programmer, Tester
                PAHATI, EISEN LIAM - Documentation, Brochure

                This program, although not perfect, is made with meticulous care and passion 
                about what we are doing.
                """
            )
            self.about_frame.pack()
            


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
                text = "Input equation must be in the format M(x,y)dx + N(x,y)dy = 0",
            )
            self.input_frame.input_entry.configure(
                border_width = 3,
                border_color = "red",
            )
        

           
    
if __name__ == '__main__':
    DEChecker().window.mainloop()
