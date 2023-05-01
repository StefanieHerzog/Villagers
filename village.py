class Village:
    name = ""
    resources = int()

    def __init__(self):
        self.name = input("Definiere einen Namen für dein Dorf: ")
        self.resources = 50

    def show_stats(self):
        print(
            f"{self.name:<8}",
            "Ressourcen: ", self.resources,
        )