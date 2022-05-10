from tkinter import *
from tkinter import ttk
import sys
sys.path.append('..')
from Server.Models import User, Devices, Rooms

class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        #Setup Menu
        MainMenu(self)
        #Setup Frame
        self.container = Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
	
        self.show_frame(ListUser)	
        
    def show_frame(self, frame, context = None):
        frame = frame(self.container, self, context)
        frame.grid(row=0, column=0, sticky="news")
        frame.tkraise()


class ListUser(Frame):
    def __init__(self, parent, controller, context):
        Frame.__init__(self, parent)

        self.controller = controller

        # Set up treeview
        self.tree = ttk.Treeview(self)
        self.tree.grid(row=0, column=0)

        self.tree['columns']= ('Id', 'Name','Email')
        self.tree.column("#0", width=0,  stretch=NO)
        self.tree.column("Id",anchor=CENTER, width=200)
        self.tree.column("Name",anchor=CENTER, width=200)
        self.tree.column("Email",anchor=CENTER, width=200)

        self.tree.heading("#0",text="",anchor=CENTER)
        self.tree.heading("Id",text="ID",anchor=CENTER)
        self.tree.heading("Name",text="Name",anchor=CENTER)
        self.tree.heading("Email",text="Email",anchor=CENTER)

        self.update_list()
        
        self.tree.bind('<<TreeviewSelect>>', self.item_selected)

        # Set up button
        Button(self, text="Add User", command=self.add_user).grid(row=1, padx=5, pady=5)

    def update_list(self):
        for i, user in enumerate(User().get_all()):
            self.tree.insert(parent='', index='end', iid=i, text='', values=(user["_id"], user["name"], user["email"]))

    def item_selected(self, event):
        item = self.tree.selection()[0]
        item = self.tree.item(item)["values"][0]
        self.controller.show_frame(ListDevices, {"user_id": item})

    def add_user(self):
        newWindow = Toplevel(self)
        newWindow.title("Add User")

        Label(newWindow, text="Name").grid(row=0)
        Label(newWindow, text="Email").grid(row=1)
        Label(newWindow, text="Password").grid(row=2)

        inputName = Entry(newWindow, width=70)
        inputName.grid(row=0, column=1)
        inputEmail = Entry(newWindow, width=70)
        inputEmail.grid(row=1, column=1)
        inputPassword = Entry(newWindow, width=70)
        inputPassword.grid(row=2, column=1)

        def handle_add_button():
            User().create(inputName.get(), inputEmail.get(), inputPassword.get())
            newWindow.destroy()
            self.controller.show_frame(ListUser)

        Button(newWindow, text="Add", command=lambda: handle_add_button()).grid(row=3, columnspan=2)

