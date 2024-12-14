import sympy as sp
import customtkinter as ctk
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from test_homog import TestHomogenous


class HomogFunction:
    def __init__(self, func, name, sub_lambda, simplified, factored, degree):
        self.func = func
        self.name = name
        self.sub_lambda = sub_lambda
        self.simplified = simplified
        self.factored = factored
        self.degree = degree


class TestHomogWindow(ctk.CTkToplevel):
    def __init__(self, *args, fg_color = None, M, N, **kwargs,):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.geometry("800x650")
        self.after(100, self.lift)
        self.title("Homogenous Check Solution")
        self.M = M
        self.N = N

        self.scroll_frame = ctk.CTkScrollableFrame(
            master=self,
            width=800,
            height=650,
            fg_color='transparent',
        )
        self.scroll_frame.pack()

        
        self.M_obj = HomogFunction(self.M, *TestHomogenous(self.M, 'M'))
        self.N_obj = HomogFunction(self.N, *TestHomogenous(self.N, 'N'))
        self.func_objects = [
            self.M_obj, self.N_obj
        ]

        sp.init_printing()
        self.result_string = []
        
        self.label_helper("Your inputted equation was:", pady=(30, 5))
        self.equation_label_helper(f'M({self.M})dx + N({self.N})dy = 0')

        for obj in self.func_objects:
            
            self.label_helper(f'Turning {obj.name}(x ,y) into {obj.name}(λx, λy)')
            self.equation_label_helper(f'{obj.sub_lambda}')

            self.label_helper(f"Simplifying {obj.name}(λx, λy)")
            self.equation_label_helper(f'{obj.simplified}')

            self.label_helper(f"Factoring out λ from {obj.name}(λx, λy)")
            self.equation_label_helper(f'{obj.factored}')

            if obj.degree != 0:
                self.label_helper(f"{obj.name}(x,y) is Homogenous at {obj.degree} Degree", pady=(0, 20))
            else:
                self.label_helper(f"{obj.name}(x,y) is not Homogenous", pady=(0, 20))
            


        if self.M_obj.degree == self.N_obj.degree:
            self.result_string = ["is Equal", "is Homogenous"]
        else:
            self.result_string = ["is not Equal", "is not Homogenous"]

        if self.func_objects[0].degree == 0 or self.func_objects[1].degree == 0:
            self.label_helper(f"Since one of the functions is not a Homogenous function\nThe differential equation is not Homogenous", pady=(10, 20))
        else:
            self.label_helper(f"Degree of M(x,y) ({self.func_objects[0].degree}) {self.result_string[0]} to Degree of N(x,y) ({self.func_objects[1].degree})\nTherefore, the differential equation {self.result_string[1]}", pady=(10, 20))


        exit_button = ctk.CTkButton(
            master=self.scroll_frame,
            text='Exit',
            command=lambda: self.destroy(),
            font=("Verdana", 16, 'bold'),
            fg_color='green',
        )
        exit_button.pack(pady=(0, 30))

    def label_helper(self, text, pady = (0,5)):
        ctk.CTkLabel(
            master=self.scroll_frame,
            text=text,
            font=("Verdana", 14),
            fg_color='transparent',
            text_color='white',
        ).pack(pady=pady)

    def equation_label_helper(self, equation):
        equation = equation.replace("**", "^").replace("*", "") 
        self.render_latex(equation)

    def render_latex(self, latex_string):

        fig, ax = plt.subplots(figsize=(6, 1))
        ax.text(0.5, 0.5, f'${latex_string}$', fontsize=24, ha='center', va='center', color='white')
        ax.axis('off')
        fig.patch.set_facecolor('#363636')

        canvas = FigureCanvasTkAgg(fig, master=self.scroll_frame)
        canvas.get_tk_widget().pack()

        canvas.draw()

        plt.close(fig)