#Some resources to understand pip and mysql connection:
#https://packaging.python.org/tutorials/installing-packages/
#https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html


#Simple program to create a database with one relation and to find the instructors in a department



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
mycursor.execute("insert into instructor values ('1', 'Tian Tian', 'CS');")
mycursor.execute("insert into instructor values ('2', 'Marvin Bishop', 'Math');")
mycursor.execute("insert into instructor values ('3', 'Kashifuddin Qazi', 'CS');")
mycursor.execute("insert into instructor values ('4', 'Sr. Joan', 'Math');")


option = input("Enter department name to find instructors: ")

mycursor.execute("SELECT name from instructor where dept_name = '" + option + "';")

myresult = mycursor.fetchall()


if mycursor.rowcount == 0:

  print('No instructors found')

else:

  for x in myresult:

    print(x[0])

mycursor.close()

mydb.close()

