import tkinter
import tkinter.messagebox
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('600x300')
        self.main_window.title('Responsive Registration Form')
        self.main_window.configure(bg='light blue')

        self.frame1 = tkinter.Frame(self.main_window, width = 300)
        self.frame2 = tkinter.Frame(self.main_window, width = 300)
        self.frame3 = tkinter.Frame(self.main_window, width = 300)
        self.frame4 = tkinter.Frame(self.main_window, width = 300)
        self.frame5 = tkinter.Frame(self.main_window, width = 300)
        self.frame6 = tkinter.Frame(self.main_window, width = 300)
        self.frame7 = tkinter.Frame(self.main_window, width = 300)
        self.frame8 = tkinter.Frame(self.main_window, width = 300)
        self.frame9 = tkinter.Frame(self.main_window, width = 300)
        self.frame10 = tkinter.Frame(self.main_window, width = 300)

        self.label1 = tkinter.Label(self.frame1, text = 'Responsive Registration Form', width = 100, bg = 'light blue')
        self.email_label = tkinter.Label(self.frame2, text = 'Email:', bg = 'light blue')
        self.email_entry = tkinter.Entry(self.frame2, width = 50, bg = 'light blue')
        self.password_label = tkinter.Label(self.frame3, text = 'Password:', bg = 'light blue')
        self.password_entry = tkinter.Entry(self.frame3,show = '*', width = 47, bg = 'light blue')
        self.retype_label = tkinter.Label(self.frame4, text = 'Retype password:', bg = 'light blue')
        self.retype_entry = tkinter.Entry(self.frame4,show = '*', width = 40, bg = 'light blue')
        self.first_name = tkinter.Label(self.frame5,text = 'First Name:', bg = 'light blue')
        self.first_name_entry = tkinter.Entry(self.frame5, width = 30, bg = 'light blue')
        self.last_name = tkinter.Label(self.frame6, text = 'Last name:', bg = 'light blue')
        self.last_name_entry = tkinter.Entry(self.frame6, width = 31, bg = 'light blue')
        self.radio_var = tkinter.IntVar()
        self.rb1 = tkinter.Radiobutton(self.frame7, text = 'Male', variable = self.radio_var, value = 1, bg = 'light blue')
        self.rb2 = tkinter.Radiobutton(self.frame7, text = 'Female', variable = self.radio_var, value = 2, bg = 'light blue')
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb1 = tkinter.Checkbutton(self.frame8, text = 'I agree to terms and conditions', variable = self.cb_var1, bg = 'light blue')
        self.cb2 = tkinter.Checkbutton(self.frame9, text = 'I want to receive the newsletter', variable = self.cb_var2, bg = 'light blue')
        self.register = tkinter.Button(self.frame10, text = 'Register', command = self.validate_choices, bg = 'light green')

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()
        self.frame7.pack()
        self.frame8.pack()
        self.frame9.pack()
        self.frame10.pack()

        self.label1.pack()
        self.email_label.pack(side = 'left')
        self.email_entry.pack(side = 'left')
        self.password_label.pack(side = 'left')
        self.password_entry.pack(side = 'left')
        self.retype_label.pack(side = 'left')
        self.retype_entry.pack(side = 'left')
        self.first_name.pack(side = 'left')
        self.first_name_entry.pack(side = 'left')
        self.last_name.pack(side = 'left')
        self.last_name_entry.pack(side = 'left')
        self.rb1.pack(side = 'left')
        self.rb2.pack(side= 'left')
        self.cb1.pack()
        self.cb2.pack()
        self.register.pack()
        
        tkinter.mainloop()
    def validate_choices(self):

        password = self.password_entry.get()
        retype_password = self.retype_entry.get()
        gender = self.radio_var.get()
        agree_terms = self.cb_var1.get()
        receive_newsletter = self.cb_var2.get()

        if gender == 0:
            tkinter.messagebox.showerror("Error", "Please select a gender.")
            return
        if not agree_terms:
            tkinter.messagebox.showerror("Error", "Please agree to terms and conditions.")
            return
        if not receive_newsletter:
            tkinter.messagebox.showerror("Error", "Please agree to receive the newsletter.")
            return
        if password != retype_password:
            tkinter.messagebox.showerror("Error", "Passwords do not match.")
            return
        tkinter.messagebox.showinfo("Registration Successful")
My_gui = MyGUI()
