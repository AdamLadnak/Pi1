
class human:
    def __init__(self, name):
        self.name = name
        self.unava = 0

    def __str__(self):
        return self.name + " ma únavu: " + str(self.unava)

    def beh(self, km):
        if km > 20 - self.unava:
            print("Nemôžeš bežať ", km ,"km si moc unavený")
            return
        self.unava += km
        print(self)


    def spanok(self, hours):
        self.unava -= hours * 10
        if self.unava < 0:
            self.unava = 0

        print(self)



human = human("Karol")

human.beh(10)
human.beh(10)
human.beh(10)

human.spanok(1)

