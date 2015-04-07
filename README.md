# ESCoBox_Load_Model
Simulates mini- and micro-grid operation to evaluate load parameters

INTRODUCTION
The purpose of this model is to simulate the operation of electrical appliances commonly required by users of developing world mini- and micro-grids, such as lighting, mobile phone chargers, ceiling fans, refrigerators.  Because of the relatively small numbers of appliances on such grids, the total electrical load they present is highly stochastic and prediction of the maximum load they are likely to present is difficult by conventional methods.  The model comprises a Monte Carlo simulation which simply randomly determines in each time interval whether an appliance is running or not using a probability of use parameter. All appliances are then added together to give the load for that interval. This is repeated many times to give a month or year's operation, with the assumption that each random determination across the population represents one minute.  A user interface provides a default set of appliances and the load each type is likely to present, with the ability to add, change, save, and load an appliance population.

INSTALLATION
The model is coded in Python 2.7.  To run it Python 2.7 and one additional library module must be installed first. The following instructions apply for a Windows 7 or 8 computer:

1. Download and install the latest version of Python 2.7 from  https://www.python.org/downloads/ 

2. Add Python to the Windows PATH settings:
    - Open the Windows Control Panel
    - In the Control Panel, search for and open System.
    - In the dialog box, select Advanced System Settings
    - In the next dialog, select Environment Variables.
    - In the User Variables section, edit the PATH statement to include the following (if there is no PATH variable, click         NEW to create one):  C:\Python27;C:\Python27\Lib\site-packages\;C:\Python27\Scripts\;
  
3.  Install setup tools from  https://pypi.python.org/pypi/setuptools To do this, download  ez_setup.py from the website, preferably so it is on the desktop.  Then open IDLE which is one of the Python programs installed at step 1, and from its File menu open ez_setup.py.  This will open in a new window, select the Run menu and Run module.  
  
4.  Install pip by opening a Windows Command Prompt and entering:  easy_install pip
  
5.  Install Pillow by entering at the Windows Command Prompt: pip install Pillow
 
6.  Finally install the ESCoBox Load Model by entering at the Windows Command Prompt: pip install 


