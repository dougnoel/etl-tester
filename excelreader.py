# Reading an excel file using Python 
import xlrd 
  
# Give the location of the file 
loc = ("PyTestSpreadsheet.xlsx") 
  
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet1 = wb.sheet_by_index(0)
sheet2 = wb.sheet_by_index(1)

# For row 0 and column 0 
print(sheet1.cell_value(0, 0))
print("Number of rows: ")
print(sheet1.nrows)
print("Number of columns: ")
print(sheet1.ncols)
print("Column names:")
for i in range(sheet1.ncols): 
    print(sheet1.cell_value(0, i))
print("First column:")
for i in range(sheet1.nrows): 
    print(sheet1.cell_value(i, 0))
print("2nd row value:")
print(sheet1.row_values(1)) 