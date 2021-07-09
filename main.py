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

    def special_buttons(self):
        self.clear_button()
        self.equals_button()
        self.square_button()
        self.sqrt_button()
        self.delete_button()
        self.sin_button()
        self.cos_button()
        self.tan_button()
        self.percent_button()
        self.dec_button()

    def dec_button(self):
        button = tk.Button(self.button_frame, text = ".", bg = DARK_GRAY, fg = WHITE, font = DEFULT_FONT, borderwidth = 0, command = self.decimal)
        button.grid(row = 5, column = 2, sticky = tk.NSEW)
        
    def clear_button(self):
        button = tk.Button(self.button_frame, text = "C", bg = DARK_GRAY, fg = ORANGE, font = DEFULT_FONT, borderwidth = 0, command = self.clear)
        button.grid(row = 0, column = 1, sticky = tk.NSEW)

    def delete_button(self):
        button = tk.Button(self.button_frame, text = "Del", bg = DARK_GRAY, fg = ORANGE, font = DEFULT_FONT, borderwidth = 0, command = self.delete)
        button.grid(row = 0, column = 4, sticky = tk.NSEW)

    def square_button(self):
        button = tk.Button(self.button_frame, text = "x\u00b2", bg = DARK_GRAY, fg = BLUE_GREEN, font = DEFULT_FONT, borderwidth = 0, command = self.square)
        button.grid(row = 0, column = 3, sticky = tk.NSEW)

    def sqrt_button(self):
        button = tk.Button(self.button_frame, text = "\u221ax", bg = DARK_GRAY, fg = BLUE_GREEN, font = DEFULT_FONT, borderwidth = 0, command = self.sqrt)
        button.grid(row = 0, column = 2, sticky = tk.NSEW)

    def percent_button(self):
        button = tk.Button(self.button_frame, text = "%", bg = DARK_GRAY, fg = BLUE_GREEN, font = DEFULT_FONT, borderwidth = 0, command = self.percent)
        button.grid(row = 5, column = 3, sticky = tk.NSEW)

    def sin_button(self):
        button = tk.Button(self.button_frame, text = "sin", bg = DARK_GRAY, fg = BLUE_GREEN, font = DEFULT_FONT, borderwidth = 0, command = self.sin)
        button.grid(row = 1, column = 1, sticky = tk.NSEW)

    def cos_button(self):
        button = tk.Button(self.button_frame, text = "cos", bg = DARK_GRAY, fg = BLUE_GREEN, font = DEFULT_FONT, borderwidth = 0, command = self.cos)
        button.grid(row = 1, column = 2, sticky = tk.NSEW)

    def tan_button(self):
        button = tk.Button(self.button_frame, text = "tan", bg = DARK_GRAY, fg = BLUE_GREEN, font = DEFULT_FONT, borderwidth = 0, command = self.tan)
        button.grid(row = 1, column = 3, sticky = tk.NSEW)

    def equals_button(self):
        button = tk.Button(self.button_frame, text = "=", bg = DARK_GRAY, fg = LIGHT_BLUE, font = DEFULT_FONT, borderwidth = 0, command = self.evaluate)
        button.grid(row = 5, column = 4, sticky = tk.NSEW)

    def button_frame(self):
        frame = tk.Frame()
        frame.pack(expand = True, fill = "both")
        return frame

    def update_label(self):
        expr = self.total
        
        for operator, symbol in self.operations.items():
            expr = expr.replace(operator, f" {symbol} ")
        
        self.exp_display.config(text = expr)

    def update_total(self):
        self.total_display.config(text = self.expression[:10])

    def run(self):
        self.window.mainloop()

    
    
    def add_expression(self, value):
        self.add_dec = True
        self.add_op = True
        self.expression += str(value)
        self.update_total()

    def decimal(self):
        if "." in self.expression:
        	self.add_dec = False
        if self.add_dec == True:
        	self.expression += "."
        	
        	self.update_label()
        	self.update_total()
        self.add_dec = False
        
    def add_operator(self, operator):
        if self.add_op == True:
        	self.expression += operator
        	self.total += self.expression
        	self.expression = ""
        	self.update_label()
        	self.update_total()
        self.add_op = False

    def clear(self):
        self.expression = ""
        self.total = ""
        self.update_total()
        self.update_label()

    def delete(self):
        if "Math Error" in self.expression:
        		self.expression = ""
        try:
        	self.expression = self.expression[:-1]
        except IndexError:
        	pass
        
        self.update_label()
        self.update_total()
        if len(self.expression) == 0:
        	self.total = self.total[:-1]

    def square(self):
        a = self.expression
        if self.expression == "":
        	return ""
        self.total += (f"{self.expression}\u00b2")
        self.expression = str(eval(f"{self.expression}**2"))
        self.update_total()
        self.update_label()
        self.total = self.total.replace(f"{a}\u00b2", "")

    def sqrt(self):
        a = self.expression
        if self.expression == "":
        	return ""
        self.total += str(f"\u221a{self.expression}")
        self.expression = str(eval(f"{self.expression}**0.5"))
        self.update_total()
        self.update_label()
        self.total = self.total.replace(f"\u221a{a}", "")

    def percent(self):
        a = self.expression
        if self.expression == "":
        	return ""
        self.total += str(f"{self.expression}%")
        self.expression = str(eval(f"{self.expression}/100"))
        self.update_total()
        self.update_label()
        
        self.total = self.total.replace(f"{a}%", "")

    def sin(self):
        if self.expression == "":
        	return ""
        a = self.expression
        self.total += str(f"sin({self.expression})")
        self.expression = str(math.sin(eval(f"{self.expression}")))
        
        self.update_total()
        self.update_label()
        self.total = self.total.replace(f"sin({a})", "")    

    def cos(self):
        a = self.expression
        if self.expression == "":
        	return ""
        self.total += str(f"cos({self.expression})")
        self.expression = str(math.cos(eval(f"{self.expression}")))
        self.update_total()
        self.update_label()
        self.total = self.total.replace(f"cos({a})", "")
        
    def tan(self):
        a = self.expression
        if self.expression == "":
        	return ""
        self.total += str(f"tan({self.expression})")
        self.expression = str(math.tan(eval(f"{self.expression}")))
        self.update_total()
        self.update_label()
        self.total = self.total.replace(f"tan({a})", "")
    
    def evaluate(self):
        self.total += self.expression
        self.update_label()

        try:
            self.expression = str(eval(self.total))
            self.total = ""
        except Exception as e:
            self.expression = "Math Error"
        finally:
            self.update_total()

