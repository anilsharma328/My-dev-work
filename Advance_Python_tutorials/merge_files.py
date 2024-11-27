# Script to concatenate a bunch of Excel files with
# Python and Pandas
#
# Remember that indexing starts with 0 in Python,
# whereas indexing starts with 1 in Excel
#import xlwt
import pandas as pd


# Number of files to process
n = 4
# Excel sheetname
sheetname = 'Tabelle1'
# Number of row to skip in each file
skiprows=1
# Header line that will be kept for column name (index 5 in Excel)
header=4
# Column containing the index for each row. Leave it to None if no index
index_col=0
# First file to process
#"C:/Users/anils/PycharmProjects/pythonProject/SampleWork.xlsx",
#folder= "C:/Users/anils/PycharmProjects/datafolder/"
#C:\Users\anils\PycharmProjects\pythonProject\datafolder
folder_name=r"C:\Users\anils\PycharmProjects\pythonProject\datafolder\\"
f = folder_name+"file1.xlsx"
DF = pd.read_excel(f, sheetname, skiprows = skiprows,header = header, index_col = index_col)
# Concatenate the content of other file to this dataframe
for i in range(2,n+1):
    f = folder_name+'file'+str(i)+'.xlsx'
    df = pd.read_excel(f, sheetname, skiprows = skiprows, header = header, index_col = index_col,engine='openpyxl')
    DF.append(df, ignore_index=True)
# Write the concatenated content to excel
DF.to_excel('file.xls',sheet_name = sheetname)