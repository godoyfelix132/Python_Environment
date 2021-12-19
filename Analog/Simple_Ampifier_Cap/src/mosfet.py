class Mosfet:
    def __init__(self, name, gm, gds):
        self.name = name
        self.gm = float(gm)
        self.gds = float(gds)
