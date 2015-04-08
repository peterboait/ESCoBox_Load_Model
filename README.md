# ESCoBox_Load_Model
Simulates mini- and micro-grid operation to evaluate load parameters

INTRODUCTION
The purpose of this model is to simulate the operation of electrical appliances commonly required by users of developing world mini- and micro-grids, such as lighting, mobile phone chargers, ceiling fans, refrigerators.  Because of the relatively small numbers of appliances on such grids, the total electrical load they present is highly stochastic and prediction of the maximum load they are likely to present is difficult by conventional methods.  The model comprises a Monte Carlo simulation which simply randomly determines in each time interval whether an appliance is running or not using a probability of use parameter. All appliances are then added together to give the load for that interval. This is repeated many times to give a month or year's operation, with the assumption that each random determination across the population represents one minute.  A user interface provides a default set of appliances and the load each type is likely to present, with the ability to add, change, save, and load an appliance population.

NOTE
As prototype open surce software, it is published in the hope that it is useful but no warranty of fitness for purpose is given.

INSTALLATION
The model is coded in Python 2.7.  To run it Python 2.7 and one additional library module must be installed first. The following instructions apply for a Windows 7 or 8 computer:

1. Download and install the latest version of Python 2.7 (2.7.9 or later) from  https://www.python.org/downloads/ 

2. Add Python to the Windows PATH settings:
    - Open the Windows Control Panel
    - In the Control Panel, search for and open System.
    - In the dialog box, select Advanced System Settings
    - In the next dialog, select Environment Variables.
    - In the User Variables section, edit the PATH statement to add the following (if there is no PATH variable, click         NEW to create one):  C:\Python27;C:\Python27\Lib\site-packages\;C:\Python27\Scripts\;
  
3.  Install Pillow by entering at the Windows Command Prompt: pip install Pillow
 
4.  Download the model as a zip file by clicking the button "Download ZIP" on the right hand side of the ESCoBox_Load_Model home page on GitHub (https://github.com/peterboait/ESCoBox_Load_Model/)   

5.  Unzip the download and browse down the unzipped folders to /nested/... This contains the code modules. Double-clicking on model_gui.py should run the model. Recommend that a shortcut be created by right-clicking on that file and selecting create shortcut, then move the shortcut to the desktop.  If double clicking does not work, open the IDLE program that will have been installed in step 1, from the File menu click Open and browse to model_gui.py and open it. This will come up in a new window, select Run and Run module - this should run the model.  

OPERATION
To demonstrate operation, click the "Open model" button. This opens the "nested" directory".  Look for the folder called model_inputs and open that. Select one of the files in it and open.  This populates the model with some example data which can be run using either of the "Run model-month" or "Run model-year" buttons.  Note the year run can take 15 minutes or more.

To create a mini-grid model, first decide on the time of day being simulated.  Then set up the appliance population - the numbers of each and their load can be edited if the defaults are not correct.  Select the probability of an appliance being in use from the drop-downs on the right, given the time of day - this does not have to be very accurate so an "intelligent guess" is appropriate. There must be a value in all the data entry cells, should be zero where not used. Then run using the run buttons to determine the peak and average power load that should be expected, and the standard deviation of variation in power expressed as a percentage of the average.

The model entered can be saved using the save button - use the model_inputs directory or create a new one.  This allows multiple models for different times of the day to be easily created for a single set of appliances just by modifying the probability of use drop-down.  


