from decouple import config

from pymongo import MongoClient

client = MongoClient(
        f"mongodb+srv://{config('DB_USER')}:{config('DB_PASS')}@cluster0.ogn2b.mongodb.net/myFirstDatabase"
        f"?retryWrites=true&w=majority")

db = client.my_schedule
