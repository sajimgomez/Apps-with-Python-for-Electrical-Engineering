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

Frame2 = tkinter.Frame(Root, bg = 'blue')

ImageAppCont1 = tkinter.Label(Frame1, image = ImageApp).grid(row = 2, column = 0)

MenuBar = tkinter.Menu(Root)

Root.config(menu = MenuBar)

GroundingSysConfig = tkinter.Menu(MenuBar)

MenuBar.add_cascade(label = 'Grounding grid Configuration', menu = GroundingSysConfig)

def ShowDepthElec() :

    Frame1.destroy()

    Frame2.pack(fill = 'both', expand = 1)

GroundingSysConfig.add_command(label = 'Depth Electrode', command = ShowDepthElec)

def ShowIEEE80() :

    Frame2.destroy()

    Frame1.pack()

GroundingSysConfig.add_command(label = 'Rectangular or L-shaped mesh', command = ShowIEEE80)


TypeOfConductors = ['Cooper, annealed soft-drawn 100% conductivity', 'Cooper, commercial hard-drawn 97% conductivity', 'Cooper-clad steel wire 40% conductivity', 'Cooper-clad steel wire 30% conductivity', 'Cooper-clad steel rod 20% conductivity', 'Aluminum, EC grade 61% conductivity', 'Aluminum, 5005 alloy 53.5% conductivity', 'Aluminum, 6201 alloy 52.5% conductivity', 'Aluminum-clad steel wire 20.3% conductivity', 'Steel, 1020 10.8% conductivity', 'Stainless-clad steel rod 9.8% conductivity', 'Zinc-coated steel rod 8.6% conductivity', 'Stainless steel, 304 2.4% conductivity']

CondDataProperties = [[0.00393, 234, 1083, 1.72, 3.42, 7], [0.00381, 242, 1084, 1.78, 3.42, 7.06], [0.00378, 245, 1084, 4.4, 3.85, 10.45], [0.00378, 245, 1084, 5.86, 3.85, 12.06], [0.00378, 245, 1084, 8.62, 3.85, 14.64], [0.00403, 228, 657, 2.86, 2.56, 12.12], [0.00353, 263, 652, 3.22, 2.6, 12.41], [0.00347, 268, 654, 3.28, 2.6, 12.47], [0.0036, 258, 657, 8.48, 3.58, 17.2], [0.00316, 605, 1510, 15.9, 3.28, 15.95], [0.0016, 605, 1400, 17.5, 4.44, 14.72], [0.0032, 293, 419, 20.1, 3.93, 28.96], [0.0013, 749, 1400, 72, 4.03, 30.05]]


ExistingData = tkinter.LabelFrame(Frame1, text = 'Existing network data', padx = 20, pady = 20)

ExistingData.grid(row = 0, column = 0, padx = 5, pady = 0)

MaxFaultClTime = tkinter.Label(ExistingData, text = 'Maximum Fault Clearance Time in seconds: ').grid(row = 0, column = 0)

MFCT = tkinter.StringVar()

M_F_C_T = tkinter.Entry(ExistingData, textvariable = MFCT).grid(row = 0, column = 1)

GroundRes = tkinter.Label(ExistingData, text = 'Ground Resistivity in Ohm-meter: ').grid(row = 1, column = 0)

GR = tkinter.StringVar()

G_R = tkinter.Entry(ExistingData, textvariable = GR).grid(row = 1, column = 1)

AmbTemp = tkinter.Label(ExistingData, text = 'Ambient Temperature in °C: ').grid(row = 2, column = 0)

AT = tkinter.StringVar()

A_T = tkinter.Entry(ExistingData, textvariable = AT).grid(row = 2, column = 1)

MaxFaultCurr = tkinter.Label(ExistingData, text = 'Maximum Fault Current in Kiloamps: ').grid(row = 3, column = 0)

MFC = tkinter.StringVar()

M_F_C = tkinter.Entry(ExistingData, textvariable = MFC).grid(row = 3, column = 1)

MaxFaultCurrGPR = tkinter.Label(ExistingData, text = 'Maximum Fault Current that contributes to the Ground Potential Rise in Kiloamps: ').grid(row = 4, column = 0)

MFCGPR = tkinter.StringVar()

M_F_C_GPR = tkinter.Entry(ExistingData, textvariable = MFCGPR).grid(row = 4, column = 1)

