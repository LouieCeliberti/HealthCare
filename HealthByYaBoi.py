#Some resources to understand pip and mysql connection:
#https://packaging.python.org/tutorials/installing-packages/
#https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html


#Simple program to create a database with one relation and to find the Medications, Pharmacies in a Database. As well as store patient vitals.



import mysql.connector


mydb = mysql.connector.connect(

  host="127.0.0.1",

  user="root",

  password="Lc654321" 

) #provide your own password instead of admin


mycursor = mydb.cursor()

mycursor.execute("drop database if exists university1")
mycursor.execute("create database university1")
mycursor.execute("use university1")
mycursor.execute("create table instructor (ID varchar(5), name varchar(20), dept_name varchar(20), primary key (ID));")
mycursor.execute("INSERT INTO MedicationName VALUES('Mychophenolate');")
mycursor.execute("INSERT INTO MedicationName VALUES('Cyclosporine');")
mycursor.execute("INSERT INTO MedicationName VALUES('Prednisone');")
mycursor.execute("INSERT INTO MedicationName VALUES('Clonodine');")
mycursor.execute("INSERT INTO MedicationName VALUES('Niphedimine');")
mycursor.execute("INSERT INTO MedicationName VALUES('Glycopyrolate');")
mycursor.execute("INSERT INTO MedicationName VALUES('Pantoprezol');")
mycursor.execute("INSERT INTO MedicationName VALUES('Sodium Bicarbonate');")


option = input("Enter medication name to find medication: ")

mycursor.execute("SELECT name from MedicationName where dept_name = '" + option + "';")

myresult = mycursor.fetchall()


if mycursor.rowcount == 0:

  print('No instructors found')

else:

  for x in myresult:

    print(x[0])

mycursor.close()

mydb.close()

