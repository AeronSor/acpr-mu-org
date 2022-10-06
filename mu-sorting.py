"""
My First script of this kind, as you can see its messy as hell, but it works :)
"""

# Innit bruv
import os
import glob
import re
import shutil
import tkinter as tk
from tkinter import messagebox
import customtkinter 


if __name__ == "__main__":

    # FRONTEND #

    class App(customtkinter.CTk):
        def __init__(self):
            super().__init__()

            # Window properties
            self.geometry("450x320")
            self.title("MU Organizer")
            # Elements get buggy if set to dark mode for some reason ????
            self.set_appearance_mode("light")

            # Check variable if program gets closed or not
            self.killed = False

            self.protocol("WM_DELETE_WINDOW", self.on_close)

            self.create_widgets()

        def create_widgets(self):
            # Path Label 
            p_label = customtkinter.CTkLabel(master=self, text="Enter Replay folder Path:")
            p_label.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
            
            # Path entry
            self.path_var = customtkinter.StringVar()
            p_name_entry = customtkinter.CTkEntry(master=self, textvariable =self.path_var)
            p_name_entry.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

            # User Label
            u_label = customtkinter.CTkLabel(master=self, text="Enter your player name:")
            u_label.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

            # User Entry
            self.name_var = customtkinter.StringVar()
            u_name_entry = customtkinter.CTkEntry(master=self, textvariable =self.name_var)
            u_name_entry.place(relx =0.5, rely =0.6, anchor=customtkinter.CENTER)

            # Button
            submit_button = customtkinter.CTkButton(master=self, text='Submit', command= self.submit)
            submit_button.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

               
        def submit(self):
            self.name_var = self.name_var.get()
            self.path_var = self.path_var.get()
            self.destroy()


        def on_close(self):
            self.killed = True
            self.destroy()


    app = App()
    app.mainloop()

    killed = app.killed
    
    if killed == False:

        # BACKEND #

        # Creates list with all the containing MU names
        matchups = ('ZA', 'FA', 'CH', 'MI', 'VE', 'KL', 'DI', 'JA', 'JO', 'OS', 'AX', 'BA',
                    'RO', 'SL', 'ED', 'AN', 'IN', 'BR', 'TE', 'KY', 'PO', 'MA', 'SO', 'AB', 'JU')


        # Get name
        user_name = str(app.name_var)

        # Get path
        source = str(app.path_var)


        # Create all directories if they do not exist
        for name in matchups:
            if not os.path.exists(source+name):
                os.mkdir(source+name)

            if not os.path.exists(source+"$Spectate"):
                os.mkdir(source+"$Spectate")

        # Get Files
        for file in glob.glob( source + '/*ggr'):

            # Send Spectate replays to /$Spectate folders
            if re.search(f'^((?!{user_name}).)*$', file):
                shutil.copy(file, source+'$Spectate')
                print(f"Moved {file} to ./$Spectate")
            
            else:

                # Send the rest to its appropriate folder
                for name in matchups:

                    if  re.search(f"(?<!{user_name})\({name}\)", file):
                        shutil.copy(file, source+name)
                        print(f"Moved {file} to /{name}")

            # Cleans the leftover files
            os.remove(file)

else:
    pass
