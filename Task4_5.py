import numpy as np
from comparesignals import *
from Task1 import *
from GlobalFunctions import *

class TaskFourForm:
    def __init__(self, root, task_number, X, Y):
        self.root = root
        self.root.title(f"Task {task_number} Form")
        self.X = X
        self.Y = Y

        self.frequency_domain = StringVar()
        self.Sampling_Frequency = StringVar()
        self.modified_phase = StringVar()
        self.modified_amplitude = StringVar()
        self.modified_signal_index = StringVar()
        self.m = StringVar()
        self.comp_list = []

        frequency_domain_label = Label(root, text="Frequency Domain:")
        frequency_domain_label.grid(row=0, column=0, padx=120, pady=30)

        self.frequency_domain.set("Apply Fourier Transform")
        frequency_domain_menu = OptionMenu(root, self.frequency_domain,
                                           "Apply Fourier Transform",
                                           "Modify Amplitude and Phase",
                                           "Signal Reconstruction",
                                           "Computing DCT",
                                           "Remove DC Component")
        frequency_domain_menu.grid(row=0, column=1, padx=10, pady=30)

        Sampling_Frequency_label = Label(root, text="Enter Sampling Frequency:")
        Sampling_Frequency_label.grid(row=2, column=0, padx=120, pady=30)
        self.Sampling_Frequency_entry = Entry(root, textvariable=self.Sampling_Frequency)
        self.Sampling_Frequency_entry.grid(row=2, column=1, padx=10, pady=30)

        modified_signal_index_label = Label(root, text="Enter modified signal index:")
        modified_signal_index_label.grid(row=3, column=0, padx=120, pady=30)
        self.modified_signal_index_entry = Entry(root, textvariable=self.modified_signal_index)
        self.modified_signal_index_entry.grid(row=3, column=1, padx=10, pady=30)

        modified_amplitude_label = Label(root, text="Enter modified amplitude:")
        modified_amplitude_label.grid(row=4, column=0, padx=120, pady=30)
        self.modified_amplitude_entry = Entry(root, textvariable=self.modified_amplitude)
        self.modified_amplitude_entry.grid(row=4, column=1, padx=10, pady=30)

        modified_phase_label = Label(root, text="Enter modified phase:")
        modified_phase_label.grid(row=5, column=0, padx=120, pady=30)
        self.modified_phase_entry = Entry(root, textvariable=self.modified_phase)
        self.modified_phase_entry.grid(row=5, column=1, padx=10, pady=30)

        m_label = Label(root, text="Enter m:")
        m_label.grid(row=6, column=0, padx=120, pady=30)
        self.m_entry = Entry(root, textvariable=self.m)
        self.m_entry.grid(row=6, column=1, padx=10, pady=30)

        # Create the Submit button for the constant and operation form
        submit_button = Button(root, text="Submit", command=self.submitButtonForm4, width=30)
        submit_button.grid(row=7, columnspan=2, padx=(150, 30), pady=30)

    def submitButtonForm4(self):
        x2 = self.X
        y2 = self.Y

        frequency_domain = self.frequency_domain
        Sampling_Frequency = self.Sampling_Frequency_entry
        modified_phase = self.modified_phase_entry
        modified_amplitude = self.modified_amplitude_entry
        modified_signal_index = self.modified_signal_index_entry
        comp_list = self.comp_list
        m = self.m

        if not isinstance(self.modified_phase_entry, float):
            if self.modified_phase_entry.get():
                modified_phase = float(self.modified_phase_entry.get())

        if not isinstance(self.modified_amplitude_entry, float):
            if self.modified_amplitude_entry.get():
                modified_amplitude = float(self.modified_amplitude_entry.get())

        if not isinstance(self.modified_signal_index_entry, float):
            if self.modified_signal_index_entry.get():
                modified_signal_index = float(self.modified_signal_index_entry.get())

        if not isinstance(self.Sampling_Frequency_entry, float):
            if self.Sampling_Frequency_entry.get():
                Sampling_Frequency = float(self.Sampling_Frequency_entry.get())

        if not isinstance(self.m_entry, float):
            if self.m_entry.get():
                m = int(self.m_entry.get())

        if frequency_domain.get() == "Apply Fourier Transform":
            self.comp_list = self.from_T_to_F(x2, y2, Sampling_Frequency)

        elif frequency_domain.get() == "Modify Amplitude and Phase":
            self.modifiy_phase_amplitude(comp_list, modified_signal_index,
                                         modified_phase, modified_amplitude,
                                        Sampling_Frequency)

        elif frequency_domain.get() == "Signal Reconstruction":
            x2, y2 = ReadSamplesFromFile2('lol.txt')
            self.from_F_to_T(x2, y2)

        elif frequency_domain.get() == "Computing DCT":
            x, X = ReadSamplesFromFile3('DCT_input.txt')
            self.comp_list = self.computingDCT(X, m)

        elif frequency_domain.get() == "Remove DC Component":
            x2, y2 = ReadSamplesFromFile3('DC_component_input.txt')
            self.comp_list = self.removeDC(x2, y2)

    @staticmethod
    def from_T_to_F(X,Y,fs):
        complex_list = []
        lengthOfSignal=len(X)

        for i in range(lengthOfSignal):
            Xk=0
            for n in range(lengthOfSignal):
                Xk += Y[n] * np.exp(-2j * np.pi * i * n / lengthOfSignal)
            complex_list.append(Xk)

        amplitude = np.abs(complex_list)
        phase = np.angle(complex_list)
        freq = np.arange(lengthOfSignal) * np.pi * 2 * fs / lengthOfSignal
        showPlotTask3(freq, amplitude, phase)
        save_Task4_to_txt('lol.txt', amplitude, phase)
        #for task 4
        return complex_list

    @staticmethod
    def modifiy_phase_amplitude(complexNo,index,newPhase,newAmplitude,fs):
        comp=complex(newAmplitude * np.cos(newPhase), newAmplitude * np.sin(newPhase))
        complexNo[int(index)] = comp
        lengthOfSignal=len(complexNo)
        amplitude = np.abs(complexNo)
        phase = np.angle(complexNo)
        freq = np.arange(lengthOfSignal) * np.pi * 2 * fs / lengthOfSignal
        showPlotTask3(freq, amplitude, phase)
        save_Task4_to_txt('modify.txt', amplitude, phase)

    @staticmethod
    def from_F_to_T(X,Y):
        list_normal = []
        complex_numbers = [complex(r * np.cos(i), r * np.sin(i)) for r, i in zip(X, Y)]
        lengthOfSignal=len(X)

        for i in range(lengthOfSignal):
            Xn=0
            for n in range(lengthOfSignal):
                Xn += complex_numbers[n] * np.exp(2j * np.pi * i * n / lengthOfSignal)
            Xn/=lengthOfSignal
            list_normal.append(Xn)
        x=[]
        y=[]
        y2=[]
        for i, complex_number in enumerate(list_normal):
            real_part = round(complex_number.real)
            real_part2=complex_number.real
            imaginary_part = round(complex_number.imag)
            x.append(i)
            y.append(real_part)
            y2.append(real_part2)
            # print(f"{i} {real_part} {imaginary_part}")

        PlotSamples(x, y)
        # SignalSamplesAreEqual(r'Output_Signal_IDFT.txt', x, y)
        return y2

    @staticmethod
    def computingDCT(X, m):
        complex_list = []
        N=len(X)
        for k in range(N):
            Yk=0
            for n in range(N):
                Yk += X[n] * math.cos((math.pi / (4 * N)) * ((2 * n) - 1) * (2 * k - 1))
            Yk *= np.sqrt(2 / N)
            complex_list.append(Yk)
        x = [0] * N
        SignalSamplesAreEqual('DCT_output.txt', x, complex_list)
        save_Task5_to_txt('lol3.txt', x, complex_list, m)

    @staticmethod
    def removeDC(X,Y):
        mean = np.mean(Y)
        complex_list = [round(y - mean, 3) for y in Y]
        SignalSamplesAreEqual('DC_component_output.txt', X, complex_list)



