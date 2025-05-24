import pyodbc

try:
    connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=ALEJANDRO\\SQLEXPRESS;'
            'DATABASE=GestionAcademica;'
            'UID=Alejandro;'
            'PWD=Alejandro_tf11'
        )
    print("Conexión Exitosa")
    cursor = connection.cursor()
    cursor.execute ("SELECT @@version;")
    row = cursor.fetchone()
    print(row)

except Exception as ex:
    print(ex)