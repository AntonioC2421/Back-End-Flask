class Matricula():
    def __init__(self, id, alumno_id, curso_id):
        self.id = id
        self.alumno_id = alumno_id
        self.curso_id = curso_id

    def to_JSON(self):
        return{
            'id': self.id,
            'alumno_id': self.alumno_id,
            'curso_id':self.curso_id
        }