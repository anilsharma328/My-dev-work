from pyspark import SparkConf,SparkContext ,SparkSession
from lib/logger import Log4j
if __name__ == "__main__":
    conf=SparkConf() \
    .setMaster("local[3]")\
    .setAppName("helloRDD")

    #sc = SparkContext(conf=conf)
    spark=SparkSession \
        .builder \
        .config(conf=conf) \
        .getOrCreate()

    sc =spark.SparkContext
    logger = Log4j(spark)

