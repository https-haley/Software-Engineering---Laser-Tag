# Software-Engineering---Laser-Tag

| Name     | GIT-Hub Username |
|----------|----------|
| Lexi Grozev    | lexigrozev     |
| Torin Eschberger    | tjtorin     |
| Timothy Pham    | timothypham045     |
| Haley Trejo    | https.haley     |

# **Requirements:**

The provided Debian virtual machine already includes:
  
- PostgreSQL

- Python3

The install script will automatically install all remaining dependencies such as:

- Tkinter

- pip

- virtualenv support

# **Getting the Code using Git:**

First, open the provided Debian VM. Log in using username: student and password: student.

### If Git is not installed, install it first:

Run these commands in the VM terminal.

```
sudo apt update
```
```
sudo apt install -y git
```

### To download the project onto your virtual machine, clone the repository using Git:

Run these commands in the VM terminal.

```
git clone https://github.com/https-haley/Software-Engineering---Laser-Tag.git
```
```
cd Software-Engineering---Laser-Tag
```
# Downloading the Project Without Git:

If you do not have Git installed, you can download the project as a ZIP file instead.

### Steps:

Open the repository page in your web browser.

Click the green Code button near the top of the page.

Click Download ZIP.

Save the file to your computer.

### If unzip is not installed, install it:

Run this command in the VM terminal.

```
sudo apt install -y unzip
```

### Extract the ZIP file:

Run these commands in the VM terminal.
```
cd ~/Downloads
```
```
unzip Software-Engineering---Laser-Tag-main.zip
```
```
cd Software-Engineering---Laser-Tag-main
```
# **Other Installation Instructions (once the code is on your machine):**

### Run the install script:

Run these commands in the VM terminal.

```
chmod +x install.sh
```
```
./install.sh
```
# Running the program:

Once installation is complete and you are inside the project directory (see the cd commands in the download steps above), activate the virtual environment:

```
source venv/bin/activate
```

Run the program using:

```
python3 main.py
```
# **Notes:**

The database schema must not be modified.

All players must have integer player IDs.

Equipment IDs must be unique.

Maximum players per team is 20 for this implementation.

Application tested on Debian VM environment.

If you'd like to select a different network for UDP sockets, hit f2 on the player entry screen.

To update an existing players username hit insert, then type the player ID, new username, and equipment ID (player must not already be added in the game). If the player is already added to the game, delete them first.





