XtoR_ratio_MFC = tkinter.Label(ExistingData, text = 'X (reactance) to R (resistance) ratio for the Maximum Fault Current: ').grid(row = 5, column = 0)

XRMFC = tkinter.StringVar()

X_R_MFC = tkinter.Entry(ExistingData, textvariable = XRMFC).grid(row = 5, column = 1)

XtoR_ratio_GPR = tkinter.Label(ExistingData, text = 'X (reactance) to R (resistance) ratio for the Maximum Fault Current that contributes to the Ground Potential Rise: ').grid(row = 6, column = 0)

XRGPR = tkinter.StringVar()

X_R_GPR = tkinter.Entry(ExistingData, textvariable = XRGPR).grid(row = 6, column = 1)

fnomSys = tkinter.Label(ExistingData, text = 'Nominal frecuence of the System (50Hz or 60Hz) in Hz: ').grid(row = 7, column = 0)

FNOM = tkinter.StringVar()

f_nom = tkinter.Entry(ExistingData, textvariable = FNOM).grid(row = 7, column = 1)

SplitFactor = tkinter.Label(ExistingData, text = 'Insert the Current Division Factor: ').grid(row = 8, column = 0)

Sf = tkinter.StringVar()

SplFact = tkinter.Entry(ExistingData, textvariable = Sf).grid(row = 8, column = 1)


DesignData = tkinter.LabelFrame(Frame1, text = 'Design Data', padx = 20, pady = 20)

DesignData.grid(row = 0, column = 1, padx = 5, pady = 10)

ResOfCrushedRock = tkinter.Label(DesignData, text = 'Resistivity of Crushed Rock in Ohm-meter: ').grid(row = 0, column = 0)

RCR = tkinter.StringVar()

R_C_R = tkinter.Entry(DesignData, textvariable = RCR).grid(row = 0, column = 1)

ThickOfCrushRockLayer = tkinter.Label(DesignData, text = 'Thickness Of Crushed Rock Layer in meters: ').grid(row = 1, column = 0)

TCRL = tkinter.StringVar()

T_C_R_L = tkinter.Entry(DesignData, textvariable = TCRL).grid(row = 1, column = 1)

MeBurDep = tkinter.Label(DesignData, text = 'Mesh Burial Depth in meters: ').grid(row = 2, column = 0)

MBD = tkinter.StringVar()

M_B_D = tkinter.Entry(DesignData, textvariable = MBD).grid(row = 2, column = 1)

MeLen = tkinter.Label(DesignData, text = 'Mesh Length in meters: ').grid(row = 3, column = 0)

ML = tkinter.StringVar()

M_L = tkinter.Entry(DesignData, textvariable = ML).grid(row = 3, column = 1)

MeWid = tkinter.Label(DesignData, text = 'Mesh Width in meters: ').grid(row = 4, column = 0)

MW = tkinter.StringVar()

M_W = tkinter.Entry(DesignData, textvariable = MW).grid(row = 4, column = 1)

SpacBetwParCond = tkinter.Label(DesignData, text = 'Spacing between parallel conductors in meters: ').grid(row = 5, column = 0)

SBPC = tkinter.StringVar()

S_B_P_C = tkinter.Entry(DesignData, textvariable = SBPC).grid(row = 5, column = 1)

NumbOfRods = tkinter.Label(DesignData, text = 'Number of Rods: ').grid(row = 6, column = 0)

NOR = tkinter.StringVar()

N_O_R = tkinter.Entry(DesignData, textvariable = NOR).grid(row = 6, column = 1)

LenOfRods = tkinter.Label(DesignData, text = 'Length of each Rod: ').grid(row = 7, column = 0)

LOR = tkinter.StringVar()

L_O_R = tkinter.Entry(DesignData, textvariable = LOR).grid(row = 7, column = 1)

CondMat = tkinter.Label(DesignData, text = 'Mesh Conductor Material: ').grid(row = 8, column = 0)

MCM = tkinter.StringVar()

MeCondMat = ttk.Combobox(DesignData, values = TypeOfConductors, textvariable = MCM).grid(row = 8, column = 1, pady = 5)



Results = tkinter.LabelFrame(Frame1, text = 'Results', padx = 20, pady = 20)

Results.grid(row = 1, column = 0, pady = 0)

ConSize = tkinter.Label(Results, text = 'Minimum Conductor Size in KCM (Kilo Circular Mil): ').grid(row = 0, column = 0)

CS = tkinter.StringVar()

