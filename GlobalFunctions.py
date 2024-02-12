import matplotlib.pyplot as plt
import numpy as np

def PlotSamples(x, y):
    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6))

    # Continuous representation
    ax1.plot(x, y)
    ax1.set_title('Continuous Representation')
    ax1.set_xlabel('Sample Index')
    ax1.set_ylabel('Amplitude')

    # Discrete representation
    # stem is a function for creating each data point is represented by a vertical line
    ax2.stem(x, y, use_line_collection=True)
    ax2.set_title('Discrete Representation')
    ax2.set_xlabel('Sample Index')
    ax2.set_ylabel('Amplitude')

    # Space between the two plots
    plt.tight_layout()
    plt.show()

def PlotSamples2(n, x, xq):

    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6))

    # # Continuous representation
    # ax1.plot(x, y)
    # ax1.set_title('Continuous Representation')
    # ax1.set_xlabel('Sample Index')
    # ax1.set_ylabel('Amplitude')

    # Discrete representation before quantization
    ax1.stem(n, x, use_line_collection=True)
    ax1.set_title('Discrete Representation')
    ax1.set_xlabel('n')
    ax1.set_ylabel('X')

    # Discrete representation after quantization
    ax2.stem(n, xq, use_line_collection=True)
    ax2.set_title('Discrete Representation')
    ax2.set_xlabel('n')
    ax2.set_ylabel('Xq')

    # Space between the two plots
    plt.tight_layout()
    plt.show()

def showPlotTask3(freq, amplitude, phase):
    phase_degrees = np.degrees(phase)
    plt.figure(figsize=(5, 5))
    plt.subplot(2, 1, 1)
    plt.plot(freq, amplitude)
    plt.title('Frequency vs Amplitude')
    plt.xlabel('Frequency ')
    plt.ylabel('Amplitude')
    plt.grid()

    # Plot frequency versus phase
    plt.subplot(2, 1, 2)
    plt.plot(freq, phase_degrees)
    plt.title('Frequency vs Phase')
    plt.xlabel('Frequency')
    plt.ylabel('Phase')
    plt.grid()

    plt.tight_layout()
    plt.show()

def ReadSamplesFromFile(path):
    file = open(path, 'r')
    signalType = bool(file.readline())
    isPeriodic = bool(file.readline())

    N1 = int(file.readline())
    x = []
    y = []
    for i in range(0, N1):
        line = file.readline().split()
        sampleIndex = int(line[0])
        x.append(sampleIndex)
        sampleAmplitude = float(line[1])
        y.append(sampleAmplitude)

    file.close()
    return x, y

def ReadSamplesFromFile2(path):
    file = open(path, 'r')
    signalType = bool(file.readline())
    isPeriodic = bool(file.readline())

    N1 = int(file.readline())
    x = []
    y = []
    for i in range(0, N1):
        line = file.readline().split(',')
        sampleIndex = float(line[0].rstrip('f\n'))
        x.append(sampleIndex)
        sampleAmplitude = float(line[1].rstrip('f\n'))
        y.append(sampleAmplitude)

    file.close()
    return x, y

def ReadSamplesFromFile3(path):
    file = open(path, 'r')
    signalType = bool(file.readline())
    isPeriodic = bool(file.readline())

    N1 = int(file.readline())
    x = []
    y = []
    for i in range(0, N1):
        line = file.readline().split(' ')
        sampleIndex = float(line[0].rstrip('f\n'))
        x.append(sampleIndex)
        sampleAmplitude = float(line[1].rstrip('f\n'))
        y.append(sampleAmplitude)

    file.close()
    return x, y

def save_Task4_to_txt(filename, amplitude, phase):
    with open(filename, 'w') as file:
        file.write(f"{0}\n")
        file.write(f"{1}\n")
        file.write(f"{len(amplitude)}\n")
        for a, p in zip(amplitude, phase):
            file.write(f"{a:.14f},{p:.14f}f\n")

def save_Task5_to_txt(filename, amplitude, phase, m):
    with open(filename, 'w') as file:
        file.write(f"{0}\n")
        file.write(f"{1}\n")
        file.write(f"{len(amplitude)}\n")
        for i, (a, p) in enumerate(zip(amplitude, phase)):
            if i < m:
                file.write(f"{a:.0f},{p:.14f}\n")

def from_T_to_F(X, Y, fs = 0):
    complex_list = []
    lengthOfSignal = len(X)

    for i in range(lengthOfSignal):
        Xk = 0
        for n in range(lengthOfSignal):
            Xk += Y[n] * np.exp(-2j * np.pi * i * n / lengthOfSignal)
        complex_list.append(Xk)

    # for task 9
    return complex_list

    # amplitude = np.abs(complex_list)
    # phase = np.angle(complex_list)
    # freq = np.arange(lengthOfSignal) * np.pi * 2 * fs / lengthOfSignal
    # showPlotTask3(freq, amplitude, phase)
    # save_Task4_to_txt('lol.txt', amplitude, phase)
    # for task 6
    # return amplitude, phase


def from_F_to_T(X,Y):
    N = len(X)
    XN = []
    for n in range(N):
        tmp = 0
        for k in range(N):
            tmp += Y[k] * np.exp(2j * np.pi * n * k / N)
        XN.append(round(tmp.real,4) / N)
    return XN