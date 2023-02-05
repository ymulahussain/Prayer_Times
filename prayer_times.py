import tkinter as tk                                                                                            # import tkinter module as tk
import pandas as pd                                                                                             # import pandas module as pd
import datetime                                                                                                 # import datetime module

class PrayerTimesApp:                                                                                           # define a class named PrayerTimesApp

    def __init__(self, master):                                                                                  # define __init__ method with master as argument
        self.master = master                                                                                     # set the value of master to the argument passed to the method
        self.master.title("Prayer Times")                                                                        # set the title of master to "Prayer Times"
        self.master.configure(bg='white')                                                                        # set the background color of master to white
        self.df = pd.read_excel('prayer_times.xlsx')                                                             # read data from the excel file named 'prayer_times.xlsx' and assign it to self.df
        self.current_date = datetime.datetime.now().strftime("%Y-%m-%d")                                        # get the current date and format it to YYYY-MM-DD and assign it to self.current_date
        self.index = self.df[self.df['Date'] == self.current_date].index.tolist()[0]                            # get the index of the current date from the dataframe self.df and assign it to self.index
        self.times = {                                                                                           # create a dictionary self.times with prayer timings for the current date
            "Fajr": self.df.at[self.index, 'Fajr'],
            "Sunrise": self.df.at[self.index, 'Sunrise'],
            "Dhuhr": self.df.at[self.index, 'Dhuhr'],
            "Asr": self.df.at[self.index, 'Asr'],
            "Maghrib": self.df.at[self.index, 'Maghrib'],
            "Isha": self.df.at[self.index, 'Isha']
        }
        self.iqama_times = {                                                                                     # create a dictionary self.iqama_times with iqama timings for the current date
            "Fajr": self.df.at[self.index, 'Fajr_Iqamah'],
            "Sunrise": self.df.at[self.index, 'Sunrise'],
            "Dhuhr": self.df.at[self.index, 'Dhuhr_Iqamah'],
            "Asr": self.df.at[self.index, 'Asr_Iqamah'],
            "Maghrib": self.df.at[self.index, 'Maghrib_Iqamah'],
            "Isha": self.df.at[self.index, 'Isha_Iqamah']
        }
        self.create_widgets()                                                                              # call create_widgets method


    def create_widgets(self):
        fontsize = 30
        # create a label for the title of the app
        self.title = tk.Label(self.master, text="Rahma Mosque", font=("Helvetica", 40), bg='white')
        # place the title label in the first row and spanning across three columns
        self.title.grid(row=0, column=0, columnspan=3, pady=50)
        
        # configure the weight of the three columns
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)
        
        # create labels for the headers of the table
        tk.Label(self.master, text="Date: "+self.current_date, font=("Helvetica", fontsize), bg='white').grid(row=1, column=0, pady=10)
        tk.Label(self.master, text="Athan", font=("Helvetica", fontsize), bg='white').grid(row=1, column=1, pady=10)
        tk.Label(self.master, text="Iqamah", font=("Helvetica", fontsize), bg='white').grid(row=1, column=2, pady=10)
        
        # loop through the prayer times and create labels for each one
        for i, prayer_time in enumerate(self.times):
            # configure the weight of the current row
            self.master.grid_rowconfigure(i + 2, weight=1)
            # create a label for the name of the prayer time
            name = tk.Label(self.master, text=prayer_time, font=("Helvetica", fontsize), bg='white')
            # place the name label in the current row, first column
            name.grid(row=i + 2, column=0, pady=10)
            
            # format the time string
            time_str = self.times[prayer_time].strftime("%H:%M")
            time = datetime.datetime.strptime(time_str, "%H:%M").strftime("%I:%M %p")
            # create a label for the time of the prayer time
            time_label = tk.Label(self.master, text=time, font=("Helvetica", fontsize), bg='white')
            # place the time label in the current row, second column
            time_label.grid(row=i + 2, column=1, pady=10)
            
            # if there is an iqamah time for the current prayer time
            if prayer_time in self.iqama_times:
                # format the iqamah time string
                iqama_time_str = self.iqama_times[prayer_time].strftime("%H:%M")
                iqama_time = datetime.datetime.strptime(iqama_time_str, "%H:%M").strftime("%I:%M %p")
                # create a label for the iqamah time
                iqama_time_label = tk.Label(self.master, text=iqama_time, font=("Helvetica", fontsize), bg='white')
            else:
                # create a label with "N/A" for the iqamah time if not found in the dictionary
                iqama_time_label = tk.Label(self.master, text="N/A", font=("Helvetica", fontsize), bg='white')
            # add the iqamah time label to the grid
            iqama_time_label.grid(row=i + 2, column=2, pady=10)


# call the update function to run once initially




root = tk.Tk() # create the Tkinter object
app = PrayerTimesApp(root) # create the PrayerTimesApp object and pass the Tkinter object as the master
root.mainloop() # run the main loop for the Tkinter object

