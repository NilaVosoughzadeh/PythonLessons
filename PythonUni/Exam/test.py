class Robot:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, My name is ", self.name)

    def move(self):
        print(self.name, "is moving 🤷‍♂️")