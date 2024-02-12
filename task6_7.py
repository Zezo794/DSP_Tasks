import math

import numpy as np

from ConvTest import ConvTest
from Task6.Shift_Fold_Signal import Shift_Fold_Signal
from comparesignal2 import SignalSamplesAreEqual
from GlobalFunctions import *
from tkinter import Tk, Label, Entry, OptionMenu, StringVar, Button, Frame

class TaskSixForm:
    def __init__(self, root, task_number):
        self.root = root
        self.root.title(f"Task {task_number} Form")

        self.Task_6_choice = StringVar()
        self.k_number = StringVar()

        Task_6_choice_label = Label(root, text="Task_6_choice:")
        Task_6_choice_label.grid(row=0, column=0, padx=120, pady=35)

        self.Task_6_choice.set("Smoothing")
        Task_6_choice_menu = OptionMenu(root, self.Task_6_choice, "Smoothing", "Sharpening",
                                        "Delaying or advancing", "Folding", "Delaying or advancing a folded",
                                        "Remove the DC",
                                        "Convolution",
                                        "Correlation",
                                        "Fast Convolution",
                                        "Fast Correlation")

        Task_6_choice_menu.grid(row=0, column=1, padx=10, pady=35)

        k_number_label = Label(root, text="Enter k_number:")
        k_number_label.grid(row=2, column=0, padx=120, pady=35)
        self.k_number_entry = Entry(root, textvariable=self.k_number)
        self.k_number_entry.grid(row=2, column=1, padx=10, pady=35)

        # Create the Submit button for the constant and operation form
        submit_button = Button(root, text="Submit", command=self.submitButtonForm6, width=30)
        submit_button.grid(row=3, columnspan=2, padx=(150, 30), pady=35)

    def submitButtonForm6(self):

        Task_6_choice = self.Task_6_choice
        k_number = self.k_number_entry

        if not isinstance(k_number, int):
            if k_number.get():
                k_number = int(k_number.get())

        if Task_6_choice.get() == "Smoothing":
            X, Y = ReadSamplesFromFile('Signal1.txt')
            # X, Y = ReadSamplesFromFile('Signal1.txt')
            self.smoothing(Y, k_number)

        elif Task_6_choice.get() == "Sharpening":
            self.DerivativeSignal()

        elif Task_6_choice.get() == "Delaying or advancing":
            X, Y = ReadSamplesFromFile(
                'input_fold.txt')
            self.Delaying_or_advancing(X, Y, k_number)

        elif Task_6_choice.get() == "Folding":
            X, Y = ReadSamplesFromFile(
                'input_fold.txt')
            self.Folding_a_signal(X, Y)

        elif Task_6_choice.get() == "Delaying or advancing a folded":
            X, Y = ReadSamplesFromFile(
                'input_fold.txt')
            self.Folding_with_Delaying_or_advancing(X, Y, 500)
            # Folding_with_Delaying_or_advancing (X,Y,-500)

        elif Task_6_choice.get() == "Remove the DC":
            X, Y = ReadSamplesFromFile3('DC_component_input.txt')
            self.Remove_DC(X,Y,500)

        elif Task_6_choice.get() == "Convolution":
            x1, y1 = ReadSamplesFromFile3('Convolution/Input_conv_Sig1.txt')
            x2, y2 = ReadSamplesFromFile3('Convolution/Input_conv_Sig2.txt')
            self.convolution(x1, y1, x2, y2)

        elif Task_6_choice.get() == "Correlation":
            x1, y1 = ReadSamplesFromFile3('Corr_input signal1.txt')
            x2, y2 = ReadSamplesFromFile3('Corr_input signal2.txt')
            self.correlation(y1, y2)

        elif Task_6_choice.get() == "Fast Convolution":
            x1, y1 = ReadSamplesFromFile3('Convolution/Input_conv_Sig1.txt')
            x2, y2 = ReadSamplesFromFile3('Convolution/Input_conv_Sig2.txt')
            self.fast_convolution(x1, y1, x2, y2)

        elif Task_6_choice.get() == "Fast Correlation":
            x1, y1 = ReadSamplesFromFile3('Corr_input signal1.txt')
            x2, y2 = ReadSamplesFromFile3('Corr_input signal2.txt')
            self.fast_correlation(x1, y1, x2, y2)

    @staticmethod
    def smoothing(x, k):
        out_from_smooth = []
        for i in range(len(x) - k + 1):
            temp_sum = 0
            for j in range(k):
                temp_sum += x[i + j]
            out_from_smooth.append(temp_sum / k)
        SignalSamplesAreEqual('OutMovAvgTest1.txt', out_from_smooth)
        # SignalSamplesAreEqual('OutMovAvgTest2.txt', out_from_smooth)
        return out_from_smooth

    @staticmethod
    def DerivativeSignal():
        InputSignal = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0, 50.0, 51.0, 52.0, 53.0, 54.0, 55.0, 56.0, 57.0, 58.0, 59.0, 60.0, 61.0, 62.0, 63.0, 64.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 71.0, 72.0, 73.0, 74.0, 75.0, 76.0, 77.0, 78.0, 79.0, 80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0, 100.0]
        expectedOutput_first = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                1, 1, 1, 1, 1, 1]
        expectedOutput_second = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0]

        """
        Write your Code here:
        Start
        """

        FirstDrev = [InputSignal[i] - InputSignal[i - 1] for i in range(1, len(InputSignal))]
        SecondDrev = [InputSignal[i + 1] - 2 * InputSignal[i] + InputSignal[i - 1] for i in range(1, len(InputSignal) - 1)]


        """
        End
        """

        """
        Testing your Code
        """
        if ((len(FirstDrev) != len(expectedOutput_first)) or (len(SecondDrev) != len(expectedOutput_second))):
            print("mismatch in length")
            return
        first = second = True
        for i in range(len(expectedOutput_first)):
            if abs(FirstDrev[i] - expectedOutput_first[i]) < 0.01:
                continue
            else:
                first = False
                print("1st derivative wrong")
                return
        for i in range(len(expectedOutput_second)):
            if abs(SecondDrev[i] - expectedOutput_second[i]) < 0.01:
                continue
            else:
                second = False
                print("2nd derivative wrong")
                return
        if (first and second):
            print("Derivative Test case passed successfully")
        else:
            print("Derivative Test case failed")
        return

    @staticmethod
    def Delaying_or_advancing(x,y,k):
        x=list(x)
        y=list(y)
        result_x = [a + k for a in x]
        result_y = y
        return result_x, result_y

    @staticmethod
    def Folding_a_signal(x,y):
        output_signals = {}
        signal_map = {}
        for i in range(len(x)):
            signal_map[x[i]] = y[i]
        for i, j in signal_map.items():
            output_signals[i] = signal_map[-i]
        Shift_Fold_Signal('Output_fold.txt',list(output_signals.keys()),list(output_signals.values()))
        return output_signals.keys(),output_signals.values()

    @staticmethod
    def Folding_with_Delaying_or_advancing (x,y,k):
        output_signals_X_1,output_signals_Y_1= TaskSixForm.Folding_a_signal(x,y)
        output_signals2_x,output_signals2_y = TaskSixForm.Delaying_or_advancing(output_signals_X_1,output_signals_Y_1,k)
        Shift_Fold_Signal('Output_ShifFoldedby500.txt',output_signals2_x,list(output_signals_Y_1))
        #Shift_Fold_Signal( 'C:/Users/Asus/Desktop/task5/Task 5/Task6/TestCases6/Shifting and Folding/Output_ShiftFoldedby-500.txt', output_signals2_x, list(output_signals_Y_1))

    @staticmethod
    def Remove_DC(x,y,fs):
        amplitude,phase=from_T_to_F(x, y, fs)
        amplitude[0] = np.abs(complex(0, 0))
        phase[0] = np.angle(complex(0, 0))
        final_output=from_F_to_T(amplitude,phase)
        final_output = [round(z , 3) for z in final_output ]
        SignalSamplesAreEqual('DC_component_output.txt', final_output)

    @staticmethod
    def convolution(x1, y1, x2, y2):
        x = [i for i in range(int(x1[0] + x2[0]), int(x1[-1] + x2[-1]) + 1)]
        y = []
        # y1 = [1, 2, 1, 1]
        # y2 = [1, -1, 0, 0, 1, 1]
        # y = [1, 1, -1, 0, 0, 3, 3, 2, 1]
        for i in range(0, len(x)):
            temp = 0
            for j in range(0, i + 1):
                k = i - j
                if j > len(y1) - 1 or k > len(y2) - 1:
                    continue
                temp += y1[j] * y2[k]
            y.append(int(temp))
        ConvTest(x, y)

    @staticmethod
    def correlation(y1, y2):
        corr = [0] * len(y1)
        normalize = [0] * len(y1)
        for i in range(len(y1)):
            for j in range(len(y2)):
                corr[i] += y1[j] * y2[j]
            y2 = y2[1:] + y2[:1]
            corr[i] /= len(y1)
            normalize[i] = corr[i] / ((1 / len(y1)) * math.sqrt(sum(x ** 2 for x in y1) *
                                                                sum(x ** 2 for x in y2)))
        SignalSamplesAreEqual('CorrOutput.txt', normalize)
        return corr

    @staticmethod
    def fast_convolution(x1, y1, x2, y2):
        N1 = len(y1)
        N2 = len(y2)
        X = [i for i in range(int(x1[0] + x2[0]), int(x1[-1] + x2[-1]) + 1)]
        N = N1 + N2 - 1
        Y1 = np.pad(y1, (0, (N - N1)))
        Y2 = np.pad(y2, (0, (N - N2)))
        DFTy1 = from_T_to_F(X, Y1)
        DFTy2 = from_T_to_F(X, Y2)
        result = [a * b for a, b in zip(DFTy1, DFTy2)]
        IDFTresult = from_F_to_T(X, result)
        ConvTest(X, IDFTresult)
        return IDFTresult

    @staticmethod
    def fast_correlation(x1, y1, x2, y2):
        N1 = len(y1)
        N2 = len(y2)
        N = max(N1, N2)
        X = [i for i in range(N)]
        Y1 = np.pad(y1, (0, (N - N1)))
        Y2 = np.pad(y2, (0, (N - N2)))
        correlation = []
        for i in range(N):
            DFTy1 = from_T_to_F(X, Y1)
            DFTy2 = from_T_to_F(X, Y2)
            result = [a * np.conj(b) for a, b in zip(DFTy1, DFTy2)]
            IDFTresult = from_F_to_T(X, result)
            correlation.append(IDFTresult[0] / N)
            tmp = list(Y2[1:])
            tmp.append(Y2[0])
            Y2 = tmp
        SignalSamplesAreEqual('Corr_Output.txt', correlation)
        return correlation


