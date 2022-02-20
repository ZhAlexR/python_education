"""The file contain mixed exercises.

There are tasks for Imports, Modules and Packages, Files"
"""
import datetime
import os
import sys


# create new and move to new directory
import time

new_dir = f"{os.getcwd()}/new_dir"
os.mkdir(new_dir, mode=0o777)
os.chdir(new_dir)

# pause the program
time.sleep(10)

with open(f"info_file.txt", "w") as file:
    file.write(f"This string was created at {datetime.datetime.now()}\n"
               f"The OS is {sys.platform}")

