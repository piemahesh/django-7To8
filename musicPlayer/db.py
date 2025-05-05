from pymongo import MongoClient

mongo = MongoClient("mongodb+srv://ocenMahesh:ocean123@atlascluster.euxnpsz.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster")
# database
db = mongo.oceanAcademy 
# collection
products = db.products

