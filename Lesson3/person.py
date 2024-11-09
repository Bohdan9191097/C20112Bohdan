class Person:

    def __init__(self, name: str = 'FakeName'):
        self.Name = name
    def __str__(self):
        return f'Name - {self.Name}\n'