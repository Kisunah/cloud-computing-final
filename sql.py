import pyodbc
server = 'cloudcomputinggroup8.database.windows.net'
database = 'cloudComputingGroup8DB'
username = 'hanusisw'
password = 'Group8!!'   
driver= '{ODBC Driver 17 for SQL Server}'

def query(query):
    rows = []
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchone()
            while row:
                rows.append(row)
                row = cursor.fetchone()
    return rows

def insert(query):
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
            return