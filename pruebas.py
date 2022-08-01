import mysql.connector as connection
import pandas as pd

result = ("Adolescentes","adulto25")
rango_etario = result
sql = f"SELECT * FROM personas WHERE rango_etario IN {rango_etario}";

db = connection.connect(host='172.23.1.56',
            database='personasjb',
            user='botmaker',
            password='wj93s07Eqlb6r2',
            port='3306',
        )

df = pd.read_sql(sql,db)

df.head()

df.to_excel('datos.xlsx')
print("Excel Generado!")