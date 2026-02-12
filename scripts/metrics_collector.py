import mysql.connector
import psutil
import logging

#logging
logging.basicConfig(
    filename="/opt/python-mysql-grafana_monitoring/logs/metrics.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

# MYSQL connection
db_config = {
    "host": "localhost",
    "user": "user",
    "password": "YourPassword",
    "database": "mysql-grafana_monitoring"
}

try:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = """
        INSERT INTO system_metrics (cpu_usage, memory_usage)
        VALUES (%s, %s)
    """

    cursor.execute(query, (cpu, memory))
    conn.commit()

    logging.info(f"Inserted CPU={cpu} MEMORY={memory}")

except Exception as e:
    logging.error(str(e))

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
