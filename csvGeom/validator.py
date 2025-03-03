from csvGeom.enums.geoJsonType import GeoJsonType
from csvGeom.utils.util import Util
from csvGeom.utils.logger import Logger

from csvGeom.geojson.featureCollection import FeatureCollection
from csvGeom.geojson.feature import Feature


class Validator:
    
    def __init__(self, language):
        self.errCount = 0

        self.translations = Util.load_translations(language)
    
    def determine_geometry_type(self, geometry):
        return geometry.type

    def validate_coordinate_element(self, value):
        return value is not None

    def validate_coordinate(self, coordinate):
        return self.validate_coordinate_element(coordinate.north) and self.validate_coordinate_element(coordinate.east)
    
    def validate_coordinates(self, coordinates):
        for coordinate in coordinates:
            if not self.validate_coordinate(coordinate):
                return False

        return True

    def validate_point(self, geometry):
        number_of_coordinates = len(geometry.coordinates)

        if number_of_coordinates != 1:
            raise Exception
        
        for element in geometry.coordinates:
            try:
                self.validate_coordinate(element)
            except:
                Logger.error(self.translations["err_validation"], [geometry.type, element.pt_id], log_to_file=True)
                self.errCount += 1

        return geometry

    def validate_line_string(self, geometry):
        number_of_coordinates = len(geometry.coordinates)

        if number_of_coordinates < 2:
            raise Exception
        
        for element in geometry.coordinates:
            try:
                self.validate_coordinate(element)
            except:
                Logger.error(self.translations["err_validation"], [geometry.type, element.pt_id], log_to_file=True)
                self.errCount += 1
                
        return geometry
    
    def validate_polygon(self, geometry):
        number_of_coordinates = len(geometry.coordinates)

        if number_of_coordinates < 3:
            raise Exception
        
        for element in geometry.coordinates:
            try:
                self.validate_coordinate(element)
            except:
                Logger.error(self.translations["err_validation"], [geometry.type, element.pt_id], log_to_file=True)
                self.errCount += 1
        
        return geometry
        
    def validate_multi_point(self, geometry):
        number_of_points = len(geometry.points)

        if number_of_points < 2:
            raise Exception
        
        for element in geometry.points:
            try:
                self.validate_point(element)
            except:
                Logger.error(self.translations["err_validation"], [element.type, element.pt_id], log_to_file=True)
                self.errCount += 1

        return geometry
        
    def validate_multi_line_string(self, geometry):
        number_of_line_strings = len(geometry.lineStrings)

        if number_of_line_strings < 2:
            raise Exception
        
        for element in geometry.lineStrings:
            try:
                self.validate_line_string(element)
            except:
                Logger.error(self.translations["err_validation"], [element.type, element.pt_id], log_to_file=True)
                self.errCount += 1
        
        return geometry

    def validate_multi_polygon(self, geometry):
        number_of_polygons = len(geometry.polygons)

        if number_of_polygons < 2:
            raise Exception
        
        for element in geometry.polygons:
            try:
                self.validate_polygon(element)
            except:
                Logger.error(self.translations["err_validation"], [element.type, element.pt_id], log_to_file=True)
                self.errCount += 1

        return geometry

    def validate_geometry(self, geometry):
        geometry_type = self.determine_geometry_type(geometry)

        try:
            if geometry_type == GeoJsonType.POINT:
                return self.validate_point(geometry)
            elif geometry_type == GeoJsonType.LINESTRING:
                return self.validate_line_string(geometry)
            elif geometry_type == GeoJsonType.POLYGON:
                return self.validate_polygon(geometry)
            elif geometry_type == GeoJsonType.MULTI_POINT:
                return self.validate_multi_point(geometry)
            elif geometry_type == GeoJsonType.MULTI_LINESTRING:
                return self.validate_multi_line_string(geometry)
            elif geometry_type == GeoJsonType.MULTI_POLYGON:
                return self.validate_multi_polygon(geometry)
        except:
            raise Exception
        
    def validate(self, feature_collection_model):
        valid_model = FeatureCollection()

        for element in feature_collection_model.features:
            try:
                valid_geometry = self.validate_geometry(element.geometry)
                feature = Feature(element.identifier, valid_geometry)
                valid_model.add_feature(feature)
            except:
                Logger.error(self.translations["err_validation_feature"], [element.identifier], log_to_file=True)
                self.errCount += 1
        
        return valid_model
