import pyspark
from pyspark.sql import SparkSession
import pandas as pd

spark=SparkSession.builder.appName('StockPriceAnalysis').getOrCreate()
#df_pyspark=pd.read_csv('Security_Price.csv')
df_pyspark=spark.read.option('header','true').csv('Security_Price.csv').show()

df_pyspark.select().show()
#df_pyspark.describe().show()