class ListDevices(Frame):
    def __init__(self, parent, controller, context):
        Frame.__init__(self, parent)

        self.controller = controller
        self.context = context

        self.tree = ttk.Treeview(self)
        self.tree.grid(row=1, columnspan=5)

        self.tree['columns']= ('Id', 'Name', 'Code','Category')
        self.tree.column("#0", width=0,  stretch=NO)
        self.tree.column("Id",anchor=CENTER, width=200)
        self.tree.column("Name",anchor=CENTER, width=200)
        self.tree.column("Code",anchor=CENTER, width=200)
        self.tree.column("Category",anchor=CENTER, width=200)

        self.tree.heading("#0",text="",anchor=CENTER)
        self.tree.heading("Id",text="ID",anchor=CENTER)
        self.tree.heading("Name",text="Name",anchor=CENTER)
        self.tree.heading("Code",text="Code",anchor=CENTER)
        self.tree.heading("Category",text="Category",anchor=CENTER)

        for i, device in enumerate(Devices().get_by_user_id(context["user_id"])):
            self.tree.insert(parent='', index='end', iid=i, text='', values=(device["_id"], device["name"], device["code"], device["category"]))
        
        self.tree.bind('<<TreeviewSelect>>', self.item_selected) 

        # Set up button
        Button(self, text="Go back", command=self.go_back).grid(row=0, column=0, padx=5, pady=5)
        Button(self, text="Delete user", command=self.delete_user).grid(row=0, column=1, padx=5, pady=5)
        Button(self, text="Update user", command=self.update_user).grid(row=0, column=2, padx=5, pady=5)
        Button(self, text="Manage Room", command=lambda:self.controller.show_frame(ListRooms, self.context)).grid(row=0, column=3, padx=5, pady=5)
        Button(self, text="Add device", command=self.add_device).grid(row=2, column=1, padx=5, pady=5)

    def item_selected(self, event):
        item = self.tree.selection()[0]
        item = self.tree.item(item)["values"][0]
        
        newWindow = Toplevel(self)
        newWindow.title("Update infomation")

        Label(newWindow, text="Name").grid(row=0, column=0)
        Label(newWindow, text="Code").grid(row=1, column=0)
        Label(newWindow, text="Catelogy").grid(row=2, column=0)

        inputName = Entry(newWindow, width=70)
        inputName.grid(row=0, column=1, columnspan=2)
        inputCode = Entry(newWindow, width=70)
        inputCode.grid(row=1, column=1, columnspan=2)
        inputCategory = Entry(newWindow, width=70)
        inputCategory.grid(row=2, column=1, columnspan=2)

        def handle_update_button():
            Devices().update(item, inputName.get(), inputCode.get(),inputCategory.get())
            newWindow.destroy()
            self.controller.show_frame(ListDevices, self.context)

        def handle_delete_button():
            Devices().delete(item)
            newWindow.destroy()
            self.controller.show_frame(ListDevices, self.context)

        Button(newWindow, text="Update", command=lambda: handle_update_button()).grid(row=4, column=1)
        Button(newWindow, text="Delete", command=lambda: handle_delete_button()).grid(row=4, column=2)

    
    def add_device(self):
        newWindow = Toplevel(self)
        newWindow.title("Add Device")

        Label(newWindow, text="Name").grid(row=0)
        Label(newWindow, text="Code").grid(row=1)
        Label(newWindow, text="Catelogy").grid(row=2)

        inputName = Entry(newWindow, width=70)
        inputName.grid(row=0, column=1)
        inputCode = Entry(newWindow, width=70)
        inputCode.grid(row=1, column=1, columnspan=2)
        inputCategory = Entry(newWindow, width=70)
        inputCategory.grid(row=2, column=1)

        def handle_add_button():
            Devices().create(inputName.get(), inputCode.get(),inputCategory.get(), self.context["user_id"])
            newWindow.destroy()
            self.controller.show_frame(ListDevices, self.context)

        Button(newWindow, text="Add", command=lambda: handle_add_button()).grid(row=3, column=1)


    def go_back(self):
        self.controller.show_frame(ListUser)

    def update_user(self):
        newWindow = Toplevel(self)
        newWindow.title("Update infomation")

        Label(newWindow, text="Name").grid(row=0)
        Label(newWindow, text="Email").grid(row=1)
        Label(newWindow, text="Password").grid(row=2)

        inputName = Entry(newWindow, width=70)
        inputName.grid(row=0, column=1)
        inputEmail = Entry(newWindow, width=70)
        inputEmail.grid(row=1, column=1)
        inputPassword = Entry(newWindow, width=70)
        inputPassword.grid(row=2, column=1)

        def handle_add_button():
            User().changePassword(self.context["user_id"], inputName.get(), inputEmail.get(), inputPassword.get())
            newWindow.destroy()
            self.controller.show_frame(ListUser)

        Button(newWindow, text="Update", command=lambda: handle_add_button()).grid(row=4, columnspan=2)
    
    def delete_user(self):
        User().delete(self.context["user_id"])
        self.controller.show_frame(ListUser)

class ListRooms(Frame):
    def __init__(self, parent, controller, context):
        Frame.__init__(self, parent)

        self.controller = controller
        self.context = context

        self.tree = ttk.Treeview(self)
        self.tree.grid(row=1, columnspan=4)

        self.tree['columns']= ('Id', 'Name')
        self.tree.column("#0", width=0,  stretch=NO)
        self.tree.column("Id",anchor=CENTER, width=300)
        self.tree.column("Name",anchor=CENTER, width=300)

        self.tree.heading("#0",text="",anchor=CENTER)
        self.tree.heading("Id",text="ID",anchor=CENTER)
        self.tree.heading("Name",text="Name",anchor=CENTER)
        for i, room in enumerate(Rooms().get_by_user_id(context["user_id"])):
            self.tree.insert(parent='', index='end', iid=i, text='', values=(room["_id"], room["name"]))
        
        self.tree.bind('<<TreeviewSelect>>', self.item_selected) 

        # Set up button
        Button(self, text="Go back", command=self.go_back).grid(row=0, column=0, padx=5, pady=5)
        Button(self, text="Delete user", command=self.delete_user).grid(row=0, column=1, padx=5, pady=5)
        Button(self, text="Update user", command=self.update_user).grid(row=0, column=2, padx=5, pady=5)
        Button(self, text="Manage Devices", command=lambda:self.controller.show_frame(ListDevices, self.context)).grid(row=0, column=3, padx=5, pady=5)
        Button(self, text="Add room", command=self.add_room).grid(row=2, column=1, padx=5, pady=5)

    def item_selected(self, event):
        item = self.tree.selection()[0]
        item = self.tree.item(item)["values"][0]
        self.controller.show_frame(ListDevicesOfRoom, {"room_id": item, "user_id": self.context["user_id"]})
   
    def add_room(self):
        newWindow = Toplevel(self)
        newWindow.title("Add Device")

        Label(newWindow, text="Name").grid(row=0)

        inputName = Entry(newWindow, width=70)
        inputName.grid(row=0, column=1)

        def handle_add_button():
            Rooms().create(inputName.get(), self.context["user_id"])
            newWindow.destroy()
            self.controller.show_frame(ListRooms, self.context)

        Button(newWindow, text="Add", command=lambda: handle_add_button()).grid(row=1, column=1)

    def go_back(self):
        self.controller.show_frame(ListUser)

    def update_user(self):
        newWindow = Toplevel(self)
        newWindow.title("Update infomation")

        Label(newWindow, text="Name").grid(row=0)
        Label(newWindow, text="Email").grid(row=1)
        Label(newWindow, text="Password").grid(row=2)

        inputName = Entry(newWindow, width=70)
        inputName.grid(row=0, column=1)
        inputEmail = Entry(newWindow, width=70)
        inputEmail.grid(row=1, column=1)
        inputPassword = Entry(newWindow, width=70)
        inputPassword.grid(row=2, column=1)

        def handle_add_button():
            User().changePassword(self.context["user_id"], inputName.get(), inputEmail.get(), inputPassword.get())
            newWindow.destroy()
            self.controller.show_frame(ListUser)

        Button(newWindow, text="Update", command=lambda: handle_add_button()).grid(row=4, columnspan=2)
    
    def delete_user(self):
        User().delete(self.context["user_id"])
        self.controller.show_frame(ListUser)

