from src.database.insert import insert

class Class:
    def __init__(self, name, id ,year,subjects, teacher , students):
        self.name = name
        self.id = id
        self.year = year
        self.subjects = subjects
        self.teacher = teacher
        self.students = students
        self.registerGrade()
    
    def registerGrade(self):
        insert(self, "classes")

    def __int__(self):
      return self.id
    

alg = Class("TADS 1", 1, 1900,"Alg",["Beto", "Vlad", "Huilton", "Kader"], ["Eu"])