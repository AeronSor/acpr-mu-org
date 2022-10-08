"""
My First script of this kind, as you can see its messy as hell, but it works :)
"""

# Innit bruv
import os
import glob
import re
import shutil
import tkinter as tk
import customtkinter 


# Makes this only execute as the main file
if __name__ == "__main__":


   # FRONTEND #

    class App(customtkinter.CTk):
        def __init__(self):
            super().__init__()


            # Get path for either Linux or Windows
            if os.name == "posix":
                self.os_path = ""
                self.replay_path = os.path.expanduser('~')
                self.replay_path += "/.steam/steam/steamapps/compatdata/348550/pfx/drive_c/users/steamuser/Documents/ARC SYSTEM WORKS/GGXXAC/Replays/"

            if os.name == "nt":
                self.os_path = " \\ "
                self.replay_path = os.path.expanduser('~')
                self.replay_path += "\\Documents\\ARC SYSTEM WORKS\\GGXXAC\\Replays"


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
            self.p_label = customtkinter.CTkLabel(master=self, text="Enter Replay folder Path:")
            self.p_label.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

            
            # Path entry
            self.path_var = customtkinter.StringVar()
            self.p_name_entry = customtkinter.CTkEntry(master=self, textvariable =self.path_var)
            self.p_name_entry.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
            self.p_name_entry.insert(0, self.replay_path)


            # User Label
            self.u_label_var = tk.StringVar()
            self.u_label_var.set("Enter your player name:")

            self.u_label = customtkinter.CTkLabel(master=self, textvariable=self.u_label_var)
            self.u_label.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)


            # User Name Entry
            self.name_var = tk.StringVar()

            # Get username from file automatically
            if os.path.exists('player.txt'):
                file_usr_name = open('player.txt', 'r')
                file_usr_name = file_usr_name.read()
                self.name_var.set(file_usr_name) 

            self.u_name_entry = customtkinter.CTkEntry(master=self, textvariable =self.name_var)
            self.u_name_entry.place(relx =0.5, rely =0.6, anchor=customtkinter.CENTER)


            # Button
            self.submit_button = customtkinter.CTkButton(master=self, text='Submit', command= self.submit)
            self.submit_button.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

               
        def submit(self):

            # Get values from GUI into strings for backend
            self.name_out = self.name_var.get()
            self.path_out = self.path_var.get()


            # Write the name written into a file
            open('player.txt', 'w').write(self.name_out)

            
            self.p_label.destroy()
            self.p_name_entry.destroy()

            # Runs the actual thing
            self.sorting()

            self.u_label_var.set("DONE!")

        def sorting(self):
            
            # BACKEND #
            # Creates list with all the containing MU names
            matchups = ('ZA', 'FA', 'CH', 'MI', 'VE', 'KL', 'DI', 'JA', 'JO', 'OS', 'AX', 'BA',
                        'RO', 'SL', 'ED', 'AN', 'IN', 'BR', 'TE', 'KY', 'PO', 'MA', 'SO', 'AB', 'JU')

            # Get name
            user_name = str(app.name_out)

            # Get path
            source = str(app.path_out)


            # Create all directories if they do not exist
            for name in matchups:
                if not os.path.exists(source + self.os_path + name):
                    os.mkdir(source + self.os_path + name)

                if not os.path.exists(source+ self.os_path + "$Spectate"):
                    os.mkdir(source + self.os_path + "$Spectate")

            # Get Files
            
            for file in glob.glob( source + '*ggr'):

                # Send Spectate replays to /$Spectate folders
                if re.search(f'^((?!{user_name}).)*$', file):
                    shutil.copy(file, source + self.os_path + '$Spectate')
                    print(f"Moved {file} to ./$Spectate")
                
                else:

                    # Send the rest to its appropriate folder
                    for name in matchups:

                        if  re.search(f"(?<!{user_name})\({name}\)", file):
                            shutil.copy(file, source + self.os_path + name)
                            print(f"Moved {file} to /{name}")

                # Cleans the leftover files
                os.remove(file)


        # Close event behaviour that triggers with 'self.protocol("WM_DELETE_WINDOW")'
        def on_close(self):
            self.destroy()


    # App mainloop
    app = App()
    app.mainloop()
