from flask import Flask, request, jsonify
from researchGate import findResearchGate
from googleAcademic import findGoogle
from microsoft import findMicrosoft
from database import queryDatabase, insertData
from bson import json_util

app = Flask(__name__)

@app.route('/')
def welcome():

    return {
        'message' : 'Bienvenido a la api de python webscraper de identidad digital',
        'authors' : {
            'Luis Octavio Grajales Servín' : 'Dev',
            'Antonio Vázquez Gutiérrez' : 'Dev',
            'M.S.I. José Alejandro Vargas Díaz' : 'Profesor a cargo'
        }
    }

# Consulta la base de datos, de no tener datos se hace el scrape
@app.route('/<string:name>')
def query_by_name(name):

    queryResult = queryDatabase(name)
    if(queryResult != None):
        return queryResult
    else:
        scrapeResults = {
            'research_gate' : findResearchGate(name),
            'google' : findGoogle(name),
            'microsoft' : findMicrosoft(name)
        }

        insertedData = insertData(name, scrapeResults)
        
        return insertedData


# Consulta únicamente la base de datos
@app.route('/db/<string:name>')
def query(name):
    results = queryDatabase(name)
    if(results != None):
        print (results)
        return results
    else:
        return { 'error' : 'Sin resultados' }

# Realiza únicamente el scrape guardando o sobreescribiendo los datos de la base de datos
@app.route('/scrape/<string:name>')
def scrape(name):

    scrapeResults = {
        'research_gate' : findResearchGate(name),
        'google' : findGoogle(name),
        'microsoft' : findMicrosoft(name)
    }

    insertedData = insertData(name, scrapeResults)
    
    return insertedData


if __name__ == "__main__":
    app.run(debug=True)