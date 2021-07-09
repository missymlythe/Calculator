import tkinter as tk
import math

LARGE_FONT = ("Verdana", 35, "bold")
SMALL_FONT = ("Verdana", 16)
DIGIT_FONT = ("Verdana", 24, "bold")
DEFULT_FONT = ("Verdana", 20)

WHITE = "#FFFFFF"
DARK_GRAY = "#131313"
LIGHT_BLUE = "#4caba4"
BLUE_GREEN = "#00877E"
ORANGE = "#cc8400"
DARK_GRAY1 = "#141414"


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window
        self.window.title(" CodeGeeks Calculator")

        self.add_dec = True
        self.add_op = True
        self.total = ""
        self.expression = ""
        self.display_frame = self.display_frame()

        self.exp_display = tk.Label(self.display_frame, text = self.expression, anchor = tk.E, bg = DARK_GRAY1, fg = WHITE, padx = 24, font = SMALL_FONT)
        self.exp_display.pack(expand = True, fill = "both")
        self.total_display = tk.Label(self.display_frame, text = self.total, anchor = tk.E, bg = DARK_GRAY1, fg = WHITE, padx = 24, font = LARGE_FONT)
        self.total_display.pack(expand = True, fill = "both")

        self.digits = {
            7: (2,1), 8: (2,2), 9: (2,3),
            4: (3,1), 5: (3,2), 6: (3,3),
            1: (4,1), 2: (4,2), 3: (4,3),
            0: (5,1), ".": (5,2)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+" }
        self.button_frame = self.button_frame()
        
        self.button_frame.rowconfigure(0, weight = 1)

        for x in range(1,6):
            self.button_frame.rowconfigure(x, weight = 1)
        for x in range(1,5):
            self.button_frame.columnconfigure(x, weight = 1)

        self.digit_buttons()
        self.operator_buttons()
        self.special_buttons()
        self.keyboard()


    def display_frame(self):
        frame = tk.Frame(self.window, height = 221, bg = DARK_GRAY)
        frame.pack(expand = True, fill = "both")
        return frame

    def digit_buttons(self):
        for digit, grid in self.digits.items():
            button = tk.Button(self.button_frame, text = str(digit), bg = DARK_GRAY, fg = WHITE, font = DIGIT_FONT, borderwidth = 0, command = lambda x = digit: self.add_expression(x))
            button.grid(row = grid[0], column = grid[1], sticky = tk.NSEW)

    def operator_buttons(self):
        i = 1
        for operator, symbol in self.operations.items():
            button = tk.Button(self.button_frame, text = symbol, bg = DARK_GRAY, fg = BLUE_GREEN, font = DEFULT_FONT, borderwidth = 0, command = lambda x = operator: self.add_operator(x))
            button.grid(row = i, column = 4, sticky = tk.NSEW)
            i +=1

    def keyboard(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        self.window.bind("<BackSpace>", lambda event: self.delete())
        self.window.bind("<Delete>", lambda event: self.clear())
        self.window.bind("<s>", lambda event: self.square())
        self.window.bind("<r>", lambda event: self.sqrt())
        self.window.bind("<%>", lambda event: self.percent())
        self.window.bind("<q>", lambda event: self.sin())
        self.window.bind("<w>", lambda event: self.cos())
        self.window.bind("<e>", lambda event: self.tan())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit = key: self.add_expression(digit))
        
        for key in self.operations:
            self.window.bind(key, lambda event, operator = key: self.add_operator(operator))            
            
    def update_label(self):
        expr = self.total
        
        for operator, symbol in self.operations.items():
            expr = expr.replace(operator, f" {symbol} ")
        
        self.exp_display.config(text = expr)

    def update_total(self):
        self.total_display.config(text = self.expression[:10])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
