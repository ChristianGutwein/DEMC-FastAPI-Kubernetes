from databricks import sql
import os
from dotenv import load_dotenv
load_dotenv()


def test_db_connection():
    try:
        # Establish connection
        with sql.connect(
            server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
            http_path=os.getenv("DATABRICKS_HTTP_PATH"),
            access_token=os.getenv("DATABRICKS_ACCESS_TOKEN")
        ) as connection:

            print("Connection established successfully!")

            # Execute a simple test query
            query = f"""
                SELECT *    
                FROM mhpdeworkshop_databricks.00_christian_silver.nyc_taxi_enriched
                ORDER BY pickup_datetime DESC
                LIMIT 10
            """

            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                print("Query Result:")
                for row in result:
                    print(row)

    except Exception as e:
        print("Error connecting to Databricks:", e)

if __name__ == "__main__":
    test_db_connection()    