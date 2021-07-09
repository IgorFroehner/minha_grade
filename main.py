from decouple import config

from pymongo import MongoClient
from model import Schedule, save

if __name__ == '__main__':

    client = MongoClient(
        f"mongodb+srv://{config('DB_USER')}:{config('DB_PASS')}@cluster0.ogn2b.mongodb.net/myFirstDatabase"
        f"?retryWrites=true&w=majority")
    db = client.test

    result = db.test.insert_one({"name": "machado", "id": 1})

    a = Schedule(1, 'CDI-0001')

    save([a])