C_size = ttk.Entry(Results, state = 'readonly', textvariable = CS).grid(row = 0, column = 1)        

MeshResis = tkinter.Label(Results, text = 'Mesh Resistance in Ohm: ').grid(row = 2, column = 0)

MR = tkinter.StringVar()

M_R = ttk.Entry(Results, state = 'readonly', textvariable = MR).grid(row = 2, column = 1)

GrPotRise = tkinter.Label(Results, text = 'Ground Potential Rise (GPR) in volts: ').grid(row = 3, column = 0)

GrPoRi = tkinter.StringVar()

G_P_R = ttk.Entry(Results, state = 'readonly', textvariable = GrPoRi).grid(row = 3, column = 1)

AlloTouVol = tkinter.Label(Results, text = 'Allowable Touch voltage for 50Kg person in volts: ').grid(row = 4, column = 0)

ATV = tkinter.StringVar()

A_T_V = ttk.Entry(Results, state = 'readonly', textvariable = ATV).grid(row = 4, column = 1)

AlloStepVol = tkinter.Label(Results, text = 'Allowable Step voltage for 50Kg person in volts: ').grid(row = 5, column = 0)

ASV = tkinter.StringVar()

A_S_V = ttk.Entry(Results, state = 'readonly', textvariable = ASV).grid(row = 5, column = 1)

MaxMesVol = tkinter.Label(Results, text = 'Maximum Mesh voltage "Em" in volts: ').grid(row = 6, column = 0)

MMV = tkinter.StringVar()

M_M_V = ttk.Entry(Results, state = 'readonly', textvariable = MMV).grid(row = 6, column = 1)

MaxStepVol = tkinter.Label(Results, text = 'Maximum Step voltage "Es" in volts: ').grid(row = 7, column = 0)

MSV = tkinter.StringVar()

M_S_V = ttk.Entry(Results, state = 'readonly', textvariable = MSV).grid(row = 7, column = 1)


Vdic = tkinter.StringVar()

Verdict = ttk.Entry(Frame1, state = 'readonly', textvariable = Vdic, width = 70).grid(row = 2, column = 1)

# IEEE80 functionality *************************************************************************************


