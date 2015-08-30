# Title: Python file finder
# Author: Nilu Hilal
# Date: 8/29/2015

import os

print "Welcome to the python file finder"
filename = raw_input("Please enter a filename: ")
foldername = raw_input("Please enter a folder to search: ")
exists = os.path.isfile(os.path.join(foldername, filename))
if exists is True:
    print "it exists!"
else:
    print "its missing!"
