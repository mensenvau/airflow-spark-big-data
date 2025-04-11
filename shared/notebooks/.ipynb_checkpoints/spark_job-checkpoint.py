from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ExampleJob").getOrCreate()

# Configure Spark to talk to MinIO (S3-compatible)
hadoop_conf = spark._jsc.hadoopConfiguration()
hadoop_conf.set("fs.s3a.endpoint", "http://minio:9000")
hadoop_conf.set("fs.s3a.access.key", "minioadmin")
hadoop_conf.set("fs.s3a.secret.key", "minioadmin")
hadoop_conf.set("fs.s3a.path.style.access", "true")

df = spark.read.text("s3a://data-lake/input.txt")
df.show()
df.write.mode("overwrite").csv("s3a://data-lake/output")
spark.stop()