class ListDevicesOfRoom(Frame):
    def __init__(self, parent, controller, context):
        Frame.__init__(self, parent)

        self.controller = controller
        self.context = context

        self.tree = ttk.Treeview(self)
        self.tree.grid(row=1, columnspan=2)

        self.tree['columns']= ('Id', 'Name', 'Code','Category')
        self.tree.column("#0", width=0,  stretch=NO)
        self.tree.column("Id",anchor=CENTER, width=200)
        self.tree.column("Name",anchor=CENTER, width=200)
        self.tree.column("Code",anchor=CENTER, width=200)
        self.tree.column("Category",anchor=CENTER, width=200)

        self.tree.heading("#0",text="",anchor=CENTER)
        self.tree.heading("Id",text="ID",anchor=CENTER)
        self.tree.heading("Name",text="Name",anchor=CENTER)
        self.tree.heading("Code",text="Code",anchor=CENTER)
        self.tree.heading("Category",text="Category",anchor=CENTER)

        for i, device in enumerate(Rooms().get_by_id(context["room_id"])["devices"]):
            device = Devices().get_by_id(device)
            self.tree.insert(parent='', index='end', iid=i, text='', values=(device["_id"], device["name"], device["code"], device["category"]))
        
        self.tree.bind('<<TreeviewSelect>>', self.item_selected) 

        # Set up button
        Button(self, text="Go back", command=self.go_back).grid(row=0, column=0, padx=5, pady=5)
        Button(self, text="Manage Room", command=lambda:self.controller.show_frame(ListRooms, self.context)).grid(row=0, column=1, padx=5, pady=5)
        Button(self, text="Add device", command=self.add_device).grid(row=2, column=0, padx=5, pady=5)

    def item_selected(self, event):
        item = self.tree.selection()[0]
        item = self.tree.item(item)["values"][0]
        
        newWindow = Toplevel(self)
        newWindow.title("Delete item?")
        newWindow.geometry("250x30")

        def handle_delete_button():
            Rooms().deleteDevice(self.context["room_id"], item)
            newWindow.destroy()
            self.controller.show_frame(ListDevicesOfRoom, self.context)

        Button(newWindow, text="Delete", command=lambda: handle_delete_button()).pack()

    def add_device(self):
        newWindow = Toplevel(self)
        newWindow.title("Add device")

        tree = ttk.Treeview(newWindow)
        tree.grid(row=1, columnspan=2)

        tree['columns']= ('Id', 'Name', 'Code','Category')
        tree.column("#0", width=0,  stretch=NO)
        tree.column("Id",anchor=CENTER, width=200)
        tree.column("Name",anchor=CENTER, width=200)
        tree.column("Code",anchor=CENTER, width=200)
        tree.column("Category",anchor=CENTER, width=200)

        tree.heading("#0",text="",anchor=CENTER)
        tree.heading("Id",text="ID",anchor=CENTER)
        tree.heading("Name",text="Name",anchor=CENTER)
        tree.heading("Code",text="Code",anchor=CENTER)
        tree.heading("Category",text="Category",anchor=CENTER)

        for i, device in enumerate(Devices().get_by_user_id(self.context["user_id"])):
            tree.insert(parent='', index='end', iid=i, text='', values=(device["_id"], device["name"], device["code"], device["category"]))

        def handle_item_selelec(event):
            item = tree.selection()[0]
            item = tree.item(item)["values"][0]

            Rooms().addDevice(self.context["room_id"], item)

            newWindow.destroy()
            self.controller.show_frame(ListDevicesOfRoom, self.context)
        
        tree.bind('<<TreeviewSelect>>', handle_item_selelec)

    def go_back(self):
        self.controller.show_frame(ListRooms, self.context)


class MainMenu:
    def __init__(self, master):
        menubar = Menu(master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        master.config(menu=menubar)


app = App()
app.title("Admin")
app.mainloop()

