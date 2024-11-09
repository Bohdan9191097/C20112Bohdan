from human import Human
class Worker(Human):
    def __init__(self, name: str = 'Default worker name'):
        super().__init__(name)
    def __str__(self):
        return f'Teacher name: {self.Name}'