'''
Created on 18 March 2015
Copyright De Montfort University
@author: Peter Boait
'''
import random
from math import sqrt


class MonteCarloAggregate: 
    """Provides the Monte Carlo simulation for the complete appliance data set entered in the GUI.
    
    Arguments are:
     - device_popn is an array containing the number of each appliance type to be simulated;
     - run_length is the number of binomial trials to be performed for each appliance;
     - duty_cycles is an array containing the probability that each appliance is operating;
     - power_values is an array containing the power consumed in kW by an instance of each appliance type.
     
     Returns:
      - RunMax is the largest aggregate power observed from the set of trials in run_length;
      - RunAvge is the average power over the set of trials;
      - RunSDpercent is the standard deviation of aggregate power over the set of trials expressed as
      a percentage of the average power (for compatibility with HOMER). 
          
    """
    

    def __init__(self, device_popn, run_length, duty_cycles, power_values):
        
        self.n_array = device_popn
        self.length = run_length
        self.duty_array = duty_cycles
        self.power_array = power_values
        
    
    def aggregate_model(self):
        """Executes the number of binomial trials specified in self.length for each appliance and
        aggregates the resulting power consumed"""
        
        SDinstance=SD() #calculates running SD
        RunMax=0.0
        for k in range(1,self.length+1):
            sum_of_load=0.0
            z=0 #Loop counter to index input data
            for n in self.n_array:
                for j in range(1,n+1):
                    r=random.random() #The Monte Carlo bit
                    if self.duty_array[z]>r: #appliance is operational and consuming power
                        sum_of_load += self.power_array[z] #add power to aggregate
                z=z+1
                
            RunSD=SDinstance.sd(sum_of_load) #compute running value for SD of power
            if sum_of_load>RunMax: #identify maximum
                RunMax=sum_of_load  
               
        #Now compute average load
        z=0 #Loop counter to index input data arrays
        RunAvge=0.0
        for n in self.n_array:
            RunAvge += (n*self.power_array[z]*self.duty_array[z])
            z=z+1 
        
        RunSDpercent = round((RunSD*100)/RunAvge,1)
        
        #print (RunSD)
        return [RunMax,RunAvge,RunSDpercent]       
                

class SD(object):
    """Computes standard deviation incrementally given a new value each time the sd method is called"""
    
    def __init__(self):
        self.sum, self.sum2, self.n = (0.0,0.0,0.0)
    def sd(self, x):
        self.sum  += x
        self.sum2 += x*x
        self.n    += 1.0
        return sqrt(self.sum2/self.n - self.sum*self.sum/self.n/self.n)

# Test code for standard dev incremental function - returns 2.0 from dataset
#sd_inst = SD()
#for value in (2,4,4,4,5,5,7,9):
#    print (value, sd_inst.sd(value))

#Some test code here that can be uncommented and used to run the monte carlo model on its own
#model=MonteCarloAggregate([10,5,5,6,7], 500, [0.2,0.3,0.4,0.5,0.1], [8.6,7.2,5.5,3.3,2.2])
#result=model.aggregate_model_v2()
#print (result[0])
#print (result[1])
#print (result[2])

