import math
from tkinter import Tk, Label, Entry, OptionMenu, StringVar, Button, Frame
from comparesignals import SignalSamplesAreEqual
from GlobalFunctions import *

class TaskOneForm:
    def __init__(self, root, task_number):
        self.root = root
        self.root.title(f"Task {task_number} Form")

        self.amplitude = StringVar()
        self.analogFrequency = StringVar()
        self.samplingFrequency = StringVar()
        self.phaseShift = StringVar()
        self.signalType = StringVar()

        amplitude_label = Label(root, text="Amplitude:")
        amplitude_label.grid(row=0, column=0, padx=120, pady=35)
        self.amplitude_entry = Entry(root, textvariable=self.amplitude)
        self.amplitude_entry.grid(row=0, column=1, padx=10, pady=35)

        phase_shift_label = Label(root, text="Phase Shift:")
        phase_shift_label.grid(row=1, column=0, padx=120, pady=35)
        self.phase_shift_entry = Entry(root, textvariable=self.phaseShift)
        self.phase_shift_entry.grid(row=1, column=1, padx=10, pady=35)

        analog_frequency_label = Label(root, text="Analog Frequency:")
        analog_frequency_label.grid(row=2, column=0, padx=120, pady=35)
        self.analog_frequency_entry = Entry(root, textvariable=self.analogFrequency)
        self.analog_frequency_entry.grid(row=2, column=1, padx=10, pady=35)

        sampling_frequency_label = Label(root, text="Sampling Frequency:")
        sampling_frequency_label.grid(row=3, column=0, padx=120, pady=35)
        self.sampling_frequency_entry = Entry(root, textvariable=self.samplingFrequency)
        self.sampling_frequency_entry.grid(row=3, column=1, padx=10, pady=35)

        signal_type_label = Label(root, text="Signal Generation:")
        signal_type_label.grid(row=4, column=0, padx=120, pady=35)
        self.signalType.set('sin')
        signal_type_menu = OptionMenu(root, self.signalType, "sin", "cos")
        signal_type_menu.grid(row=4, column=1, padx=10, pady=35)

        submit_button = Button(root, text="Submit", command=self.submitButton, width=30)
        submit_button.grid(row=7, columnspan=2, padx=(150, 30), pady=35)

    def submitButton(self):
        amplitude = int(self.amplitude_entry.get())
        analogFrequency = int(self.analog_frequency_entry.get())
        samplingFrequency = int(self.sampling_frequency_entry.get())
        phaseShift = float(self.phase_shift_entry.get())
        signalType = self.signalType.get()

        x = []
        y = []

        for i in range(0, samplingFrequency):
            x.append(i)
            if signalType == 'sin':
                # x(t) = Asin(wt+ alpha)
                # w = 2 * pi * fa
                # t = n * Ts = n / fs
                y.append(amplitude * math.sin(2 * math.pi * analogFrequency *
                                              (i / samplingFrequency) + phaseShift))
            else:
                y.append(amplitude * math.cos(2 * math.pi * analogFrequency *
                                              (i / samplingFrequency) + phaseShift))

        SignalSamplesAreEqual('SinOutput.txt', x, y)
        # SignalSamplesAreEqual('CosOutput.txt', x, y)
        # Plot SIGNALS #
        PlotSamples(x, y)




