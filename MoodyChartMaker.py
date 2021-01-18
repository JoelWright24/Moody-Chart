import math
import matplotlib.pyplot as plt
import numpy as np

def colebrook(FrictionFactor, ReynoldsNumber, RelativeRoughoughness):
    #Here is the colebrook equation: 
    ColbrookFunction = (FrictionFactor**-0.5)+2*math.log10 ((2.51/(ReynoldsNumber*(FrictionFactor**0.5)))+(RelativeRoughoughness/3.72))        
    return ColbrookFunction

def colebrook_derivative(FrictionFactor, ReynoldsNumber, RelativeRoughoughness):
    #Here is the derivative of the colebrook equation:
    ConstantA=2.51/ReynoldsNumber
    ConstantB=RelativeRoughoughness/3.72
    ColbrookDerivativeFuction = -0.5*(FrictionFactor**-1.5)-(1/(2*math.log10 ((FrictionFactor+(ConstantB/(ConstantA*FrictionFactor**-1.5))))))
    return ColbrookDerivativeFuction
#Newton function performs the Newton-Raphson Algorithm using the Colbrook and the Colbrook-derivate fuctions,
# to provide a root. See readme.md for more details.  
def newton(Current_x, ReynoldsNumber, RelativeRoughoughness, maxiter, tol):
    counter=0
    ReynoldsNumberynolds=ReynoldsNumber
    #write a loop that compare Next_x Current_x and the tolerence.
    ColeblookFuction=colebrook(Current_x, ReynoldsNumberynolds, RelativeRoughoughness)
    ColbrookDerivativeFuction=colebrook_derivative(Current_x, ReynoldsNumberynolds, RelativeRoughoughness)
    Next_x= Current_x - (ColeblookFuction/ColbrookDerivativeFuction)
    counter = counter+1
    difference=abs(Next_x-Current_x)
    Current_x=Next_x
    while (difference>tol):
        ColeblookFuction=colebrook(Current_x, ReynoldsNumberynolds, RelativeRoughoughness)
        ColbrookDerivativeFuction=colebrook_derivative(Current_x, ReynoldsNumberynolds, RelativeRoughoughness)
        Next_x= Current_x - (ColeblookFuction/ColbrookDerivativeFuction)
        counter = counter+1
        difference=abs(Next_x-Current_x)
        Current_x=Next_x
        if (counter>maxiter):
            break
    return (Next_x)

