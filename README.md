# Software-Engineering---Laser-Tag

| Name     | GIT-Hub Username |
|----------|----------|
| Lexi Grozev    | lexigrozev     |
| Torin Eschberger    | tjtorin     |
| Timothy Pham    | timothypham045     |
| Haley Trejo    | https.haley     |

## **Requirements:**

The provided Debian virtual machine already includes:

- Python 3
  
- PostgreSQL

The install script will automatically install all remaining dependencies such as:

- Tkinter

- pip

- virtualenv support

All dependencies will be installed automatically using the install script.

## **Getting the Code:**

### If Git is not installed, install it first:

sudo apt update

sudo apt install -y git

### To download the project onto your local machine or virtual machine, clone the repository using Git:

git clone https://github.com/https-haley/Software-Engineering---Laser-Tag.git

cd Software-Engineering---Laser-Tag

## Downloading the Project Without Git:

If you do not have Git installed, you can download the project as a ZIP file instead.

### Steps:

Open the repository page in your web browser
(example: https://github.com/https-haley/Software-Engineering---Laser-Tag)

Click the green Code button near the top of the page.

Click Download ZIP.

Save the file to your computer.

### Extract the ZIP file:

unzip Software-Engineering---Laser-Tag.zip

cd Software-Engineering---Laser-Tag

### If unzip is not installed, install it:

sudo apt install -y unzip

## **Other Installation Instructions:**

### Run the install script:

chmod +x install.sh

./install.sh

## Running the program

Once all required dependencies are downloaded with the script, run the program using python3 main.py

## **Notes:**

The database schema must not be modified.

All players must have integer player IDs.

Equipment IDs must be unique.

Maximum players per team is 20 for this sprint implementation.

Application tested on Debian VM environment.

If you'd like to select a different network for UDP sockets, hit f2 on the player entry screen.









