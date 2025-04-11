FROM apache/airflow:2.8.0

USER root
COPY requirements.txt /tmp/requirements.txt
RUN chown airflow: /tmp/requirements.txt

USER airflow

RUN pip install --no-cache-dir jupyter
RUN pip install --no-cache-dir -r /tmp/requirements.txt
