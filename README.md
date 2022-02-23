# PyJournal
This is a journal that's automated using python. It creates directories for years and months, and text files for each day.
## How to use
You need to create a `path_file.txt` in the same directory as the PyJournal script with the path to the main journal directory. Then I created a shell script that sources the virtual python enviroment (not really necessary but may be for future versions) and opens the text file in vim. This would look something like: 
```
source /path/to/bin/activate
vim $(python3 /path/to/python/script/PyJournal.py)
```
This is a very basic journal automation program, but in the future I'm planning on implementing some sort of locking feature using locked compressed .zip files - not the most secure, but files remain unreadable without the password.