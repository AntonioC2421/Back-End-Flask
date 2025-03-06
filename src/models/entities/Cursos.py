class Curso():
    def __init__(self, id, name=None , id_profesor=None):
        self.id = id
        self.name = name
        self.id_profesor = id_profesor
    
    def to_JSON(self):
        return {
            'id':self.id,
            'name':self.name,
            'id_profesor':self.id_profesor,
        }