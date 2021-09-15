#!/bin/bash

sudo su -
# to use sudo root powers
yum install python3 -y
# to install python version3 as the program file has been made for version 3 interpreter , may show errors in other versions
chmod +x lvm.py
# to make lvm.py file executable
chmod +x automate.py
# to make automate.py file executable
python3 automate.py
# to run the code for execution of various automated lvm tasks
