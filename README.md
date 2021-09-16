
**Solution to following Exercises:**

A data file will be provided alongside this test. The dataset is a CSV which contains publicly available data about mobile phone masts in an area of the UK. This file contains un-normalised data (such as multiple variations of Tenant Name) – treat these as individual tenants.

**Actions**

1.	Load the data file, process and output the data in the forms specified
2.	Read in, process and present the data as specified in the requirements section
3.	Demonstrate usage of list comprehension for at least one of the tasks
4.	Allow user input to run all of your script, or specific sections

**Setup**

1. Create virtual envuironment
                   `python -m venv venv`
                   
2. Activate the virtualenv        
                  `Source venv/Scripts/activate`
                  
**Modules Used:**

     datetime,csv,collections,os,unittest
                  
**Requirements**

1.  Read the csv file
a.	Produce a list sorted by “Current Rent” in ascending order
b.	Obtain the first 5 items from the resultant list and output to the console

2.	From the list of all mast data, create a new list of mast data with “Lease Years” = 25 years.
a.	Output the list to the console, including all data fields
b.	Output the total rent for all items in this list to the console

3.	Create a dictionary containing tenant name and a count of masts for each tenant
a.	Output the dictionary to the console in a readable form

4.	List the data for rentals with “Lease Start Date” between 1st June 1999 and 31st August 2007
a.	Output the data to the console with dates formatted as DD/MM/YYYY

**Note **
    Without using of Pandas Library in python




