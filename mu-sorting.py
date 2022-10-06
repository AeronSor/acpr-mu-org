# Innit bruv
import os
import glob
import re
import shutil
import tkinter as tk
import customtkinter 

if __name__ == "__main__":

    # FRONTEND #

    class App(customtkinter.CTk):
        def __init__(self):
            super().__init__()

            # Window properties
            self.geometry("400x240")
            self.title("MU Organizer")
            # Elements get buggy if set to dark mode for some reason ????
            self.set_appearance_mode("light")

            self.create_widgets()

        def create_widgets(self):
            # Label
            label = customtkinter.CTkLabel(master=self, text="Enter your player name:")
            label.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

            # Entry
            self.name_var = customtkinter.StringVar()
            name_entry = customtkinter.CTkEntry(master=self, textvariable =self.name_var)
            name_entry.place(relx =0.5, rely =0.4, anchor=customtkinter.CENTER)

            # Button
            submit_button = customtkinter.CTkButton(master=self, text='Submit', command= self.submit)
            submit_button.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

               
        def submit(self):
            self.name_var = self.name_var.get()
            self.destroy()

    app = App()
    app.mainloop()


    # BACKEND #
    source = './'

    # Creates list with all the containing MU names
    matchups = ('ZA', 'FA', 'CH', 'MI', 'VE', 'KL', 'DI', 'JA', 'JO', 'OS', 'AX', 'BA',
                'RO', 'SL', 'ED', 'AN', 'IN', 'BR', 'TE', 'KY', 'PO', 'MA', 'SO', 'AB', 'JU')


    # Get name
    user_name = app.name_var

    # Create all directories if they do not exist
    for name in matchups:
        if not os.path.exists(name):
            os.mkdir(name)

        if not os.path.exists("$Spectate"):
            os.mkdir("$Spectate")

    # Get Files
    for file in glob.glob(source + '/*ggr'):

        # Send Spectate replays to /$Spectate folders
        if re.search('^((?!Aeron Sor).)*$', file):
            shutil.copy(file, './$Spectate')
            print(f"Moved {file} to ./$Spectate")
        
        else:

            # Send the rest to its appropriate folder
            for name in matchups:

                if  re.search(f"(?<!{user_name})\({name}\)", file):
                    shutil.copy(file, source+name)
                    print(f"Moved {file} to /{name}")

        # Cleans the leftover files
        os.remove(source+file)

else:
    pass
