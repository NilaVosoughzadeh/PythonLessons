import sqlite3

connection = sqlite3.connect("./Bank.db")
cursor = connection.cursor()

query = """
    CREATE TABLE DEPOSIT (
        ACOUNTNUMBER INT PRIMARY KEY ,
        BALANCE BIGINT,
        FOREIGN KEY (NAME) REFERENCES BRANCH,
        FOREIGN KEY (NCODE) REFERENCES CUSTOMER
    )
"""
#CREATE TABLE CUSTOMER(
#         NCODE CHAR(10) PRIMARY KEY,
#         NAME VARCHAR(50) ,
#         CITY VARCHAR(50),
#         STREET VARCHAR(85)
#     )

cursor.execute(query)
connection.commit()
connection.close()