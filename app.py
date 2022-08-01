import json
from flask import Flask, render_template, request
import mysql.connector as connection
import pandas as pd
result = None
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/rangoetario')
def rango_etario():
    return render_template('rango_etario.html')

@app.route('/generarExcel/')

def generar_excel():

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
    return("Excel Generado!")

if __name__=="__main__":
    app.run(debug=True)

@app.route('/test', methods=['POST'])
def test():
    output = request.get_json()
    print(output) # This is the output that was stored in the JSON within the browser
    print(type(output))
    global result
    result = json.loads(output) #this converts the json output to a python dictionary
    result = tuple([tuple(e) for e in result])
    print(result) # Printing the new dictionary
    print(type(result))#this shows the json converted as a python dictionary
    return result