#Moody fuction is used to plot a Moody Chart and the user may input data
# from a text file or manually: 
def moody ():
    ###
    #Producing the Moody Chart:
    print("Welcome to the Moody Script. Here you can print a Moody Chart and add your data points.")
    
    NumberOfPoints = 500
    Spacing_Array=np.linspace(math.log10(2040), 8, NumberOfPoints)
    ReynoldsNumberynolds_Array=np.zeros((NumberOfPoints))
    for i in range (NumberOfPoints):
        ReynoldsNumberynolds_Array[i]= 10**Spacing_Array[i]
    ##This concludes the Generating of the Reynolds Numbers Array

    #Relative Roughnesses
    TheRelativeRoughnesses=((0, 10**-2, 10**-3, 10**-4, 10**-5, 10**-6))
    #Now I need to put the numbers through the Newton Function
    Initial_Guess=0.01
    ## Now start producing the Arrays of data for turbulent flow. 
    Friction_Factors_Array=np.zeros((NumberOfPoints, len(TheRelativeRoughnesses)))
    for ii in range (len(TheRelativeRoughnesses)):
        for jj in range (NumberOfPoints):
            
            Friction_Factors_Array[(jj,ii)]=newton(Initial_Guess, ReynoldsNumberynolds_Array[jj], TheRelativeRoughnesses[ii], 1000, 10**-9)

    #Produce the straight line between ReynoldsNumber 500 and ReynoldsNumber2500
    Laminar_Spacing_Array=np.linspace(500, 2500, NumberOfPoints)  
    fD_Laminar=64/Laminar_Spacing_Array

    ### Now to plot ### 
    plt.figure(1)   
    # Setting a logarithmic scale for y-axis
    plt.title('Moody diagram for Lamina/turbulent pipe flow')
    plt.xlabel('Reynolds Number')
    plt.ylabel('Friction Factor fD')
    plt.yscale('log')
    plt.xscale('log')
    plt.xlim((500,1e8))
    plt.ylim((5e-3,2e-1))
    plt.plot(Laminar_Spacing_Array,fD_Laminar, color="blue", label='Laminarr')
    plt.plot(ReynoldsNumberynolds_Array, Friction_Factors_Array[:,0],color="orange", label='Smooth')
    plt.plot(ReynoldsNumberynolds_Array, Friction_Factors_Array[:,5], color="green", label='$\epsilon$/D = $10^{-6}$')
    plt.plot(ReynoldsNumberynolds_Array, Friction_Factors_Array[:,4], color="red", label='$\epsilon$/D = $10^{-5}$')
    plt.plot(ReynoldsNumberynolds_Array, Friction_Factors_Array[:,3], color="purple", label='$\epsilon$/D = $10^{-4}$')
    plt.plot(ReynoldsNumberynolds_Array, Friction_Factors_Array[:,2], color="brown", label='$\epsilon$/D = $10^{-3}$')
    plt.plot(ReynoldsNumberynolds_Array, Friction_Factors_Array[:,1], color="magenta", label='$\epsilon$/D = $10^{-2}$')
    plt.grid(b=None, which='major', axis='both')
    plt.grid(b=True, which='minor', axis='both', ls='dashed')
    plt.vlines(2040, 0.001, 0.5, colors='r', linestyles='dashed',label='Turbulence transition')
    ###
    #points can also be made into an input option
    #file name is name to be saved - this can be editied 
    
    ProceedWithPlot="Loading"
    while (ProceedWithPlot=="Loading"):

        print("Spicific data points can be posted on the graph from a text file or data you can eneter in the terminal.")
        print("For the data to be read, it needs to be written in a specific format. The infomation in each row needs to be as follows: \n"
        "The pipe diameter D [m], fluid velocity U [ms−1], fluid density ρ [kgm−3], fluid dynamic viscosity µ [Pas], pipe absolute roughness Ɛ [mm]")
        YesOrNo = input("Would you like to plot points from a text file? [y/n]: ")
        if (YesOrNo=="y"):
            print("What is the name of the text file saved in this the current directory?")
            
            FileName = str(input("Please enter the file name including the file extenstion (e.g. inputs.txt): "))        
            from os import listdir
            onlyfiles = listdir()
            NumberOfFiles=len(onlyfiles)
            counter=0
            for i in range (NumberOfFiles):
                
                if (onlyfiles[i]==FileName):
                    ProceedWithPlot="Yes"
                    break
                    
                else:
                    counter=counter+1
                    
                if (counter==NumberOfFiles):

                    print("A valid filename is required. Please Try again...")
                    print("Alternativly enter [n] to Exit")
            
        else:
            ProceedWithPlot="No"
            break
            
    if (ProceedWithPlot=="Yes"):    
        openFile=np.genfromtxt(FileName, dtype=float)
        
        # Initialize the required arrays:
        ReynoldsNumbersFromFile=np.zeros(len(openFile))
        RelativeRoughnessNumbers=np.zeros(len(openFile))
        Friction_Factors=np.zeros(len(openFile))
        Pressurer_Loss=np.zeros(len(openFile))
        Pressure_Loss_Array=np.zeros((len(openFile),2))
        PointsListFromFile=np.zeros((len(openFile),2))

        #Need to generate the ReynoldsNumbery and Relative Roughness. 
        # Re= rho*U*D/mu
        # Relative Roughness = Esp/D 
        for kk in range (len(openFile)):
            ReynoldsNumbersFromFile[kk]= openFile[kk,0]*openFile[kk,1]*openFile[kk,2]/openFile[kk,3]
            RelativeRoughnessNumbers[kk]=(openFile[kk,4]/1000)/openFile[kk,0]
            #Now plug this into darcy to get fd
            Friction_Factors[kk]=newton(0.01, ReynoldsNumbersFromFile[kk], RelativeRoughnessNumbers[kk], 1000, 10**-9)
            #Write Pressure Loss Equation
            Pressurer_Loss[kk]=0.5*Friction_Factors[kk]*openFile[kk,2]*openFile[kk,1]*openFile[kk,1]/openFile[kk,0]
            #Write Friction Factor and Pressure Loss into new array 
            Pressure_Loss_Array[kk,0]=Friction_Factors[kk]
            Pressure_Loss_Array[kk,1]=Pressurer_Loss[kk]
            #write the points list:
            PointsListFromFile[kk,0]=ReynoldsNumbersFromFile[kk]
            PointsListFromFile[kk,1]=Friction_Factors[kk]
        
        #Finally plot the points using plt.scatter: 
        plt.scatter(PointsListFromFile[:,0], PointsListFromFile[:,1], marker='x' ,color="black", label="Supplied points from file")

    #Plot the file values from a list of supplied points:
    PointsYesOrNo=input("Do you want to print a list of user input points? [y/n] ")
    if (PointsYesOrNo=="y"):
        ReynoldsPoints=[]
        FrictionFactorPoints=[]
        print("Please enter the coordinates of the points")
        #Enter Reynolds Number: 
        while True:
                try:
                    RePoint=float(input("Please enter the Reynolds Number between 500 and 1e+08: "))#Between 500 and 10^8 
                    if (500<RePoint<1e8):
                        break
                    else:
                        print("Please give a Reynolds Number in the range of 500 and 1e8...")
                        ValueError
                except ValueError:
                    print("A valid Reynolds Number between 500 and 1e8 required. Please Try again...")
        # Enter Friction Factor:
        while True:
                try:
                    FFpoint=float(input("Enter is the Friction Factor between 5e-3 and 2e-1: "))#Between 0.005 and 0.2 
                    if (0.005<FFpoint<0.2):
                        break
                    else:
                        print("Please give a Friction Factor in the range of 5e-3 and 2e-1...")
                        ValueError
                except ValueError:
                    print("A valid Friction Factor between 5e-3 and 2e-1 required. Please Try again...")

        ReynoldsPoints.append(RePoint)
        FrictionFactorPoints.append(FFpoint)
        KeepEnteringPoints=(input("Would you like to add another point to the graph? [y/n]"))
        while (KeepEnteringPoints=="y"):
            #Enter Reynolds Number: 
            while True:
                    try:
                        RePoint=float(input("Please enter the Reynolds Number between 500 and 1e+08: "))#Between 500 and 10^8 
                        if (500<RePoint<1e8):
                            break
                        else:
                            print("Please give a Reynolds Number in the range of 500 and 1e8...")
                            ValueError
                    except ValueError:
                        print("A valid Reynolds Number between 500 and 1e8 required. Please Try again...")
            # Enter Friction Factor:
            while True:
                    try:
                        FFpoint=float(input("Enter is the Friction Factor between 5e-3 and 2e-1: "))#Between 0.005 and 0.2 
                        if (0.005<FFpoint<0.2):
                            break
                        else:
                            print("Please give a Friction Factor in the range of 5e-3 and 2e-1...")
                            ValueError
                    except ValueError:
                        print("A valid Friction Factor between 5e-3 and 2e-1 required. Please Try again...")
            ReynoldsPoints.append(RePoint)
            FrictionFactorPoints.append(FFpoint)
            KeepEnteringPoints=(input("Would you like to add another point to the graph? [y/n] "))
        
        #Finally plot the points using plt.scatter:
        plt.scatter(ReynoldsPoints,FrictionFactorPoints, marker='x' ,color="blue", label="User supplied points")
        
        
    # finish the plotting off outside of the if statment to ignore plotting points if not required.    
    # Set the legend in the bottom left hand corner
    plt.legend(loc=3)
    SaveYesOrNo=input("Would you like to save the graph? [y/n]")
    if (SaveYesOrNo=="y"):
        newFileName=input("Please enter the name the file: ")
        FileExtention=".pdf"
        FullFileName=newFileName+FileExtention
        plt.savefig(FullFileName, dpi=300, bbox_inches='tight')
 
    plt.show()
    return ()
Solution=moody()