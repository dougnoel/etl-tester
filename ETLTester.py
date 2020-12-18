import zipfile
import xlrd
import mysql.connector
from mysql.connector import Error

def extract_excel(zip_file_path, extract_directory):
    
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_directory)
        
    print(zip_file_path + " Extracted")

def read_excel_sheet(excel_file_path, sheet_index):
    wb = xlrd.open_workbook(excel_file_path)
    return wb.sheet_by_index(sheet_index)

def read_database_table(db_host, db_name, db_user, db_password, table):
    try:
        connection = mysql.connector.connect(host=db_host,
                                             database=db_name,
                                             user=db_user,
                                             password=db_password)
    
        sql_select_Query = "select * from " + table
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        return cursor.fetchall()
    
    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

#create a temporary folder to store the extracted excel file
extract_path = "temp/"
#Take the zipfile name from the commandline
spread_sheet_name = "PyTestSpreadsheet"
extract_excel(spread_sheet_name + ".zip", extract_path)
#Look for an excel file in the temp folder and 
sheet1 = read_excel_sheet(extract_path + spread_sheet_name + ".xlsx", 0)
sheet2 = read_excel_sheet(extract_path + spread_sheet_name + ".xlsx", 1)

records = read_database_table('localhost', 'test_db', 'testuser', 'PoorPassword', 'docs')

#read mapping yaml
#map each sheet name in the yaml to a sheet name in excel. Throw an error if they do not match
# for each sheet
    #for each row in sheet
        #check to see if the sql results have the excel row data
        #store success or failure
        #if failure, store the expected result and the result found
            #Questions: What should we match on to determine an incomplete result?
            #What should we do to determine if a result has duplicate entries?
        #remove the row from the sql results
    #report on the results for the sheet:
        #Total number of rows processed
        #Number of Rows passed
        #Number of rows failed
        #Output of expected and actual results for each failed excel row
        #Total Number of rows processed
#Delete the excel file

print("Excel records")
for i in range(sheet1.nrows):
    print(sheet1.row_values(i))
print("DB Records")
for row in records:
    print("{",row[1],",",row[2],"}")

# show a link between specialty and docs sheet in excel and db