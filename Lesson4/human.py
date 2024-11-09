class Human:
    greeting = 'greeting - Hello'
    _greeting = '_greeting - Hello'
    __greeting = '__greeting - Hello'
    def __init__(self, name: str = 'Default human name'):
        self.Name = name
    def __str__(self):
        return (f'Name: {self.Name}\n'
                f'__Greeting: {self.__greeting}\n')
