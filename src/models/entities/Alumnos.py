class Alumno():
    def __init__(self, id, name=None, last_name=None, email=None):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.email = email

    def to_JSON(self):
        return {
            'id':self.id,
            'name':self.name,
            'last_name':self.last_name,
            'email':self.email
        }