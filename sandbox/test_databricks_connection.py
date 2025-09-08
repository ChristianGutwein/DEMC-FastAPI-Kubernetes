from databricks import sql
#from app.core.config import get_settings

#_settings = get_settings()

# Replace with your Databricks connection details
#DATABRICKS_SERVER_HOSTNAME = _settings.DATABRICKS_SERVER_HOSTNAME
#HTTP_PATH = _settings.DATABRICKS_HTTP_PATH
#ACCESS_TOKEN = _settings.DATABRICKS_ACCESS_TOKEN

try:
    # Establish connection
    with sql.connect(
        server_hostname="",
        http_path="",
        access_token=""
    ) as connection:

        print("Connection established successfully!")

        # Execute a simple test query
        with connection.cursor() as cursor:
            cursor.execute("SELECT current_user(), current_date()")
            result = cursor.fetchall()
            print("Query Result:", result)

except Exception as e:
    print("Error connecting to Databricks:", e)