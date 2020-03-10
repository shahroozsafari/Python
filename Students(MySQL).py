
import pymysql
#-------------------------------CREATE DATABASE & CONNECTION --------------
Database=pymysql.connect(host="127.0.0.1",user="sh",password="Sh135714381203",db="books")
cursor=Database.cursor()
#-------------------------------CREATE TABLE ------------------------------
try:
    cursor.execute("CREATE TABLE students(stdcode INTEGER PRIMARY KEY,first_name TEXT,last_name TEXT,age INTEGER,avg REAL)")
except:
   print("Database Create")
#-------------------------------INSERT STUDENTS ----------------------------
std=[
    [1,"Ali","Ahmadi",20,19],
    [2,"Reza","Hasani",21,18.5],
    [3,"Payam","Rezaei",22,17],
    [4,"Maryam","Naseri",23,16.5],
    [5,"Shahram","Fazeli",25,14.3],
    [6,"Yaser","Ghafari",26,16.2]
]

for i in range(0,len(std)):
    try:
      cursor.execute("INSERT INTO students VALUES(%s,%s,%s,%s,%s) ",std[i])
    except:
        print("Student Exists")
Database.commit()
#-------------------------------UPDATE FIELDS ---------------------------
std_id=input("Enter Student Number : ")
cursor.execute("UPDATE students SET avg=20 where stdcode=%s",(std_id,))
Database.commit()
#-------------------------------DELETE RECORDS ---------------------------
std_id=input("Enter Student Number : ")
cursor.execute("DELETE FROM students where stdcode=%s",[std_id])
Database.commit()
#-------------------------------QUERY RECORDS ----------------------------
cursor.execute("SELECT * FROM students")
records=cursor.fetchall()

for record in records:
    print(record)
    