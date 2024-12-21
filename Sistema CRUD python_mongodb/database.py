import pymongo
import pymongo.mongo_client

def conectar_mongo():
    try:
        #Conecta ao banco de dados
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['pcConfig_db']
        print("Conectado")
        return db
    except Exception as e:
        print(f"Erro ao conectar ao banco de dadaos\nErro: {e}")
        return None