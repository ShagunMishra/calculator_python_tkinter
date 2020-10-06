# calculator_python_tkinter

Python offers multiple options for developing GUI (Graphical User Interface). Out of all the GUI methods, tkinter is most commonly used method. It is a standard Python interface to the Tk GUI toolkit shipped with Python. 

To create a tkinter:
1.	Importing the module – tkinter
2.	Create the main window (container)
3.	Add any number of widgets to the main window
4.	Apply the event Trigger on the widgets.
 
To create a main window, tkinter offers a method 
‘Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)’. 
To change the name of the window, we can change the className to the desired one. 

mainloop():
There is a method known by the name mainloop() is used when we are ready for the application to run. mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event till the window is not closed.

import tkinter 
m = tkinter.Tk() 
''' 
widgets are added here 
'''
m.mainloop()

tkinter also offers access to the geometric configuration of the widgets which can organize the widgets in the parent windows. There are mainly three geometry manager classes class.

pack() method:  It organizes the widgets in blocks before placing in the parent widget.
grid() method:  It organizes the widgets in grid (table-like structure) before placing in the parent widget.
place() method: It organizes the widgets by placing them on specific positions directed by the programmer.
