# Employee_Manager_APP (API)
This is an aplication intended to manage employee's information and reports.

## Table of contents
* [General info](#general-info)
* [Setup](#setup)

## General info
In order to run the program in your local environment, remember to fill in your personal information for the user and password to access the 
methods implemented in the API. These are related with the environment variables: 'admin_key' and 'password'.

The information about the extensions used in python are in the requirements.txt file.

## Setup

* cloning repository
```
$ git clone https://github.com/CristianoR12/Employee_Manager_APP.git
```
* Prepare the virtual environment:
```
# Linux
sudo apt-get install python3-venv    # If needed
Activating: python3 -m venv env
Activating: source env/bin/activate
```

* Enter your IDE (e.g. VSCode) - in case it is the VSCode
```
python -m pip install --upgrade pip
python -m pip install flask
```

* Install all requirements:
```
pip install -r requirements.txt
```

* Fill in the information for the admin_key and password (['admin_key'] and ['password'] with the environment variables)
 
* Start project
```
python3 -m flask run
```






