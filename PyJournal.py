# Rocco Carlson
# A terminal-based journal that automatically stores journal data in a text file

from ast import And
import os
from datetime import date

# Directory that journal is stored in
with open("/path_file.txt", "r") as file:
    parent_dir = file.read()
    
d = date.today()
    
daysOfWeek = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
monthsOfYear = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

year_dir = os.path.join(parent_dir, str(d.year))
month_dir = os.path.join(year_dir, str(d.month))
day_path = os.path.join(month_dir, str(d.day))+".txt"

if os.path.exists(year_dir) == False:
    os.mkdir(year_dir)
    
if os.path.exists(month_dir) == False:
    os.mkdir(month_dir)
    
if os.path.exists(day_path) == False:
    with open(day_path, "w") as file:
        msg = daysOfWeek[d.isoweekday()] + ", " + monthsOfYear[d.month-1] + " " + str(d.day) + ", " + str(d.year)
        file.write(msg)
        
print(day_path)