class Logic():
    def __init__(self):
        self.input = ""
    
    def evaluate(self):
        self.total = self.input
        try:
            self.expression = str(eval(self.total))
            self.total = ""
            return str(self.expression)
        except Exception as e:
            self.expression = "Math Error"
            return str(self.expression)

    def square(self):
        self.expression = self.input
        a = self.expression
        if self.expression == "":
        	return ""
        self.expression = str(eval(f"{self.expression}**2"))
        return str(self.expression)

    def sqrt(self):
        self.expression = self.input
        a = self.expression
        if self.expression == "":
        	return ""
        self.expression = str(eval(f"{self.expression}**0.5"))
        return str(self.expression)

    def percent(self):
        self.expression = self.input
        a = self.expression
        if self.expression == "":
        	return ""
        self.expression = str(eval(f"{self.expression}/100"))
        return str(self.expression)

    def sin(self):
        self.expression = self.input
        if self.expression == "":
        	return ""
        a = self.expression
        self.expression = str(math.sin(eval(f"{self.expression}")))
        return str(self.expression)

    def cos(self):
        self.expression = self.input
        a = self.expression
        if self.expression == "":
        	return ""
        self.expression = str(math.cos(eval(f"{self.expression}")))
        return str(self.expression)
        
    def tan(self):
        self.expression = self.input
        a = self.expression
        if self.expression == "":
        	return ""
        self.expression = str(math.tan(eval(f"{self.expression}")))
        return str(self.expression)



if __name__ == "__main__":
    calc = Calculator()
    calc.run()