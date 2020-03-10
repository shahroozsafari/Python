
import msaccessdb
import pyodbc
# Microsoft Access Engine Drive Should be installed 
# Check Driver :
# [x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')]
# If code returns Empty List [] Driver should install
# For Install Driver Serach "ACE driver" or use following Link . . .
# https://www.microsoft.com/en-us/download/details.aspx?id=54920

# With pyodbc it's Impossible  to Create Database, 
# for Create Database use msaccessdb (pip install msaccessdb)

msaccessdb.create("e:\\mydb.accdb")

Database= pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\\mydb.accdb")
cursor = Database.cursor()

try:
    cursor.execute("CREATE TABLE students(stdcode INTEGER,first_name TEXT,last_name TEXT,age byte,avg single)")
    Database.commit()
except:
    print("Table Exists")


std=[
    [1,"Ali","Ahmadi",20,19],
    [2,"Reza","Hasani",21,18.5],
    [3,"Payam","Rezaei",22,17],
    [4,"Maryam","Naseri",23,16.5],
    [5,"Shahram","Fazeli",25,14.3],
    [6,"Yaser","Ghafari",26,16.2]
]
cursor.execute("INSERT INTO Students VALUES(?,?,?,?,?)",std[0])
Database.commit()


cursor.execute("select * from Students")
records=cursor.fetchall()
for record in records:
    print (record)
