class FeatureCollection():

    type = "FeatureCollection"
    name = "csvGeom-Export"

    def __init__(self, features):
        self.features = features

    def __str__(self):
        return f'{{"type": "FeatureCollection", "features":{self.features}}}'
    
    def __repr__(self):
        return str(self)

    def __dict__(self):
        return {
            'type': 'FeatureCollection',
            'features': self.features
        }