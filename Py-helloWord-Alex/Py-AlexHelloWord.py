# Estructura de proyecto
# Py-AlexHelloWord/
# ├── helloPython.py
# ├── README.md
# ├── requirements.txt
# └── tests/
#     └── test_hello.py

class HelloPython:
    def __init__(self, name="Python"):
        self.name = name

    def saludar(self):
        return f"Hola, {self.name}!"


if __name__ == "__main__":
    saludo = HelloPython()
    print(saludo.saludar())

# Modificacion del archivio helloPython.py para agregar una función adicional
class HelloPython:
    def __init__(self, name="Python"):
        self.name = name

    def saludar(self):
        return f"Hola, {self.name}!"

    def despedir(self):
        return f"Adiós, {self.name}!"
