### ✅ **Custom `README.md` for Airflow + Spark + Jupyter + S3 for Big Data Pipeline**

A full-featured local pipeline for distributed data processing using **Apache Spark**, **Apache Airflow**, and **Jupyter Notebooks**, integrated with **MinIO (S3-compatible data lake)** for shared storage.

#### 🔧 Technologies Used

- Apache Airflow
- Apache Spark (Master + Workers)
- Jupyter Notebook (PySpark enabled)
- MinIO (S3-compatible object storage)
- Docker Compose

---

### 🚀 Quick Start

#### 1. 📦 Start All Services

```bash
docker compose up --build
```

#### 2. 🧱 Initialize Airflow (only once)

```bash
docker compose run --rm airflow-webserver airflow db migrate
docker compose run --rm airflow-webserver airflow users create \
    --username admin --password admin --role Admin --email admin@example.com --firstname admin --lastname admin
```

Then access:

- Airflow UI: [http://localhost:8081](http://localhost:8081)
- Spark Master UI: [http://localhost:8080](http://localhost:8080)
- Jupyter: [http://localhost:8888](http://localhost:8888)
- MinIO Console: [http://localhost:9001](http://localhost:9001)

---

### 📁 Folder Structure

```bash
.
├── shared/
│   ├── data/             # Input/output data for Spark and Jupyter
│   ├── minio/            # MinIO persistent volume
│   └── notebooks/        # Jupyter notebooks (PySpark jobs)
├── jars/                 # Extra Spark JARs (e.g., hadoop-aws, aws-sdk)
├── dags/                 # Airflow DAGs
├── docker-compose.yml
└── README.md
```

---

### ⚙️ Configure Jupyter to Use Spark Cluster

In your notebook:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("NotebookToCluster") \
    .master("spark://spark-master:7077") \
    .config("spark.jars", "/opt/spark/jars/hadoop-aws-3.3.6.jar,/opt/spark/jars/aws-java-sdk-bundle-1.12.517.jar,/opt/spark/jars/hadoop-common-3.3.6.jar,/opt/spark/jars/hadoop-hdfs-client-3.3.6.jar") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "minioadmin") \
    .config("spark.hadoop.fs.s3a.secret.key", "minioadmin") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .getOrCreate()
```

---

### 🧪 Sample Notebook Job

```python
df = spark.read.text("s3a://data-lake/input.txt")
df.show()
df.write.mode("overwrite").csv("s3a://data-lake/output")
```

---

### 📸 Screenshots

#### DAGs View (Airflow)

![DAGs Example](./images/dags.png)

#### S3 Bucket (MinIO)

![S3 Bucket](./images/s3%20bucket.png)

#### Spark Job Monitoring

![Spark Master UI](./images/spark_ui.png)

---

### 📺 Watch & Learn

[📹 YouTube Tutorial](https://www.youtube.com/mensenvau)

---

### 📢 Join the Community

[@mensenvau on Telegram](https://t.me/mensenvau)
