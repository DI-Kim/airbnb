class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"my name is {self.name} woof~ woof!"


jia = Dog("jia")
print(jia)

print(dir(jia))
