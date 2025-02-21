import os
from dotenv import load_dotenv
import oracledb

load_dotenv()

username = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
host = os.getenv("DB_SERVER")
port = os.getenv("DB_PORT")
service_name = os.getenv("DB_SERVICE")

dsn = f"{host}:{port}/{service_name}"


def connect_to_oracle():
    try:
        print("Attempting Oracle connection with DSN:", dsn)
        connection = oracledb.connect(user=username, password=password, dsn=dsn)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM v$version")
        for row in cursor:
            print(row)

        return connection, cursor
    except Exception as e:
        print("Error connecting to Oracle:", e)
        return None, None


if __name__ == "__main__":
    conn, cursor = connect_to_oracle()
    if conn:
        cursor.close()
        conn.close()
