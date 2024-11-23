class Generator:
    def __init__(self, students: list):
        self.Students: list = students
    def GetStudent(self):
        for i in self.Students:
            yield i