# Innit bruv
import os
import glob
import re
import shutil



# BACKEND #


source = './'

# Creates list with all the containing MU names
matchups = ('ZA', 'FA', 'CH', 'MI', 'VE', 'KL', 'DI', 'JA', 'JO', 'OS', 'AX', 'BA',
            'RO', 'SL', 'ED', 'AN', 'IN', 'BR', 'TE', 'KY', 'PO', 'MA', 'SO', 'AB', 'JU')


# Get name
print("Type your user name")
user_name = input()

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
