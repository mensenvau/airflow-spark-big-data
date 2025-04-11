#!/usr/bin/env python
# coding: utf-8

# In[5]:


from pyspark.sql import SparkSession

# Setup Session and Configure Spark to talk to MinIO (S3-compatible)
spark = SparkSession.builder \
    .appName("test") \
    .master("spark://spark-master:7077") \
    .config("spark.jars", ",".join([
        "/opt/spark/jars/hadoop-aws-3.3.6.jar",
        "/opt/spark/jars/aws-java-sdk-bundle-1.12.517.jar",
        "/opt/spark/jars/hadoop-common-3.3.6.jar",
        "/opt/spark/jars/hadoop-hdfs-client-3.3.6.jar"
    ])) \
    .getOrCreate()

spark._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "http://minio:9000")
spark._jsc.hadoopConfiguration().set("fs.s3a.access.key", "minioadmin")  # or your actual key
spark._jsc.hadoopConfiguration().set("fs.s3a.secret.key", "minioadmin")  # or your actual secret
spark._jsc.hadoopConfiguration().set("fs.s3a.path.style.access", "true")
spark._jsc.hadoopConfiguration().set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")

spark


# In[6]:


df = spark.read.csv("file:/mnt/shared/data/input.csv", header=True)
df.show()
df.write.mode("overwrite").csv("s3a://data-lake/output/")

