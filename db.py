from pymongo import Connection


def test():
    connection = Connection()
    db = connection.towns_database

    collection = db.test_collection

    town = {"name": "Patchogue",
            "avgprice": 259000,
            "county": "Suffolk"}

    collection.insert(town)

    db.collection_names()
    print collection.find_one({"name": "Patchogue"})

def insert(database, collection, objectToInsert):
    connection = Connection()
    db = connection[database]
    coll = db[collection]
    coll.insert(objectToInsert)

def find(database, collection, criteria):
    connection = Connection()
    db = connection[database]
    coll = db[collection]
    found = coll.find(criteria)
    return found

def find_one(database, collection, criteria):
    connection = Connection()
    db = connection[database]
    coll = db[collection]
    found = coll.find_one(criteria)
    return found

def getAll(database, collection):
    connection = Connection()
    db = connection[database]
    for item in db[collection].find():
        print item