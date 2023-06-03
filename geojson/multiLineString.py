from geojson.geojsonObject import GeoJsonObject

from enums.outputType import OutputType

class MultiLineString(GeoJsonObject):

    def __init__(self):
        self.lines = []
        self.type = OutputType.MULTI_LINE

    def addLine(self, line):
        self.lines.append(line)

    def __str__(self):
        return f'"type": "{OutputType.MULTI_LINE.getGeoJSONCase()}", "coordinates" : {self.lines}'
    
    def __repr__(self):
        return str(self)
    
    def __dict__(self):
        return {
            'type': OutputType.MULTI_LINE.value,
            'coordinates': self.lines
        }
    