from tkinter import filedialog
import tkinter as tk
import QuanTest1
import QuanTest2
from GlobalFunctions import *

class TaskThreeForm:
    def __init__(self, root, task_number):
        self.root = root
        self.root.title(f"Task {task_number} Form")

        # Header label
        header_label = tk.Label(root, text="Signal Quantization", font=("Arial", 20, "bold"))
        header_label.pack(pady=10)

        # File selection field
        file_label = tk.Label(root, text="Signal")
        file_label.pack()
        self.file_entry = tk.Entry(root, width=30)
        self.file_entry.pack(pady=5)

        def browse_file():
            file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(tk.END, file_path)

        browse_button = tk.Button(root, text="Browse", command=browse_file)
        browse_button.pack(pady=20)

        # Number of bits field
        bits_label = tk.Label(root, text="Number of Bits")
        bits_label.pack()
        self.bits_entry = tk.Entry(root, width=30)
        self.bits_entry.pack(pady=5)

        # Submit button
        submit_button = tk.Button(root, text="Submit", command=self.process_form_data)
        submit_button.pack(pady=25)

    def process_form_data(self):
        file_path = self.file_entry.get()
        num_bits = int(self.bits_entry.get())

        # Read the samples from the path
        n, x = ReadSamplesFromFile(file_path)

        # Calculate The outputs
        min_val, max_val, num_lvls, resolution, ranges, mid_points, interval_index, xq, \
            encoded_values, eq, eq_square, N = self.calculate_values(x, num_bits)
        # Print the values for demonstration
        # print("Display", n, x)
        # print("Number of Bits:", num_bits)
        # print("Number of Levels:", num_lvls)
        # print("Minimum Value:", min_val)
        # print("Maximum Value:", max_val)
        # print("Resolution:", resolution)
        # print("Updated Ranges:", ranges)
        # print("Mid Points:", mid_points)
        # print("Interval Index:", interval_index)
        # print("xq:", xq)
        # print("Encoded Values:", encoded_values)
        # print("eq:", eq)
        # print("eq_square:", eq_square)
        # print("N:", N)

        QuanTest1.QuantizationTest1('Quan1_Out.txt', encoded_values, xq)
        # QuanTest2.QuantizationTest2('Quan2_Out.txt', interval_index, encoded_values, xq, eq)
        PlotSamples2(n, x, xq)
    @staticmethod
    def calculate_values(x, num_bits):
        min_val = min(x)
        max_val = max(x)
        num_lvls = 2 ** num_bits
        resolution = (max_val - min_val) / num_lvls
        ranges = [(min_val + i * resolution, min_val + (i + 1) * resolution) for i in range(num_lvls)]
        mid_points = [(start + end) / 2 for start, end in ranges]
        interval_index = np.zeros(len(x), dtype=int)
        xq = np.zeros(len(x), dtype=float)
        for i, val in enumerate(x):
            index = np.argmin(np.abs(np.array(mid_points) - val))
            interval_index[i] = index + 1
            xq[i] = mid_points[interval_index[i] - 1]
            encoded_values = [format(val - 1, '0{}b'.format(num_bits)) for val in interval_index]
            eq = xq - x
            eq_square = np.square(eq)
            N = np.mean(eq_square)
        return min_val, max_val, num_lvls, resolution, ranges, mid_points, interval_index, \
            xq, encoded_values, eq, eq_square, N
