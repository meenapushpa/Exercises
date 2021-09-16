![Branch Strategy](https://img.shields.io/badge/Branch_Strategy-Linear_Branching-blue.svg)
[![Python 3.6](https://img.shields.io/badge/python-3.6.8-blue.svg)](https://www.python.org/downloads/release/python-368/)

## What does this repository contains?

This repository contains answer for the following challenges in simple python3 program without using any external modules. The birds eye view of this program is load the data from the given source file and process them accordingly to the given requirements/challenges.

## What are all the requriements?

1.	Read in the attached file
     
     a.	Produce a list sorted by “Current Rent” in ascending order
     
     b.	Obtain the first 5 items from the resultant list and output to the console
2.	From the list of all mast data, create a new list of mast data with “Lease Years” = 25 years.
     
     a.	Output the list to the console, including all data fields
     
     b.	Output the total rent for all items in this list to the console
3.	Create a dictionary containing tenant name and a count of masts for each tenant
     
     a.	Output the dictionary to the console in a readable form
4.	List the data for rentals with “Lease Start Date” between 1st June 1999 and 31st August 2007
     
     a.	Output the data to the console with dates formatted as DD/MM/YYYY


## How do I configure workstation to run this program?

* Install Python 3.6 in your workstation, please refer this [link](https://www.python.org/downloads/) for more info

* Create virtual envuironment (Windows) 
     
     `python -m venv venv`                   

* Activate the virtualenv (Windows)       

     `Source venv/Scripts/activate`
* The default modules are used in this program,they are datetime,csv,collections,os,unittest

## How to run this program ?

This program has menu for each requirement mentioned above along with its sub requirements. The way to run the program is

`python exercise_solutions.py`

*Example output*

```
$python exercise_solutions.py
enter the choice as 1/2/3/4/5/6:
1. Sort the current rent in ascending order
2. First 5 values from sorted list
3. Return the data with 'lease year=25'
4. Total rent for above list
5. Dictionary containing tenant name and a count of masts        
6. “Lease Start Date” between 1st June 1999 and 31st August 2007 
1
Enter filepath with extension: C:\Projects\work21\Python Developer Test (1)\Python Developer Test\Python Developer Test Dataset.csv

```

## How to test this program?

This program is using unittest module to do this automated test. This has its own script in order to evaluate the program with the expected values. The way to test the program is

`python -m unittest testcase_solutions.py`

*Example output*

```
$python -m unittest testcase_solution.py
........
----------------------------------------------------------------------
Ran 8 tests in 0.093s

OK
```


