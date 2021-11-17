"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""
import tkinter

# TODO 13.2 Using the tkinter Module
print("=" * 10, "Section 13.2 using tkinter", "=" * 10)
# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter. Use the class name MyGUI2


class MyGUI2:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text="My name is Dylan Bukovsky: Majoring in Computer Science")
        self.label.pack()
        tkinter.mainloop()


my_gui2 = MyGUI2
# TODO 13.3 Adding a label widget
print("=" * 10, "Section 13.3 adding a label widget", "=" * 10)
# Add a label to MyGUI2 (above) that prints your first and last name; pack the label
# Create an instance of MyGUI2

# TODO 13.4 Organizing Widgets with Frames
print("=" * 10, "Section 13.4 using frames", "=" * 10)
# Create a MyGUI3 class that creates a window with two frames
# In the top Frame add labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester
# Create an instance of MyGUI3
class MyGUI3:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)

        self.label_name = tkinter.Label(self.frame1, text="Dylan Bukovsky")
        self.label_name = tkinter.Label(self.frame2, text="Python Programming")

        self.label_name.pack(side='top')
        self.label_major.pack(side='top')

        self.label_python.pack('left')
# TODO 13.5 Button Widgets and info Dialog Boxes
print("=" * 10, "Section 13.5 button widgets and info dialogs", "=" * 10)
# Create a GUI that will tell a joke
# Use a button to show the punch line, which should appear in a dialog box
# Create an instance of the GUI


class MyGUI4:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.joke = tkinter.Label(self.main_window, text="What did the fish say when he hit the wall? ")
        self.punch_line = tkinter.Button(self.main_window, text="Punchline", command=self.reveal)

        self.joke.pack()
        self.punch_line.pack()

        tkinter.mainloop()

    def reveal(self):
        tkinter.messagebox.showinfo('Punchline', 'Dam')


my_gui4 = MyGUI4()


class InchConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.prompt_label = tkinter.Label(self.top_frame, text='Enter a measurement in inches: ')
        self.inch_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label.pack(side='left')
        self.inch_entry.pack(side='left')

        self.descr_label = tkinter.Label(self.mid_frame, text="Converter to centimeters:")
        self.value = tkinter.StringVar()
        self.miles_label = tkinter.Label(self.mid_frame, textvariable= self.value)

        self.descr_label.pack(side='left')
        self.miles_label.pack(side='left')

        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        inches = float(self.inch_entry.get())
        centimeters = inches * 2.54

        self.value.set(centimeters)


kilo_conv = InchConverterGUI()
