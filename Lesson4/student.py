from human import Human
class Student(Human):
    def __init__(self, name: str = 'Default student name'):
        super().__init__(name)

    def __str__(self):
        return (f'Student name: {self.Name}\n'
        f'Greeting: {self.greeting}\n'
        f'_Greeting: {self._greeting}\n')
