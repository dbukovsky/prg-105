"""
Write a GUI program that calculates a car’s gas mileage.
The program’s window should have Entry widgets that let the user
enter the number of gallons of gas the car holds, and the number
of miles it can be driven on a full tank. When a Calculate MPG button is
clicked, the program should display the number of miles that the car may
be driven per gallon of gas. Use the following formula to calculate miles
per gallon:
"""

import tkinter


class MPG:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.frame1 = tkinter.Frame()
        self.frame2 = tkinter.Frame()
        self.frame3 = tkinter.Frame()
        self.frame4 = tkinter.Frame()

        # Frame 1
        self.gallon_label = tkinter.Label(self.frame1, text='Enter how many gallons of gas your car holds')
        self.gallon_entry = tkinter.Entry(self.frame1, width=10)

        self.gallon_label.pack(side='left')
        self.gallon_entry.pack(side='left')

        # Frame 2
        self.miles_label = tkinter.Label(self.frame2, text='How many miles have you traveled? ')
        self.miles_entry = tkinter.Entry(self.frame2, width=10)

        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')

        # Frame 3
        self.mpg_value = tkinter.StringVar()
        self.miles_per_gallon = tkinter.Label(self.frame3, text='Your gas mileage: ')
        self.results = tkinter.Label(self.frame3, textvariable=self.mpg_value)

        self.miles_per_gallon.pack(side='left')
        self.results.pack(side='left')

        # Frame 4
        self.calc_button = tkinter.Button(self.frame4, text="Calculate", command=self.calculate)
        self.quit_button = tkinter.Button(self.frame4, text='Quit', command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack Frames
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()

        tkinter.mainloop()

    def calculate(self):
        gallons = float(self.gallon_entry.get())
        miles = float(self.miles_entry.get())
        self.mpg_value.set = format(miles/gallons, ",.2f")


mpg = MPG()
