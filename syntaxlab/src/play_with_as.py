class PlayWithAS:
    def __init__(self, name):
        self.name = name
        self.message = 'Hello ' + self.name + ', I am created.'
        self.content = [1, 2, 3, 4, 5]
        print(self.message)

    def __enter__(self):
        self.message = 'Hello ' + self.name + ', I entered.'
        print(self.message)
        return self.content

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.message = 'Hello ' + self.name + ', I exited.'
        print(self.message)


with PlayWithAS('Yang SHEN') as c:
    [print(x) for x in c]
