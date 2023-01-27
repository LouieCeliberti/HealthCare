#Some resources to understand pip and mysql connection:
#https://packaging.python.org/tutorials/installing-packages/
#https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html


#Simple program to create a database with one relation and to retrieve Medications, Pharmacies in a Database. As well as store patient vitals.



import mysql.connector


mydb = mysql.connector.connect(

  host="127.0.0.1",

  user="root",

  password="Lc654321" 

) #provide your own password instead of admin


mycursor = mydb.cursor()


option = input("Enter medication name to find medication: ")

mycursor.execute("SELECT", option, "FROM MedicationName;")

myresult = mycursor.fetchall()


if mycursor.rowcount == 0:

  print('Medication name not found')

else:

  for x in myresult:

    print(x[0])

mycursor.close()

mydb.close()

