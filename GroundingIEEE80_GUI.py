from math import pi, e, log

import cmath, tkinter

from tkinter import ttk


Root = tkinter.Tk()

Root.title('Grounding Grid Design With IEEE-std_80')

IconImageApp = tkinter.PhotoImage(file = 'Ifgrid.png')

ImageApp = tkinter.PhotoImage(file = 'Step-and-touch-voltage.png')

Root.iconphoto(False, IconImageApp)

Frame1 = tkinter.Frame(Root)

Frame1.pack()

ImageAppCont1 = tkinter.Label(Frame1, image = ImageApp).grid(row = 2, column = 0, columnspan = 2)


TypeOfConductors = ['Cooper, annealed soft-drawn 100% conductivity', 'Cooper, commercial hard-drawn 97% conductivity', 'Cooper-clad steel wire 40% conductivity', 'Cooper-clad steel wire 30% conductivity', 'Cooper-clad steel rod 20% conductivity', 'Aluminum, EC grade 61% conductivity', 'Aluminum, 5005 alloy 53.5% conductivity', 'Aluminum, 6201 alloy 52.5% conductivity', 'Aluminum-clad steel wire 20.3% conductivity', 'Steel, 1020 10.8% conductivity', 'Stainless-clad steel rod 9.8% conductivity', 'Zinc-coated steel rod 8.6% conductivity', 'Stainless steel, 304 2.4% conductivity']

CondProperties = ['αr at 20°C (1/°C)', 'Ko at 0°C (°C)', 'Fusing Temperature Tm', 'ρr at 20°C (μΩcm)', 'TCAP Thermal capacity (J/cm3°C)', 'Kf']

CondDataProperties = [[0.00393, 234, 1083, 1.72, 3.42, 7], [0.00381, 242, 1084, 1.78, 3.42, 7.06], [0.00378, 245, 1084, 4.4, 3.85, 10.45], [0.00378, 245, 1084, 5.86, 3.85, 12.06], [0.00378, 245, 1084, 8.62, 3.85, 14.64], [0.00403, 228, 657, 2.86, 2.56, 12.12], [0.00353, 263, 652, 3.22, 2.6, 12.41], [0.00347, 268, 654, 3.28, 2.6, 12.47], [0.0036, 258, 657, 8.48, 3.58, 17.2], [0.00316, 605, 1510, 15.9, 3.28, 15.95], [0.0016, 605, 1400, 17.5, 4.44, 14.72], [0.0032, 293, 419, 20.1, 3.93, 28.96], [0.0013, 749, 1400, 72, 4.03, 30.05]]


ExistingData = tkinter.LabelFrame(Frame1, text = 'Existing network data', padx = 20, pady = 20)

ExistingData.grid(row = 0, column = 0, padx = 5, pady = 0)

MaxFaultClTime = tkinter.Label(ExistingData, text = 'Maximum Fault Clearance Time in seconds: ').grid(row = 0, column = 0)

M_F_C_T = tkinter.Entry(ExistingData).grid(row = 0, column = 1)

GroundRes = tkinter.Label(ExistingData, text = 'Ground Resistivity in Ohm-meter: ').grid(row = 1, column = 0)

G_R = tkinter.Entry(ExistingData).grid(row = 1, column = 1)

AmbTemp = tkinter.Label(ExistingData, text = 'Ambient Temperature in °C: ').grid(row = 2, column = 0)

A_T = tkinter.Entry(ExistingData).grid(row = 2, column = 1)

MaxFaultCurr = tkinter.Label(ExistingData, text = 'Maximum Fault Current in Kiloamps: ').grid(row = 3, column = 0)

M_F_C = tkinter.Entry(ExistingData).grid(row = 3, column = 1)

MaxFaultCurrGPR = tkinter.Label(ExistingData, text = 'Maximum Fault Current that contributes to the Ground Potential Rise in Kiloamps: ').grid(row = 4, column = 0)

M_F_C_GPR = tkinter.Entry(ExistingData).grid(row = 4, column = 1)

XtoR_ratio_MFC = tkinter.Label(ExistingData, text = 'X (reactance) to R (resistance) ratio for the Maximum Fault Current: ').grid(row = 5, column = 0)

X_R_MFC = tkinter.Entry(ExistingData).grid(row = 5, column = 1)

XtoR_ratio_GPR = tkinter.Label(ExistingData, text = 'X (reactance) to R (resistance) ratio for the Maximum Fault Current that contributes to the Ground Potential Rise: ').grid(row = 6, column = 0)

X_R_GPR = tkinter.Entry(ExistingData).grid(row = 6, column = 1)

