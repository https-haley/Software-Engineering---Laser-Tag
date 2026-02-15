#!/bin/bash

sudo apt install python3-tk # Install tkinter
sudo apt-get install python3-venv

# Create virtual environment and install required libs
python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
