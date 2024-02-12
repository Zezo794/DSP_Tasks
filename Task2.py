from tkinter import Tk, Label, Entry, OptionMenu, StringVar, Button, Frame
from comparesignals import SignalSamplesAreEqual
from GlobalFunctions import *
class TaskTwoForm:
    def __init__(self, root, task_number, X, Y):
        self.root = root
        self.root.title(f"Task {task_number} Form")
        self.X = X
        self.Y = Y

        self.operation = StringVar()
        self.constant = StringVar()
        self.normalize = StringVar()

        # Create and layout widgets for the constant and operation form
        constant_label = Label(root, text="Constant Value:")
        constant_label.grid(row=0, column=0, padx=120, pady=35)
        self.constant_entry = Entry(root, textvariable=self.constant)
        self.constant_entry.grid(row=0, column=1, padx=10, pady=35)

        operation_label = Label(root, text="Arithmetic Operation:")
        operation_label.grid(row=1, column=0, padx=120, pady=35)

        self.operation.set("Addition")
        operation_menu = OptionMenu(root, self.operation, "Addition", "Subtraction", "Multiplication",
                                    "Squaring", "Shifting", "Normalization", "Accumulation")
        operation_menu.grid(row=1, column=1, padx=10, pady=35)

        normalize_label = Label(root, text="Normalize coefficient:")
        normalize_label.grid(row=2, column=0, padx=120, pady=35)

        self.normalize.set("-1 to 1")
        normalize_menu = OptionMenu(root, self.normalize, "-1 to 1", "0 to 1", )
        normalize_menu.grid(row=2, column=1, padx=10, pady=35)

        # Create the Submit button for the constant and operation form
        submit_button = Button(root, text="Submit", command=self.submitButtonForm2, width=30)
        submit_button.grid(row=3, columnspan=2, padx=(150, 30), pady=35)

    def submitButtonForm2(self):
        x = self.X
        y = self.Y
        x1 = []
        y1 = []
        n = self.normalize.get()

        if self.constant.get():
            constant = float(self.constant_entry.get())

        if self.operation.get() == "Addition":
            x2, y2 = ReadSamplesFromFile(
                'signal2.txt')
            x1, y1 = self.addition(x, y, x2, y2)
        elif self.operation.get() == "Subtraction":
            x2, y2 = ReadSamplesFromFile(
                'signal2.txt')
            x1, y1 = self.subtraction(x, y, x2, y2)
        elif self.operation.get() == "Multiplication":
            x1, y1 = self.multiplication(x, y, constant)
        elif self.operation.get() == "Squaring":
            x1, y1 = self.squaring(x, y)
        elif self.operation.get() == "Shifting":
            x1, y1 = self.shifting(x, y, constant)
        elif self.operation.get() == "Normalization":
            if n[0] == '-':
                flag = 0
            else:
                flag = 1
            min_val = min(y)
            max_val = max(y)
            x1, y1 = self.normalization(x, y, min_val, max_val, flag)
        elif self.operation.get() == "Accumulation":
            x1, y1 = self.accumulation(x, y)
        # Plot SIGNALS #
        PlotSamples(x1, y1)
        SignalSamplesAreEqual("Signal1+signal2.txt", x, y)

    @staticmethod
    def addition(x, y, x2, y2):
        result_x = x
        result_y = [a + b for a, b in zip(y, y2)]
        return result_x, result_y

    @staticmethod
    def subtraction(x, y, x2, y2):
        result_x = x
        result_y = [abs(a - b) for a, b in zip(y, y2)]
        return result_x, result_y

    @staticmethod
    def multiplication(x, y, constant):
        result_x = x
        result_y = [a * constant for a in y]
        return result_x, result_y

    @staticmethod
    def squaring(x, y):
        result_x = x
        result_y = [a ** 2 for a in y]
        return result_x, result_y

    @staticmethod
    def shifting(x, y, constant):
        result_x = [a - constant for a in x]
        result_y = y
        return result_x, result_y

    @staticmethod
    def normalization(x, y, min_val, max_val,flag):
        result_x = x
        if flag:
            result_y = [(a - min_val) / (max_val - min_val) for a in y]
        else:
            result_y = [2*(a - min_val) / (max_val - min_val) -1 for a in y]
        return result_x, result_y

    @staticmethod
    def accumulation(x, y):
        result_x = x
        result_y = [sum(y[:i + 1]) for i in range(len(y))]
        return result_x, result_y



