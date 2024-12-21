class PC_config:
    def __init__(self, db):
        self.db = db
        self.collection = db["pcConfig"]

    def add_config(self, id, processador, memoria_ram, armazenamento, placa_video, placa_mae):
        #Busca pelo processador
        pc_config = self.collection.find_one({"id:":id})
        if pc_config:
            return False #Ja existe essa configuração inserida no banco
        self.collection.insert_one({
            'id': id,
            'processador': processador,
            'memoria_ram': memoria_ram,
            'armazenamento': armazenamento,
            'placa_video': placa_video,
            'placa_mae': placa_mae
        })
        return True
    
    def del_config(self, id):
        #Busca pelo processador   
        pc_config = self.collection.find_one({"id:":id})
        if pc_config:
            self.collection.delete_one({"id": id})
            return True
        else:
            return False
        
    def listar_config(self):
        return self.collection.find()