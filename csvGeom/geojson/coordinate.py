class Coordinate():

    def __init__(self, east, north, height="0"):
        self.east = east
        self.north = north
        self.height = height

    def __str__(self):
        return f"[{self.east},{self.north},{self.height}]"

    def __repr__(self):
        return str(self)

    def __dict__(self):
        return {
            'east' : self.east,
            'north' : self.north,
            'height' : self.height
        }
    