import pyodbc

# Connection details
server = 'LAPTOP-R8HE13NJ'
database = 'mydatabase'      
driver = '{ODBC Driver 17 for SQL Server}'

# Connection string using Windows Authentication
conn_str = f"""
DRIVER={driver};
SERVER={server};
DATABASE={database};
Trusted_Connection=yes;
TrustServerCertificate=yes;
"""

'''you can also use :
   Username: YourUsername 
Password: YourPassword123'''


try:
    # Connect to SQL Server
    conn = pyodbc.connect(conn_str)
    print(" Connected to SQL Server successfully.")

    # Create a cursor and execute a query
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 5 * FROM dbo.Employees")
    rows = cursor.fetchall()

    # Print the rows
    print(" First 3 rows from Employees table:")
    for row in rows:
        print(row)

except pyodbc.Error as e:
    print("Database error :", e)
except Exception as ex:
    print("An unexpected error :", ex)
finally:
    try:
        conn.close()
        print("Connection closed.")
    except:
        pass
