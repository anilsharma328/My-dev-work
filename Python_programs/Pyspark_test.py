import pyspark
from pyspark.sql import SparkSession
import pandas as pd

spark=SparkSession.builder.appName('StockPriceAnalysis').getOrCreate()
df=pd.read_csv('Security_Price.csv')

print(df)


