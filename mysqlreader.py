import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='test_db',
                                         user='testuser',
                                         password='PoorPassword')

    sql_select_Query = "select * from docs"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of doctors is: ", cursor.rowcount)

    print("\nPrinting each doctor record")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Location  = ", row[2], "\n")

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")



# create table docs(
#    id INT NOT NULL AUTO_INCREMENT,
#    name VARCHAR(100) NOT NULL,
#    location VARCHAR(100) NOT NULL,
#    PRIMARY KEY ( id )
# );

# INSERT INTO docs (name, location)
# VALUES ('Bob', 'Boston'),
# ('Marc', 'Minneapolis'),
# ('Rachel', 'Raleigh');

# create table specialties(
#    id INT NOT NULL AUTO_INCREMENT,
#    Specialty VARCHAR(100) NOT NULL,
#    Description VARCHAR(100) NOT NULL,
#    PRIMARY KEY ( id )
# );

# INSERT INTO specialties (Specialty, Description)
# VALUES ('Knee', 'Knee stuff'),
# ('Cardio', 'Heart stuff');