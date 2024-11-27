import pandas as pd

d = {'c1': ["Often times you'll need to use Pandas to analyze data that is stored in an Excel file or in a CSV file. This requires you to open and import the data from such sources into Pandas. Luckily, Pandas provides us with numerous methods that we can use to load the data from such sources into a Pandas DataFrame. Often times you'll need to use Pandas to analyze data that is stored in an Excel file or in a CSV file. This requires you to open and import the data from such sources into Pandas. Luckily, Pandas provides us with numerous methods that we can use to load the data from such sources into a Pandas DataFrame Often times you'll need to use Pandas to analyze data that is stored in an Excel file or in a CSV file. This requires you to open and import the data from such sources into Pandas. Luckily, Pandas provides us with numerous methods that we can use to load the data from such sources into a Pandas DataFrame Anil"]}

folder_name=r"C:\Users\anils\PycharmProjects\pythonProject\files\\"
filename1 = folder_name  + "sample.txt"
df=pd.DataFrame(d)
print(df.to_string())
dfAsString= df.to_string(header=False, index=False,col_space=1)
#dfAsString = Input_dataFrame[SeekCursorFrom:SeekCursorTo + DataChunkSize].to_string(header=False, index=False)
###print(dfAsString)
for i in range(10):
    with open(filename1, 'w') as f:
        f.write(dfAsString)


#######################Prg 2

# import pandas lib as pd
import pandas as pd

# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel("C:/Users/anils/PycharmProjects/pythonProject/SampleWork.xlsx",engine='openpyxl')
for row in dataframe1.iterrows():
    print("##########printing Next row ###########")
    print (row[1][0])
