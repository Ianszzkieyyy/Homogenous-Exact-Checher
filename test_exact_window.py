import sympy as sp
import customtkinter as ctk
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from test_exact import TestExact


class TestExactWindow(ctk.CTkToplevel):
    def __init__(self, *args, fg_color = None, M, N, **kwargs,):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.geometry("800x650")
        self.after(100, self.lift)
        self.title("Exact Check Solution")
        self.M = M
        self.N = N

        sp.init_printing()
        self.derivative_y_respect, self.derivative_x_respect, self.isExact = TestExact(self.M, self.N)
        self.result_string = []

        self.label_helper("Your inputted equation was:", pady=(30, 5))
        self.equation_label_helper(f'M({self.M})dx + N({self.N})dy = 0')
        self.label_helper("The partial differentiation of M with respect to y is:")
        self.equation_label_helper(f'∂M/∂Y = {self.derivative_y_respect}')
        self.label_helper("The partial differentiation of N with respect to x is:")
        self.equation_label_helper(f'∂N/∂X = {self.derivative_x_respect}')
        self.label_helper("The partial differentiations of M and N must be equal")

        if self.isExact:
            self.equation_label_helper(f'∂M/∂Y = {self.derivative_y_respect} = {self.derivative_x_respect} = ∂N/∂X')
            self.result_string = ["is Equal", "is Exact"]
        else:
            self.equation_label_helper(f'∂M/∂Y = {self.derivative_y_respect} ≠ {self.derivative_x_respect} = ∂N/∂X')
            self.result_string = ["is not Equal", "is not Exact"]

        self.label_helper(f"∂M/∂Y {self.result_string[0]} to ∂N/∂X\nTherefore, the differential equation {self.result_string[1]}", pady=(10, 20))

        exit_button = ctk.CTkButton(
            master=self,
            text='Exit',
            command=lambda: self.destroy(),
            font=("Verdana", 16, 'bold'),
            fg_color='green',
        )
        exit_button.pack()

    def label_helper(self, text, pady = (0,5)):
        ctk.CTkLabel(
            master=self,
            text=text,
            font=("Verdana", 14),
            fg_color='transparent',
            text_color='white',
        ).pack(pady=pady)

    def equation_label_helper(self, equation):
        equation = equation.replace("**", "^").replace("*", "") 
        self.render_latex(equation)

    def render_latex(self, latex_string):

        fig, ax = plt.subplots(figsize=(8, 1))
        ax.text(0.5, 0.5, f'${latex_string}$', fontsize=24, ha='center', va='center', color='white')
        ax.axis('off')
        fig.patch.set_facecolor('#363636')

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack()

        plt.close(fig)

    

