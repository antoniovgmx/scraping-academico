import datetime
from pymongo import MongoClient
connectionString="mongodb+srv://admin:serviciosocial@webscrape-database.ibt88.mongodb.net/<dbname>?retryWrites=true&w=majority"
# localConnection=""
client = MongoClient(connectionString)
db=client.scraped
authors = db.authors

def queryDatabase(search_param):
    result = authors.find_one({ 'full_name' : search_param }, {'_id':False} )
    if(result is not None):
        return result
    else: 
        return None

def insertData(name, data):

    if(queryDatabase(name) is not None):
        y se .replace_one({ 'full_name' : name }, {
        'full_name' : name,
        'date' : datetime.datetime.now(),
        'research_gate' : data['research_gate'],
        'google' : data['google'],
        'microsoft': : data['microsoft']
        }) 
    else:
        authors.insert_one({
        'full_name' : name,
        'date' : datetime.datetime.now(),
        'research_gate' : data['research_gate'],
        'google' : data['google'],
        'microsoft': : data['microsoft']
        })

    insertedData = queryDatabase(name)

    return insertedData
