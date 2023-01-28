import pyspark
import pandas as pd
from pyspark.sql import SparkSession

df=pd.read_csv('./data.csv')
print(df)

#df.info()

spark=SparkSession.builder.appName("practice").getOrCreate()
data_frame=spark.read.option('Header','true').csv('./data.csv',inferSchema=True)
data_frame.printSchema()
type(data_frame)
#data_frame.columns
##Print two columns
data_frame.select('first_name','salary').show()
###Show Datatypes
data_frame.dtypes
##Describe Columns
data_frame.describe().show()

##Add columns in Data Frame
data_frame=data_frame.withColumn('Salary after 2 years', data_frame['salary'] * 2)
data_frame.show()
###  Remove the columns
data_frame = data_frame.drop('Salary after 2 years')
data_frame.show()

data_frame= data_frame.withColumnRenamed('first_name','Name')
data_frame.show()


