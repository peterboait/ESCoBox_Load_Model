'''
Created on 18 March 2015
Copyright De Montfort University
@author: Peter Boait
'''
import monte_carlo

import Tkinter
import tkFont
from PIL import ImageTk
import tkFileDialog


class escobox_model_tk (Tkinter.Tk):
    """This class creates the model GUI then a button press calls the monte carlo model using the data entered."""
   
    def __init__(self,parent):
            Tkinter.Tk.__init__(self,parent)
            self.parent = parent
            self.customFont=tkFont.Font(family="Helvetica", size=12)
            self.customFontB=tkFont.Font(family="Helvetica", size=12, weight=tkFont.BOLD)            
            self.initialize() 
       
    def initialize(self):
        """Creates the GUI screen"""
        
        self.grid()
        
        #Logo label and row
        logo=ImageTk.PhotoImage(file="ESCoBox_Logo.gif")
        ImageLabel0=Tkinter.Label(self,image=logo)
        ImageLabel0.image=logo
        ImageLabel0.grid(column=0,row=1,sticky='EW') 
        
        LogoLabel1=Tkinter.Label(self,text="MINI- & MICRO- GRID  LOAD",anchor="w",fg="black",bg="white",font=self.customFontB)
        LogoLabel1.grid(column=1,row=1,sticky='EW')
        
        LogoLabel2=Tkinter.Label(self,text="MODEL",anchor="w",fg="black",bg="white",font=self.customFontB)
        LogoLabel2.grid(column=2,row=1,sticky='EW')      
        
                
        #Header labels
        HeaderLabel1=Tkinter.Label(self,text="Appliance type",anchor="w",fg="black",bg="white",font=self.customFontB)
        HeaderLabel1.grid(column=0,row=3,sticky='EW')  
        
        HeaderLabel2=Tkinter.Label(self,text="No. of appliances",anchor="w",fg="black",bg="white",font=self.customFontB)
        HeaderLabel2.grid(column=1,row=3,sticky='EW')  
        
        HeaderLabel3=Tkinter.Label(self,text="Power used (kW)",anchor="w",fg="black",bg="white",font=self.customFontB)
        HeaderLabel3.grid(column=2,row=3,sticky='EW')  
        
        HeaderLabel4=Tkinter.Label(self,text="Duty cycle (probability of use)",anchor="w",fg="black",bg="white",font=self.customFontB)
        HeaderLabel4.grid(column=3,row=3,sticky='EW')  
        
                
        #Now we have a proper data entry row
        applianceLabel1=Tkinter.Label(self,text="Light - incandescent",anchor="w",fg="black",bg="white",font=self.customFont)
        applianceLabel1.grid(column=0,row=5,sticky='EW')
             
        self.enteredNumberAppliance1=Tkinter.IntVar()
        self.appliance1NumberField = Tkinter.Entry(self,textvariable=self.enteredNumberAppliance1,font=self.customFont)
        self.appliance1NumberField.grid(column=1,row=5,sticky='EW')
        
        self.enteredPowerAppliance1=Tkinter.DoubleVar()
        self.enteredPowerAppliance1.set(0.04) #default power level
        self.appliance1PowerField = Tkinter.Entry(self,textvariable=self.enteredPowerAppliance1,font=self.customFont)
        self.appliance1PowerField.grid(column=2,row=5,sticky='EW')
             
        self.dropdown_variable1=Tkinter.DoubleVar()
        self.dropdown_variable1.set("0.1")
        self.dropdown1=Tkinter.OptionMenu(self,self.dropdown_variable1,"0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0")
        self.dropdown1.grid(column=3,row=5)
               
        #Second data entry row
        applianceLabel2=Tkinter.Label(self,text="Light - CFL",anchor="w",fg="black",bg="white",font=self.customFont)
        applianceLabel2.grid(column=0,row=6,sticky='EW')
             
        self.enteredNumberAppliance2=Tkinter.IntVar()
        self.appliance2NumberField = Tkinter.Entry(self,textvariable=self.enteredNumberAppliance2,font=self.customFont)
        self.appliance2NumberField.grid(column=1,row=6,sticky='EW')
        
        self.enteredPowerAppliance2=Tkinter.DoubleVar()
        self.enteredPowerAppliance2.set(0.012) #default power level
        self.appliance2PowerField = Tkinter.Entry(self,textvariable=self.enteredPowerAppliance2,font=self.customFont)
        self.appliance2PowerField.grid(column=2,row=6,sticky='EW')
             
        self.dropdown_variable2=Tkinter.DoubleVar()
        self.dropdown_variable2.set("0.1")
        self.dropdown2=Tkinter.OptionMenu(self,self.dropdown_variable2,"0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0")
        self.dropdown2.grid(column=3,row=6)
        
        #Third data entry row
        applianceLabel3=Tkinter.Label(self,text="Light-LED",anchor="w",fg="black",bg="white",font=self.customFont)
        applianceLabel3.grid(column=0,row=7,sticky='EW')
 
        self.enteredNumberAppliance3=Tkinter.IntVar()
        self.appliance3NumberField = Tkinter.Entry(self,textvariable=self.enteredNumberAppliance3,font=self.customFont)
        self.appliance3NumberField.grid(column=1,row=7,sticky='EW')
        
        self.enteredPowerAppliance3=Tkinter.DoubleVar()
        self.enteredPowerAppliance3.set(0.005) #default power level
        self.appliance3PowerField = Tkinter.Entry(self,textvariable=self.enteredPowerAppliance3,font=self.customFont)
        self.appliance3PowerField.grid(column=2,row=7,sticky='EW')
             
        self.dropdown_variable3=Tkinter.DoubleVar()
        self.dropdown_variable3.set("0.1")
        self.dropdown3=Tkinter.OptionMenu(self,self.dropdown_variable3,"0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0")
        self.dropdown3.grid(column=3,row=7)
        
        #Fourth data entry row
        applianceLabel4=Tkinter.Label(self,text="Phone charger",anchor="w",fg="black",bg="white",font=self.customFont)
        applianceLabel4.grid(column=0,row=8,sticky='EW')
             
        self.enteredNumberAppliance4=Tkinter.IntVar()
        self.appliance4NumberField = Tkinter.Entry(self,textvariable=self.enteredNumberAppliance4,font=self.customFont)
        self.appliance4NumberField.grid(column=1,row=8,sticky='EW')
        
        self.enteredPowerAppliance4=Tkinter.DoubleVar()
        self.enteredPowerAppliance4.set(0.005) #default power level
        self.appliance4PowerField = Tkinter.Entry(self,textvariable=self.enteredPowerAppliance4,font=self.customFont)
        self.appliance4PowerField.grid(column=2,row=8,sticky='EW')
             
        self.dropdown_variable4=Tkinter.DoubleVar()
        self.dropdown_variable4.set("0.1")
        self.dropdown4=Tkinter.OptionMenu(self,self.dropdown_variable4,"0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0")
        self.dropdown4.grid(column=3,row=8)

        #Fifth data entry row
        applianceLabel5=Tkinter.Label(self,text="Television-LCD",anchor="w",fg="black",bg="white",font=self.customFont)
        applianceLabel5.grid(column=0,row=9,sticky='EW')
             
        self.enteredNumberAppliance5=Tkinter.IntVar()
        self.appliance5NumberField = Tkinter.Entry(self,textvariable=self.enteredNumberAppliance5,font=self.customFont)
        self.appliance5NumberField.grid(column=1,row=9,sticky='EW')
        
        self.enteredPowerAppliance5=Tkinter.DoubleVar()
        self.enteredPowerAppliance5.set(0.05) #default power level
        self.appliance5PowerField = Tkinter.Entry(self,textvariable=self.enteredPowerAppliance5,font=self.customFont)
        self.appliance5PowerField.grid(column=2,row=9,sticky='EW')
             
        self.dropdown_variable5=Tkinter.DoubleVar()
        self.dropdown_variable5.set("0.1")
        self.dropdown5=Tkinter.OptionMenu(self,self.dropdown_variable5,"0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0")
        self.dropdown5.grid(column=3,row=9)

        #Sixth data entry row
        applianceLabel6=Tkinter.Label(self,text="Ceiling fan",anchor="w",fg="black",bg="white",font=self.customFont)
        applianceLabel6.grid(column=0,row=10,sticky='EW')
             
        self.enteredNumberAppliance6=Tkinter.IntVar()
        self.appliance6NumberField = Tkinter.Entry(self,textvariable=self.enteredNumberAppliance6,font=self.customFont)
        self.appliance6NumberField.grid(column=1,row=10,sticky='EW')
        
        self.enteredPowerAppliance6=Tkinter.DoubleVar()
        self.enteredPowerAppliance6.set(0.15) #default power level
        self.appliance6PowerField = Tkinter.Entry(self,textvariable=self.enteredPowerAppliance6,font=self.customFont)
        self.appliance6PowerField.grid(column=2,row=10,sticky='EW')
             
        self.dropdown_variable6=Tkinter.DoubleVar()
        self.dropdown_variable6.set("0.1")
        self.dropdown6=Tkinter.OptionMenu(self,self.dropdown_variable6,"0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0")
        self.dropdown6.grid(column=3,row=10)

        #Seventh data entry row
        applianceLabel7=Tkinter.Label(self,text="Refrigerator",anchor="w",fg="black",bg="white",font=self.customFont)
        applianceLabel7.grid(column=0,row=11,sticky='EW')
             
        self.enteredNumberAppliance7=Tkinter.IntVar()
        self.appliance7NumberField = Tkinter.Entry(self,textvariable=self.enteredNumberAppliance7,font=self.customFont)
        self.appliance7NumberField.grid(column=1,row=11,sticky='EW')
        
        self.enteredPowerAppliance7=Tkinter.DoubleVar()
        self.enteredPowerAppliance7.set(0.0) #default power level
        self.appliance7PowerField = Tkinter.Entry(self,textvariable=self.enteredPowerAppliance7,font=self.customFont)
        self.appliance7PowerField.grid(column=2,row=11,sticky='EW')
             
        self.dropdown_variable7=Tkinter.DoubleVar()
        self.dropdown_variable7.set("0.1")
        self.dropdown7=Tkinter.OptionMenu(self,self.dropdown_variable7,"0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0")
        self.dropdown7.grid(column=3,row=11)
        
        #Eighth data entry row
        applianceLabel8=Tkinter.Label(self,text="Other Appliance",anchor="w",fg="black",bg="white",font=self.customFont)
        applianceLabel8.grid(column=0,row=12,sticky='EW')
             
        self.enteredNumberAppliance8=Tkinter.IntVar()
        self.appliance8NumberField = Tkinter.Entry(self,textvariable=self.enteredNumberAppliance8,font=self.customFont)
        self.appliance8NumberField.grid(column=1,row=12,sticky='EW')
        
        self.enteredPowerAppliance8=Tkinter.DoubleVar()
        self.enteredPowerAppliance8.set(0.0) #default power level
        self.appliance8PowerField = Tkinter.Entry(self,textvariable=self.enteredPowerAppliance8,font=self.customFont)
        self.appliance8PowerField.grid(column=2,row=12,sticky='EW')
             
        self.dropdown_variable8=Tkinter.DoubleVar()
        self.dropdown_variable8.set("0.1")
        self.dropdown8=Tkinter.OptionMenu(self,self.dropdown_variable8,"0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0")
        self.dropdown8.grid(column=3,row=12)
        
        #Ninth data entry row
        applianceLabel9=Tkinter.Label(self,text="Other Appliance",anchor="w",fg="black",bg="white",font=self.customFont)
        applianceLabel9.grid(column=0,row=13,sticky='EW')
             
        self.enteredNumberAppliance9=Tkinter.IntVar()
        self.appliance9NumberField = Tkinter.Entry(self,textvariable=self.enteredNumberAppliance9,font=self.customFont)
        self.appliance9NumberField.grid(column=1,row=13,sticky='EW')
        
        self.enteredPowerAppliance9=Tkinter.DoubleVar()
        self.enteredPowerAppliance9.set(0.0) #default power level
        self.appliance9PowerField = Tkinter.Entry(self,textvariable=self.enteredPowerAppliance9,font=self.customFont)
        self.appliance9PowerField.grid(column=2,row=13,sticky='EW')
             
        self.dropdown_variable9=Tkinter.DoubleVar()
        self.dropdown_variable9.set("0.1")
        self.dropdown9=Tkinter.OptionMenu(self,self.dropdown_variable9,"0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0")
        self.dropdown9.grid(column=3,row=13)
        
        #Run model row
        button_run=Tkinter.Button(self,text="Run model-month",command=self.call_model_month,font=self.customFontB)
        button_run.grid(column=0,row=14)
        
        button_run=Tkinter.Button(self,text="Run model-year",command=self.call_model_year,font=self.customFontB)
        button_run.grid(column=1,row=14)
        
        button_run=Tkinter.Button(self,text="Clear results",command=self.zeroise_results,font=self.customFontB)
        button_run.grid(column=2,row=14)
        
        
        #Results output row for peak power
        Result1Label=Tkinter.Label(self,text="Peak power used = ",anchor="w",fg="black",bg="white",font=self.customFontB)
        Result1Label.grid(column=0,row=15,sticky='EW')  
        
        self.result_total_peak=Tkinter.DoubleVar()
        Result1LabelOutput=Tkinter.Label(self,textvariable=self.result_total_peak,anchor="w",fg="black",bg="white",font=self.customFont)
        Result1LabelOutput.grid(column=1,row=15,sticky='EW')  
        
        KwpLabel=Tkinter.Label(self,text="kW",anchor="w",fg="black",bg="white",font=self.customFontB)
        KwpLabel.grid(column=2,row=15,sticky='EW')  
        
        #Results output row for average power
        Result2Label=Tkinter.Label(self,text="Average power used = ",anchor="w",fg="black",bg="white",font=self.customFontB)
        Result2Label.grid(column=0,row=16,sticky='EW')  
        
        self.result_total_avge=Tkinter.DoubleVar()
        Result2LabelOutput=Tkinter.Label(self,textvariable=self.result_total_avge,anchor="w",fg="black",bg="white",font=self.customFont)
        Result2LabelOutput.grid(column=1,row=16,sticky='EW')  
        
        KwaLabel=Tkinter.Label(self,text="kW",anchor="w",fg="black",bg="white",font=self.customFontB)
        KwaLabel.grid(column=2,row=16,sticky='EW')
        
        #Results output row for standard deviation
        Result2Label=Tkinter.Label(self,text="Standard deviation of power = ",anchor="w",fg="black",bg="white",font=self.customFontB)
        Result2Label.grid(column=0,row=17,sticky='EW')  
        
        self.result_total_sd=Tkinter.DoubleVar()
        Result2LabelOutput=Tkinter.Label(self,textvariable=self.result_total_sd,anchor="w",fg="black",bg="white",font=self.customFont)
        Result2LabelOutput.grid(column=1,row=17,sticky='EW')  
        
        KwaLabel=Tkinter.Label(self,text="% of average power",anchor="w",fg="black",bg="white",font=self.customFontB)
        KwaLabel.grid(column=2,row=17,sticky='EW')
        
        #Save and load model row
        button_save=Tkinter.Button(self,text="Save model",command=self.call_save,font=self.customFontB)
        button_save.grid(column=0,row=18)
        
        button_load=Tkinter.Button(self,text="Open model",command=self.call_open,font=self.customFontB)
        button_load.grid(column=2,row=18)
        
        #Configuration lines
        self.grid_columnconfigure(0,weight=1) #allows window to be resized
        self.resizable(True,True) #limits resizing to horizontal axis
        

    #This method calls the Monte Carlo class        
    def call_model_year(self):
        """Collects the entered data from the screen into array arguments and calls the Monte Carlo method
        
        Run length for a year is an embedded parameter due to tKinter issue with making it an argument""" 
        
        device_popn=[] #Set of arrays to hold model inputs 
        duty_cycles=[]
        power_values=[]   
        length=525600 #corresponds to about a year's running
                
        #Collect variables from appliance 1
        number1=int(self.appliance1NumberField.get()) #gui always returns strings
        power1=float(self.appliance1PowerField.get())
        duty_cycle1=float(self.dropdown_variable1.get()) #gui always returns strings
        device_popn.append(number1)
        duty_cycles.append(duty_cycle1)
        power_values.append(power1)
        
        #Collect variables from appliance 2
        number2=int(self.appliance2NumberField.get()) #gui always returns strings
        power2=float(self.appliance2PowerField.get())
        duty_cycle2=float(self.dropdown_variable2.get()) #gui always returns strings
        device_popn.append(number2)
        duty_cycles.append(duty_cycle2)
        power_values.append(power2)
 
        #Collect variables from appliance 3
        number3=int(self.appliance3NumberField.get()) #gui always returns strings
        power3=float(self.appliance3PowerField.get())
        duty_cycle3=float(self.dropdown_variable3.get()) #gui always returns strings
        device_popn.append(number3)
        duty_cycles.append(duty_cycle3)
        power_values.append(power3)
     
        #Collect variables from appliance 4
        number4=int(self.appliance4NumberField.get()) #gui always returns strings
        power4=float(self.appliance4PowerField.get())
        duty_cycle4=float(self.dropdown_variable4.get()) #gui always returns strings
        device_popn.append(number4)
        duty_cycles.append(duty_cycle4)
        power_values.append(power4)
        
        #Collect variables from appliance 5
        number5=int(self.appliance5NumberField.get()) #gui always returns strings
        power5=float(self.appliance5PowerField.get())
        duty_cycle5=float(self.dropdown_variable5.get()) #gui always returns strings
        device_popn.append(number5)
        duty_cycles.append(duty_cycle5)
        power_values.append(power5)

        #Collect variables from appliance 6
        number6=int(self.appliance6NumberField.get()) #gui always returns strings
        power6=float(self.appliance6PowerField.get())
        duty_cycle6=float(self.dropdown_variable6.get()) #gui always returns strings
        device_popn.append(number6)
        duty_cycles.append(duty_cycle6)
        power_values.append(power6)
       
        #Collect variables from appliance 7
        number7=int(self.appliance7NumberField.get()) #gui always returns strings
        power7=float(self.appliance7PowerField.get())
        duty_cycle7=float(self.dropdown_variable7.get()) #gui always returns strings
        device_popn.append(number7)
        duty_cycles.append(duty_cycle7)
        power_values.append(power7)
        
        #Collect variables from appliance 8
        number8=int(self.appliance8NumberField.get()) #gui always returns strings
        power8=float(self.appliance8PowerField.get())
        duty_cycle8=float(self.dropdown_variable8.get()) #gui always returns strings
        device_popn.append(number8)
        duty_cycles.append(duty_cycle8)
        power_values.append(power8)
        
        #Collect variables from appliance 9
        number9=int(self.appliance9NumberField.get()) #gui always returns strings
        power9=float(self.appliance9PowerField.get())
        duty_cycle9=float(self.dropdown_variable9.get()) #gui always returns strings
        device_popn.append(number9)
        duty_cycles.append(duty_cycle9)
        power_values.append(power9)
        
        #Now run the aggregate model
        agg_model=monte_carlo.MonteCarloAggregate(device_popn,length,duty_cycles,power_values)
        agg_result=agg_model.aggregate_model()
        #print (agg_result)
        
        #Display results
        self.result_total_peak.set(round(agg_result[0],2)) #Run peak
        self.result_total_avge.set(round(agg_result[1],2)) #Run avge
        self.result_total_sd.set(round(agg_result[2],2)) #Run sd as % of average

    def call_model_month(self):
        """Collects the entered data from the screen into array arguments and calls the Monte Carlo method
        
        Run length for a month is an embedded parameter due to tKinter issue with making it an argument""" 
            
        device_popn=[] #Set of arrays to hold model inputs 
        duty_cycles=[]
        power_values=[]   
        length=44640 #corresponds to a month's running
                
        #Collect variables from appliance 1
        number1=int(self.appliance1NumberField.get()) #gui always returns strings
        power1=float(self.appliance1PowerField.get())
        duty_cycle1=float(self.dropdown_variable1.get()) #gui always returns strings
        device_popn.append(number1)
        duty_cycles.append(duty_cycle1)
        power_values.append(power1)
        
        #Collect variables from appliance 2
        number2=int(self.appliance2NumberField.get()) #gui always returns strings
        power2=float(self.appliance2PowerField.get())
        duty_cycle2=float(self.dropdown_variable2.get()) #gui always returns strings
        device_popn.append(number2)
        duty_cycles.append(duty_cycle2)
        power_values.append(power2)
 
        #Collect variables from appliance 3
        number3=int(self.appliance3NumberField.get()) #gui always returns strings
        power3=float(self.appliance3PowerField.get())
        duty_cycle3=float(self.dropdown_variable3.get()) #gui always returns strings
        device_popn.append(number3)
        duty_cycles.append(duty_cycle3)
        power_values.append(power3)
     
        #Collect variables from appliance 4
        number4=int(self.appliance4NumberField.get()) #gui always returns strings
        power4=float(self.appliance4PowerField.get())
        duty_cycle4=float(self.dropdown_variable4.get()) #gui always returns strings
        device_popn.append(number4)
        duty_cycles.append(duty_cycle4)
        power_values.append(power4)
        
        #Collect variables from appliance 5
        number5=int(self.appliance5NumberField.get()) #gui always returns strings
        power5=float(self.appliance5PowerField.get())
        duty_cycle5=float(self.dropdown_variable5.get()) #gui always returns strings
        device_popn.append(number5)
        duty_cycles.append(duty_cycle5)
        power_values.append(power5)

        #Collect variables from appliance 6
        number6=int(self.appliance6NumberField.get()) #gui always returns strings
        power6=float(self.appliance6PowerField.get())
        duty_cycle6=float(self.dropdown_variable6.get()) #gui always returns strings
        device_popn.append(number6)
        duty_cycles.append(duty_cycle6)
        power_values.append(power6)
       
        #Collect variables from appliance 7
        number7=int(self.appliance7NumberField.get()) #gui always returns strings
        power7=float(self.appliance7PowerField.get())
        duty_cycle7=float(self.dropdown_variable7.get()) #gui always returns strings
        device_popn.append(number7)
        duty_cycles.append(duty_cycle7)
        power_values.append(power7)
        
        #Collect variables from appliance 8
        number8=int(self.appliance8NumberField.get()) #gui always returns strings
        power8=float(self.appliance8PowerField.get())
        duty_cycle8=float(self.dropdown_variable8.get()) #gui always returns strings
        device_popn.append(number8)
        duty_cycles.append(duty_cycle8)
        power_values.append(power8)
        
        #Collect variables from appliance 9
        number9=int(self.appliance9NumberField.get()) #gui always returns strings
        power9=float(self.appliance9PowerField.get())
        duty_cycle9=float(self.dropdown_variable9.get()) #gui always returns strings
        device_popn.append(number9)
        duty_cycles.append(duty_cycle9)
        power_values.append(power9)
        
        #Now run the aggregate model
        agg_model=monte_carlo.MonteCarloAggregate(device_popn,length,duty_cycles,power_values)
        agg_result=agg_model.aggregate_model()
        print (agg_result) #to console if open.
        
        #Display results
        self.result_total_peak.set(round(agg_result[0],2)) #Run peak
        self.result_total_avge.set(round(agg_result[1],2)) #Run avge
        self.result_total_sd.set(round(agg_result[2],2)) #Run sd
            
    def call_save(self):
        """Allows all currently entered data in GUI to be saved to a file for reuse"""
        
        appliance_numbers=[] #list to hold all of the entered parameters
        appliance_numbers.append(self.enteredNumberAppliance1.get()) #Add all params in turn to list
        appliance_numbers.append(self.enteredNumberAppliance2.get())
        appliance_numbers.append(self.enteredNumberAppliance3.get())
        appliance_numbers.append(self.enteredNumberAppliance4.get())
        appliance_numbers.append(self.enteredNumberAppliance5.get())
        appliance_numbers.append(self.enteredNumberAppliance6.get())
        appliance_numbers.append(self.enteredNumberAppliance7.get())
        appliance_numbers.append(self.enteredNumberAppliance8.get())
        appliance_numbers.append(self.enteredNumberAppliance9.get())
        
        appliance_numbers.append(self.enteredPowerAppliance1.get())
        appliance_numbers.append(self.enteredPowerAppliance2.get())
        appliance_numbers.append(self.enteredPowerAppliance3.get())
        appliance_numbers.append(self.enteredPowerAppliance4.get())
        appliance_numbers.append(self.enteredPowerAppliance5.get())
        appliance_numbers.append(self.enteredPowerAppliance6.get())
        appliance_numbers.append(self.enteredPowerAppliance7.get())
        appliance_numbers.append(self.enteredPowerAppliance8.get())
        appliance_numbers.append(self.enteredPowerAppliance9.get())
        
        appliance_numbers.append(self.dropdown_variable1.get())
        appliance_numbers.append(self.dropdown_variable2.get())
        appliance_numbers.append(self.dropdown_variable3.get())
        appliance_numbers.append(self.dropdown_variable4.get())
        appliance_numbers.append(self.dropdown_variable5.get())
        appliance_numbers.append(self.dropdown_variable6.get())
        appliance_numbers.append(self.dropdown_variable7.get())
        appliance_numbers.append(self.dropdown_variable8.get())
        appliance_numbers.append(self.dropdown_variable9.get())
        
        appliance_strings=map(str,appliance_numbers)  #create string of appliance parameters    
        
        #save_file=open('model_numbers.emm','w') #simple method of file open
        save_file=tkFileDialog.asksaveasfile(initialdir='\model_inputs')     
     
        for item in appliance_strings:
            save_file.write(item+'\n')
            
        
        return
    
    def call_open(self):
        """Allows data previously entered in the GUI and saved to be used to re-populate the GUI"""
        
        appliance_read=[]
        #load_file=open('model_numbers.emm','r') #simple read
        load_file=tkFileDialog.askopenfile()
        
        for line in load_file:
            appliance_read.append(line) #replicates input strings into list
        
        self.enteredNumberAppliance1.set(int(appliance_read[0]))
        self.enteredNumberAppliance2.set(int(appliance_read[1]))
        self.enteredNumberAppliance3.set(int(appliance_read[2]))
        self.enteredNumberAppliance4.set(int(appliance_read[3]))
        self.enteredNumberAppliance5.set(int(appliance_read[4]))
        self.enteredNumberAppliance6.set(int(appliance_read[5]))
        self.enteredNumberAppliance7.set(int(appliance_read[6]))
        self.enteredNumberAppliance8.set(int(appliance_read[7]))
        self.enteredNumberAppliance9.set(int(appliance_read[8]))
        
        self.enteredPowerAppliance1.set(float(appliance_read[9]))
        self.enteredPowerAppliance2.set(float(appliance_read[10]))
        self.enteredPowerAppliance3.set(float(appliance_read[11]))
        self.enteredPowerAppliance4.set(float(appliance_read[12]))
        self.enteredPowerAppliance5.set(float(appliance_read[13]))
        self.enteredPowerAppliance6.set(float(appliance_read[14]))
        self.enteredPowerAppliance7.set(float(appliance_read[15]))
        self.enteredPowerAppliance8.set(float(appliance_read[16]))
        self.enteredPowerAppliance9.set(float(appliance_read[17]))
        
        self.dropdown_variable1.set(float(appliance_read[18]))
        self.dropdown_variable2.set(float(appliance_read[19]))
        self.dropdown_variable3.set(float(appliance_read[20]))
        self.dropdown_variable4.set(float(appliance_read[21]))
        self.dropdown_variable5.set(float(appliance_read[22]))
        self.dropdown_variable6.set(float(appliance_read[23]))
        self.dropdown_variable7.set(float(appliance_read[24]))
        self.dropdown_variable8.set(float(appliance_read[25]))
        self.dropdown_variable9.set(float(appliance_read[26]))
                   
        print(appliance_read)
        return
    
    def zeroise_results(self):
        """Clears results cells in GUI"""
        
        self.result_total_peak.set(0.0)
        self.result_total_avge.set(0.0)
        self.result_total_sd.set(0.0)
        return
    
"""Main loop"""        
if __name__ == "__main__":
    window=escobox_model_tk(None)
    window.title('ESCOBox Minigrid Management Tools')
    window.mainloop()
    
    
        
        
        
        
        
       



