# Rocco Carlson
# A terminal-based journal that automatically stores journal data in a text file

import os
from datetime import date

# Directory that journal is stored in
# with open("/path/to/parent/directory", "r") as file:
### ^^^ Outdated way
parent_dir = "/path/to/parent/directory"

# Date and time parsing
d = date.today()
    
daysOfWeek = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
monthsOfYear = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

year_dir = os.path.join(parent_dir, str(d.year))
month_dir = os.path.join(year_dir, str(d.month))
day_path = os.path.join(month_dir, str(d.day))+".md"

# Making the directory + file
if os.path.exists(year_dir) == False:
    os.mkdir(year_dir)
    
if os.path.exists(month_dir) == False:
    os.mkdir(month_dir)
    
if os.path.exists(day_path) == False:
    with open(day_path, "w") as file:
        print(d.isoweekday())
        msg = daysOfWeek[d.isoweekday()-1] + ", " + monthsOfYear[d.month-1] + " " + str(d.day) + ", " + str(d.year)
        msg = "*" + msg + "*\n"
        file.write(msg)

# print out the path to the newly created file for use with a text editor (Vim in the normal use case) 
print(day_path)
