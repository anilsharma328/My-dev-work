from pyspark.sql import *
from lib.logger  import Log4j
if __name__ == "__main__":
    spark=SparkSession.builder.appName("Hello Spark").master("local[3]").getOrCreate()

    logger=Log4j(spark)
    logger.info("Hello Anil Starting session")


    logger.info("Hello Anil ending session")
    print("hello Pyspark")
    spark=SparkSession.builder \
    .appName("hello") \
    .master("local[2]") \
    .getOrCreate()

    data_list=[("anil",32)]

    df=spark.createDataFrame(data_list).toDF("Name","age")
    df.show()

   #spark.stop()