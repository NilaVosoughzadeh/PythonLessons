import sqlite3

connection = sqlite3.connect("./University.db")
cursor = connection.cursor()

#CREATE TABLE Student(
#             studentID BIGINT PRIMARY KEY,
#             name VARCHAR(50),
#             lastName VARCHAR(50),
#             nCode CHAR(10),
#             major VARCHAR(60),
#             age TINYINT,
#             phone CHAR(11),
#             married BOOL
#             );


studentID = eval(input("Enter your student number : "))
name = input("Enter your name : ")
lastName = input("Enter your last name : ")
nCode = input("Enter your nationality code : ")
major = input("Enter your major : ")
age = input("Enter your age : ")
phone = input("Enter your phone : ")
married = input("Are you married? (enter true or false) ")

sqlQuery = f"""
            INSERT INTO Student VALUES ({studentID} , "{name}" , "{lastName}" , "{nCode}" , "{major}" , {age} , "{phone}" , {married})
        """

#DROP TABLE Student
#DELETE FROM Student WHERE CONDITION
#UPDATE Student SET CHANGE WHERE CONDITION

#SELECT NAME FROM Student WHERE major = "Math"
#cursor.execute(sqlQuery)
#result = cursor.fetchall()
#for i in result:
# print(i)

#SELECT name , lastName FROM Student WHERE major LIKE "%Engineering"
#"%Engineering%"
#"Engineering%"

#SELECT name , lastName FROM Student WHERE name LIKE "____"

cursor.execute(sqlQuery)
connection.commit()
connection.close()