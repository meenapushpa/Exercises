import csv
from collections import Counter
import datetime
import os

# read the given csv file and return the data in list of dictionaries format
def readCsv(csvfile):
    with open(csvfile,'r')as f:
        reader=csv.DictReader(f)
        
        rows = []
        for row in reader:
            rows.append(row)

        finalList = []
        for i in rows:
            Name=i["Property Name"]
            Address1=i["Property Address [1]"]
            Address2=i["Property  Address [2]"]
            Address3=i["Property Address [3]"]
            Address4=i["Property Address [4]"]
            UnitName=i["Unit Name"]
            TenantName=i["Tenant Name"]
            StartDate=i["Lease Start Date"]
            EndDate=i["Lease End Date"]
            LeaseYears = int(i["Lease Years"])
            Rent=float(i["Current Rent"])
            finalList.append({'PropertyName':Name, 'PropertyAddress1':Address1,'PropertyAddress2':Address2, 
                          'PropertyAddress3':Address3,'PropertyAddress4':Address4,'UnitName':UnitName,
                          'TenantName':TenantName,'StartDate':StartDate,'EndDate':EndDate,'LeaseYears':LeaseYears,
                          'CurrentRent':Rent})
        return finalList

# produce a list sorted by “Current Rent” in ascending order
def exercise1_a(filepath):
    listvalue = readCsv(filepath)
    sortedlist = sorted(listvalue, key=lambda row: row['CurrentRent'])
    return sortedlist

# obtain the first 5 items from the resultant list and output to the console
def exercise1_b(filepath):
     values=exercise1_a(filepath)
     first5list=values[:5]
     return first5list
 
# output the list with lease year=25 to the console, including all data fields
def exercise2_a(filepath):
    listvalue = readCsv(filepath)
    newleaseyearlist = list(filter(lambda row: row['LeaseYears']==25, listvalue))
    return newleaseyearlist

# output the total rent for all items in this list to the console
def exercise2_b(filepath):
    newlist=exercise2_a(filepath)
    TotalRent=0
    for i in newlist:
        TotalRent+=i['CurrentRent']
    return TotalRent

# dictionary containing tenant name and a count of masts for each tenant and return the output       
def exercise3(filepath):
    listvalue = readCsv(filepath)
    TenantNamelist=[]
    for i in listvalue:
        TenantName=i['TenantName']
        TenantNamelist.append(TenantName)
    Tenantnamecount=Counter(TenantNamelist)
    return dict(Tenantnamecount)

# list the data for rentals with “Lease Start Date” between 1st June 1999 and 31st August 2007
def exercise4(filepath):
    listvalue = readCsv(filepath)
    startdate = datetime.datetime.strptime('1-Jun-99', '%d-%b-%y')
    enddate=datetime.datetime.strptime('31-Aug-07', '%d-%b-%y')
    datelist=[]
    for i in listvalue:
       if datetime.datetime.strptime(i['StartDate'], '%d-%b-%y') >=startdate and datetime.datetime.strptime(i['StartDate'], '%d-%b-%y')<=enddate:
          datetimeval=datetime.datetime.strptime(i['StartDate'],'%d-%b-%y').strftime('%d/%m/%Y')
          i.update({"StartDate":datetimeval})
          datelist.append(i)
    return datelist

if __name__=='__main__':
    
    option = int(input("enter the choice as 1/2/3/4/5/6: \n"
                                           "1. Sort the current rent in ascending order \n"
                                           "2. First 5 values from sorted list \n"
                                           "3. Return the data with 'lease year=25' \n"
                                           "4. Total rent for above list \n"
                                           "5. Dictionary containing tenant name and a count of masts \n"
                                           "6. “Lease Start Date” between 1st June 1999 and 31st August 2007 \n"))
    if option == 1:
        filename=input('Enter filepath with extension: ')
        assert os.path.exists(filename), "No such file or directory, "+str(filename)
        val1=exercise1_a(filename)
        print(val1)
    elif option == 2:
        filename=input('Enter filepath: ')
        assert os.path.exists(filename), "No such file or directory, "+str(filename)
        val2=exercise1_b(filename)
        print(val2)
    elif option == 3:
        filename=input('Enter filepath: ')
        val3=exercise2_a(filename)
        print(val3)
    elif option == 4:
        filename=input('Enter filepath: ')
        assert os.path.exists(filename), "No such file or directory, "+str(filename)
        val4=exercise2_b(filename)
        print(val4)
    elif option == 5:
        filename=input('Enter filepath: ')
        val5=exercise3(filename)
        print(val5)
    elif option == 6:
        filename=input('Enter filepath: ')
        val6=exercise4(filename)
        print(val6)  
    else:
        print("Incorrect option")
    
    
