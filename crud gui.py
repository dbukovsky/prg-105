#   CRUD GUI SAMPLE

import tkinter
import pickle
import tkinter.messagebox


class CrudGui:
    def __init__(self, master):
        self.master = master
        self.master.title('Welcome Menu')
        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # create radio buttons
        self.look = tkinter.Radiobutton(self.top_frame, text='Look up customer', variable=self.radio_var, value=1)
        self.add = tkinter.Radiobutton(self.top_frame, text='Add customer', variable=self.radio_var, value=2)
        self.change = tkinter.Radiobutton(self.top_frame, text='Change customer info', variable=self.radio_var, value=3)
        self.delete = tkinter.Radiobutton(self.top_frame, text='Delete customer', variable=self.radio_var, value=4)

        # pack radio buttons
        self.look.pack(anchor='w', padx=20)
        self.add.pack(anchor='w', padx=20)
        self.change.pack(anchor='w', padx=20)
        self.delete.pack(anchor='w', padx=20)

        # create ok and quit buttons
        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.master.destroy)

        # pack buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    def open_menu(self):
        if self.radio_var.get() == 1:
            _ = LookGUI(self.master)
        elif self.radio_var.get() == 2:
            _ = AddGUI(self.master)
        elif self.radio_var.get() == 3:
            _ = ChangeGUI(self.master)
        elif self.radio_var.get() == 4:
            _ = DeleteGUI(self.master)
        else:
            tkinter.messagebox.showinfo("Function", 'Under Construction')


class LookGUI:
    def __init__(self, master):
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
        except (FileNotFoundError, IOError):
            self.customers = {}

        self.look = tkinter.Toplevel(master)
        self.look.title('Search for customer')

        # create frames
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # add widgets to the top frame
        self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to look for: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        # middle frame - label for results
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results:')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        # pack middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')

        # Bottom frame - buttons
        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def search(self):
        name = self.search_entry.get()
        result = self.customers.get(name, 'Not Found')
        self.value.set(result)

    def back(self):
        self.look.destroy()


class AddGUI:
    def __init__(self, master):
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
        except (FileNotFoundError, IOError):
            self.customers = {}

        self.add = tkinter.Toplevel(master)
        self.add.title('Search for customer')

        # create frames
        self.top_frame = tkinter.Frame(self.add)
        self.middle_frame = tkinter.Frame(self.add)
        self.bottom_frame = tkinter.Frame(self.add)

        # add widgets to the top frame
        self.add_label = tkinter.Label(self.top_frame, text='Enter customer name to add: ')
        self.add_entry = tkinter.Entry(self.top_frame, width=15)
        self.email_label = tkinter.Label(self.top_frame, text='Enter customer email')
        self.email_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.add_label.pack(side='left')
        self.add_label.pack(side='left')
        self.email_label.pack(side='left')
        self.email_entry.pack(side='left')

        # middle frame - label for results
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results:')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        # pack middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')

        # Bottom frame - buttons
        self.add_button = tkinter.Button(self.bottom_frame, text='Search', command=self.add_person)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.add_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def add_person(self):
        name = self.add_entry.get()
        email = self.email_entry.get()
        if name in self.customers:
            result = name + 'Already exists'
        else:
            result = name + " " + email + ' will be added'
            self.customers[name] = email
            output_file = open("customer file.dat", 'wb')
            pickle.dump(self.customers, output_file)
            output_file.close()
        self.value.set(result)

    def back(self):
        self.add.destroy()


class ChangeGUI:
    def __init__(self, master):
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
        except (FileNotFoundError, IOError):
            self.customers = {}

        self.change = tkinter.Toplevel(master)
        self.change.title('Search for customer')

        # create frames
        self.top_frame = tkinter.Frame(self.change)
        self.middle_frame = tkinter.Frame(self.change)
        self.bottom_frame = tkinter.Frame(self.change)

        # add widgets to the top frame
        self.change_label = tkinter.Label(self.top_frame, text='Enter customer name to change: ')
        self.change_entry = tkinter.Entry(self.top_frame, width=15)
        self.email_label = tkinter.Label(self.top_frame, text='Change customer email')
        self.email_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.change_label.pack(side='left')
        self.change_label.pack(side='left')
        self.email_label.pack(side='left')
        self.email_entry.pack(side='left')

        # middle frame - label for results
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results:')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        # pack middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')

        # Bottom frame - buttons
        self.change_button = tkinter.Button(self.bottom_frame, text='Search', command=self.change_person)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.change_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def change_person(self):
        name = self.change_entry.get()
        email = self.email_entry.get()
        if name in self.customers:
            result = name + 'Already exists'
        else:
            result = name + " " + email + ' will be changed'
            self.customers[name] = email
            output_file = open("customer file.dat", 'wb')
            pickle.dump(self.customers, output_file)
            output_file.close()
        self.value.set(result)

    def back(self):
        self.change.destroy()


class DeleteGUI:
    def __init__(self, master):
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
        except (FileNotFoundError, IOError):
            self.customers = {}

        self.delete = tkinter.Toplevel(master)
        self.delete.title('Delete customer')

        # create frames
        self.top_frame = tkinter.Frame(self.delete)
        self.middle_frame = tkinter.Frame(self.delete)
        self.bottom_frame = tkinter.Frame(self.delete)

        # add widgets to the top frame
        self.delete_label = tkinter.Label(self.top_frame, text='Enter customer name to delete: ')
        self.delete_entry = tkinter.Entry(self.top_frame, width=15)
        self.email_label = tkinter.Label(self.top_frame, text='Delete customer email')
        self.email_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.delete_label.pack(side='left')
        self.delete_label.pack(side='left')
        self.email_label.pack(side='left')
        self.email_entry.pack(side='left')

        # middle frame - label for results
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results:')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        # pack middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')

        # Bottom frame - buttons
        self.delete_button = tkinter.Button(self.bottom_frame, text='Search', command=self.delete_person)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.delete_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def delete_person(self):
        name = self.delete_entry.get()
        email = self.email_entry.get()
        if name in self.customers:
            result = name + 'Already exists'
        else:
            result = name + " " + email + ' will be deleted'
            self.customers[name] = email
            output_file = open("customer file.dat", 'wb')
            pickle.dump(self.customers, output_file)
            output_file.close()
        self.value.set(result)

    def back(self):
        self.delete.destroy()


def main():
    root = tkinter.Tk()
    _ = CrudGui(root)
    root.mainloop()


main()
