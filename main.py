#Some resources to understand pip and mysql connection:
#https://packaging.python.org/tutorials/installing-packages/
#https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html


#Simple program to create a database with one relation and to retrieve Medications, Pharmacies in a Database. As well as store patient vitals.



#import mysql.connector

import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="Medication", user='postgres', password='pswd', host='127.0.0.1', port= '5432'
)

#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving data
cursor.execute('''SELECT * from MedicationName''')

#Fetching 1st row from the table
result = cursor.fetchone();
print(result)

#Fetching 1st row from the table
result = cursor.fetchall();
print(result)

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()