fnomSys = tkinter.Label(ExistingData, text = 'Nominal frecuence of the System (50Hz or 60Hz) in Hz: ').grid(row = 7, column = 0)

f_nom = tkinter.Entry(ExistingData).grid(row = 7, column = 1)


DesignData = tkinter.LabelFrame(Frame1, text = 'Design Data', padx = 20, pady = 20)

DesignData.grid(row = 0, column = 1, padx = 5, pady = 10)

ResOfCrushedRock = tkinter.Label(DesignData, text = 'Resistivity of Crushed Rock in Ohm-meter: ').grid(row = 0, column = 0)

R_C_R = tkinter.Entry(DesignData).grid(row = 0, column = 1)

ThickOfCrushRockLayer = tkinter.Label(DesignData, text = 'Thickness Of Crushed Rock Layer in meters: ').grid(row = 1, column = 0)

T_C_R_L = tkinter.Entry(DesignData).grid(row = 1, column = 1)

MeBurDep = tkinter.Label(DesignData, text = 'Mesh Burial Depth in meters: ').grid(row = 2, column = 0)

M_B_D = tkinter.Entry(DesignData).grid(row = 2, column = 1)

MeLen = tkinter.Label(DesignData, text = 'Mesh Length in meters: ').grid(row = 3, column = 0)

M_L = tkinter.Entry(DesignData).grid(row = 3, column = 1)

MeWid = tkinter.Label(DesignData, text = 'Mesh Width in meters: ').grid(row = 4, column = 0)

M_W = tkinter.Entry(DesignData).grid(row = 4, column = 1)

SpacBetwParCond = tkinter.Label(DesignData, text = 'Spacing between parallel conductors in meters: ').grid(row = 5, column = 0)

S_B_P_C = tkinter.Entry(DesignData).grid(row = 5, column = 1)

NumbOfRods = tkinter.Label(DesignData, text = 'Number of Rods: ').grid(row = 6, column = 0)

N_O_R = tkinter.Entry(DesignData).grid(row = 6, column = 1)

LenOfRods = tkinter.Label(DesignData, text = 'Length of each Rod: ').grid(row = 7, column = 0)

L_O_R = tkinter.Entry(DesignData).grid(row = 7, column = 1)

CondMat = tkinter.Label(DesignData, text = 'Mesh Conductor Material: ').grid(row = 8, column = 0)

MeCondMat = ttk.Combobox(DesignData, values = TypeOfConductors).grid(row = 8, column = 1, pady = 5)



Results = tkinter.LabelFrame(Frame1, text = 'Results', padx = 20, pady = 20)

Results.grid(row = 1, column = 0, pady = 0)

ConSize = tkinter.Label(Results, text = 'Minimum Conductor Size in KCM (Kilo Circular Mil): ').grid(row = 0, column = 0)

C_size = ttk.Entry(Results, state = 'readonly').grid(row = 0, column = 1)

ComConSize = tkinter.Label(Results, text = 'Comercial Conductor Size in KCM (Kilo Circular Mil) or AWG: ').grid(row = 1, column = 0)

C_C_S = ttk.Entry(Results, state = 'readonly').grid(row = 1, column = 1)

MeshResis = tkinter.Label(Results, text = 'Mesh Resistance in Ohm: ').grid(row = 2, column = 0)

M_R = ttk.Entry(Results, state = 'readonly').grid(row = 2, column = 1)

GrPotRise = tkinter.Label(Results, text = 'Ground Potential Rise (GPR) in volts: ').grid(row = 3, column = 0)

G_P_R = ttk.Entry(Results, state = 'readonly').grid(row = 3, column = 1)

AlloTouVol = tkinter.Label(Results, text = 'Allowable Touch voltage for 50Kg person in volts: ').grid(row = 4, column = 0)

A_T_V = ttk.Entry(Results, state = 'readonly').grid(row = 4, column = 1)

AlloStepVol = tkinter.Label(Results, text = 'Allowable Step voltage for 50Kg person in volts: ').grid(row = 5, column = 0)

A_S_V = ttk.Entry(Results, state = 'readonly').grid(row = 5, column = 1)

MaxMesVol = tkinter.Label(Results, text = 'Maximum Mesh voltage "Em" in volts: ').grid(row = 6, column = 0)

M_M_V = ttk.Entry(Results, state = 'readonly').grid(row = 6, column = 1)

MaxStepVol = tkinter.Label(Results, text = 'Maximum Step voltage "Es" in volts: ').grid(row = 7, column = 0)

M_S_V = ttk.Entry(Results, state = 'readonly').grid(row = 7, column = 1)


Calc = tkinter.Button(Frame1, text = 'Calculate').grid(row = 1, column = 1)


Root.mainloop()