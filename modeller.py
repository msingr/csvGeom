from geojson.featureCollection import FeatureCollection
from geojson.feature import Feature
from geojson.polygon import Polygon
from geojson.coordinate import Coordinate

from outputType import OutputType

class Modeller():

    def __init__(self):
        pass

    def createCoordinate(self, dictLine):
        east = str(dictLine['East']).replace(' ', '')
        north = str(dictLine['North']).replace(' ', '')
        height = str(dictLine['Height']).replace(' ', '')

        return Coordinate(east, north, height)

    def createGeometry(self, dict, geometryType):
        geometry = None

        if geometryType == OutputType.POLYGON:
            geometry = Polygon()

            for dictLine in dict:
                coordinate = self.createCoordinate(dictLine)
                geometry.addCoordinate(coordinate)

        if geometryType == OutputType.LINE:
            pass

        if geometryType == OutputType.POINT:
            pass

        return geometry

    def createFeature(self, dict, geometryType):
        geometry = self.createGeometry(dict, geometryType)

        identifier = dict[0]['Attribut1']

        return Feature(identifier, geometry)

    def createFeatures(self, dicts, geometryType):
        list = []

        for dict in dicts:
            feature = self.createFeature(dict, geometryType)
            list.append(feature)
        
        return list

    def createFeatureCollection(self, dicts, geometryType):
        featureList = self.createFeatures(dicts, geometryType)

        return FeatureCollection(featureList)
    
    def convertInputToModel(self, dicts, geometryType):
        return self.createFeatureCollection(dicts, geometryType)