# Prayer_Times
An app that displays the prayer times for mosques on a given date. The prayer times displayed include the names of the prayers, the prayer time, and the iqamah time. 

This is a python script that uses the tkinter and pandas libraries to create a graphical user interface (GUI) for displaying prayer times. The script creates a class called "PrayerTimesApp", which is a tkinter GUI application for showing prayer times.

The script starts by importing the necessary libraries, tkinter, pandas and datetime.

The PrayerTimesApp class takes one argument in its constructor, which is the root window for the GUI. The class initializes the window with the title "Prayer Times" and a white background color.

It then reads a "prayer_times.xlsx" excel file using pandas and gets the current date. The script uses the current date to retrieve the prayer times for that date from the excel file and store them in a dictionary called "times". Another dictionary called "iqama_times" is also created with iqama (second call to prayer) times.

The "create_widgets" method creates the widgets (e.g. labels, buttons) that are displayed in the GUI. The method first creates a label with the text "Rahma Mosque" and sets its font size to 40.

The method then sets the weight of the three columns in the window to 1, which allows them to grow and fill the available space evenly.

Next, it creates a label with the current date and sets its font size to 30. Two other labels for "Athan" and "Iqamah" are created and positioned in the second row of the window with font size 30.

The for-loop then iterates over the prayer times and creates a label for each one with the name of the prayer and the time in the appropriate format. If the prayer time has an associated iqama time, it is displayed in the third column of the window. If not, a label with "N/A" is displayed instead.

Finally, the script creates a root window and sets its title and size. The PrayerTimesApp class is then instantiated and passed the root window as its argument. The window is displayed by calling the mainloop method.