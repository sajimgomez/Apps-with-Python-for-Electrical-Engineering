from math import pi, e, log

import cmath, tkinter

from tkinter import ttk


Root = tkinter.Tk()

Root.title('Grounding Grid Design With IEEE-std_80')

IconImageApp = tkinter.PhotoImage(file = 'Ifgrid.png')

Root.iconphoto(False, IconImageApp)

Frame1 = tkinter.Frame(Root)

Frame1.pack()


ExistingData = tkinter.LabelFrame(Frame1, text = 'Existing network data')

ExistingData.grid(row = 0, column = 0)

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


DesignData = tkinter.LabelFrame(Frame1, text = 'Design Data')

DesignData.grid(row = 0, column = 1)

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

MeCondMat = ttk.Combobox(DesignData, values = ['vfdjlvn', 'fnljfn', 'hsvdsld']).grid(row = 8, column = 1)



Results = tkinter.LabelFrame(Frame1, text = 'Results')

Results.grid(row = 1, column = 0)

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


Root.mainloop()