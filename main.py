#Some resources to understand pip and mysql connection:
#https://packaging.python.org/tutorials/installing-packages/
#https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html


#Simple program to create a database with one relation and to retrieve Medications, Pharmacies in a Database. As well as store patient vitals.



#import mysql.connector

import psycopg2

hostname='localhost'
database='Medication'
username='postgres'
password='****'
port_id = 5432

try:
    conn = psycopg2.connect(
                            host=hostname,
                            dbname=database,
                            user = username,
                            pwd=password,
                            port = port_id)

    cur = conn.cursor()


    #option = input("Enter medication name to find medication: ")

    cur.execute('SELECT * FROM MedicationName;')
    print(cur.fetchall())

    conn.commit()

except Exception as error:
        print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


"""mydb = mysql.connector.connect(

  host="127.0.0.1",

  user="root",

  password="Lc654321" 

)"""