def IEEE80() :

    if float(NOR.get()) == 0 :

        LOR.set('0')

        L_O_R = tkinter.Entry(DesignData, textvariable = LOR, state = 'readonly').grid(row = 7, column = 1)



    # Mesh conductor size in KCM (Kilo circular mil)

    Ta_MF = float(XRMFC.get()) / (2 * pi * float(FNOM.get()))

    Ta_MFGPR = float(XRGPR.get()) / (2 * pi * float(FNOM.get()))


    def DecrementFactor(Ta, MaximumFaultClearanceTime) :

        Df = (1 + (Ta/MaximumFaultClearanceTime) * (1 - e ** - ((2 * MaximumFaultClearanceTime) / Ta))) ** 0.5

        return Df


    I_conductor = DecrementFactor(Ta_MF, float(MFCT.get())) * float(MFC.get())

    TCAP = CondDataProperties[TypeOfConductors.index(MCM.get())][4] 

    alpha_r = CondDataProperties[TypeOfConductors.index(MCM.get())][0] 

    rho_r = CondDataProperties[TypeOfConductors.index(MCM.get())][3] 

    Ko = CondDataProperties[TypeOfConductors.index(MCM.get())][1]

    Tm = CondDataProperties[TypeOfConductors.index(MCM.get())][2] 

    A_KCM = I_conductor * (197.4 / (((TCAP / (float(MFCT.get()) * alpha_r * rho_r)) * (log((Ko + Tm) / (Ko + float(AT.get()))))) ** 0.5))

    if A_KCM < 133.1 :

        A_KCM = 133.1 




    # Allowable Touch and step tension criteria

    Cs = 1 - ((0.09 * (1 - (float(GR.get()) / float(RCR.get())))) / (2 * float(TCRL.get()) + 0.09)) # corrective factor to compute the effective foot resistance in the presence of a finite thickness of surface material

    Es_50Kg = (1000 + 6 * Cs * float(RCR.get())) * (0.116 / (float(MFCT.get()) ** 0.5)) # Allowable step voltage for a 50 Kg person

    Et_50Kg = (1000 + 1.5 * Cs * float(RCR.get())) * (0.116 / (float(MFCT.get()) ** 0.5)) # Allowable touch voltage for a 50 Kg person


    MeshArea = float(ML.get()) * float(MW.get())

    # Mesh Resistance with Sverak formulation

    Lt = float(NOR.get()) * float(LOR.get()) + float(ML.get()) * (1 + (float(MW.get()) / float(SBPC.get()))) + float(MW.get()) * (1 + (float(ML.get()) / float(SBPC.get()))) # Total length of conductors and rods

    Rg = float(GR.get()) * ((1 / Lt) + (1 / ((20 * MeshArea) ** 0.5)) * (1 + (1 / (1 + float(MBD.get()) * ((20 / MeshArea) ** 0.5)))))

    I_mesh = DecrementFactor(Ta_MFGPR, float(MFCT.get())) * float(Sf.get()) * float(MFCGPR.get()) 

    GPR = I_mesh * Rg * 1000

    d_conductor = 0.000254 * ((10 * A_KCM) ** 0.5)

    Lx = float(ML.get()) # maximum length of the grid in the x direction in m

    Ly = float(MW.get()) # maximum length of the grid in the y direction in m

    Dm = ((Lx ** 2) + (Ly ** 2)) ** 0.5 # maximum distance between any two points on the grid in m

    na = (2 * (float(ML.get()) * (1 + (float(MW.get()) / float(SBPC.get()))) + float(MW.get()) * (1 + (float(ML.get()) / float(SBPC.get()))))) / (2 * (float(ML.get()) + float(MW.get())))

    nb = ((2 * (float(ML.get()) + float(MW.get()))) / (4 * (MeshArea ** 0.5))) ** 0.5

    nc = ((Lx * Ly) / MeshArea) ** ((0.7 * MeshArea) / (Lx * Ly))

    nd = Dm / (((Lx ** 2) + (Ly ** 2)) ** 0.5)

    n = na * nb * nc * nd

    h0 = 1 # grid reference depth

    Kh = (1 + (float(MBD.get()) / h0)) ** 0.5

    Kii = 1 / ((2 * n) ** (2 / n))

    Km = (1 / (2 * pi)) * (log(((float(SBPC.get()) ** 2) / (16 * float(MBD.get()) * d_conductor)) + (((float(SBPC.get()) + 2 * float(MBD.get())) ** 2) / (8 * float(SBPC.get()) * d_conductor)) - (float(MBD.get()) / (4 * d_conductor))) + (Kii / Kh) * (log(8 / (pi * (2 * n - 1)))))

    Ki = 0.644 + 0.148 * n

    Ls = 0.75 * (float(ML.get()) * (1 + (float(MW.get()) / float(SBPC.get()))) + float(MW.get()) * (1 + (float(ML.get()) / float(SBPC.get())))) + 0.85 * (float(NOR.get()) * float(LOR.get()))

    Ks = (1 / pi) * ((1 / (2 * float(MBD.get()))) + (1 / (float(SBPC.get()) + float(MBD.get()))) + ((1 / float(SBPC.get())) * (1 - (0.5 ** (n - 2)))))


    if NOR.get() == 0 :

        Lm = Lt

    else :

        Lm = float(ML.get()) * (1 + (float(MW.get()) / float(SBPC.get()))) + float(MW.get()) * (1 + (float(ML.get()) / float(SBPC.get()))) + (1.55 + 1.22 * (float(LOR.get()) / (((Lx ** 2) + (Ly ** 2)) ** 0.5))) * (float(NOR.get()) * float(LOR.get()))



    E_mesh = (float(GR.get()) * I_mesh * 1000 * Km * Ki) / Lm


    Es_mesh = (float(GR.get()) * Ks * Ki * I_mesh * 1000) / Ls


    CS.set(A_KCM)

    MR.set(Rg)

    GrPoRi.set(GPR)

    ATV.set(Et_50Kg)

    ASV.set(Es_50Kg)

    MMV.set(E_mesh)

    MSV.set(Es_mesh)


    if GPR < Et_50Kg :

        
        Vdic.set('Design meets standard, GPR < Et_50Kg')


    elif E_mesh < Et_50Kg and Es_mesh < Es_50Kg :


        Vdic.set('Design meets standard, E_mesh < Et_50kg and Es_mesh < Es_50kg')


    else : 


        Vdic.set('Modify Design to meet standard')    


    L_O_R = tkinter.Entry(DesignData, textvariable = LOR).grid(row = 7, column = 1)   



Calc = tkinter.Button(Frame1, text = 'Calculate', command = IEEE80).grid(row = 1, column = 1)


Root.mainloop()