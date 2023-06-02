TODO:

Ende anpassen, mich erwähnen
"resulting" anpassen

# csvGeom
Convert Lists of Coordinates to GeoJSON-geometry-Format for iDAI.field / Field Desktop

Python script that converts csv-Lists to [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON)-files. The chosen file will be saved as "*filename*_*geometryType*.geojson" in the same place as the original file. The contents of the resulting file can be copied into the "Geometry"-Field of a Resource in [iDAI.field 2 / Field Desktop client](https://github.com/dainst/idai-field). This way, exports from total stations can be relatively easy transferred to the database.

As of version 0.2.0 the following geometry-types are available:

Point (and MultiPoint)
LineString
Polygon

MultiLineString and MultiPolygon will be supported at a later date.

## Format of the csv-File
Currently, the format of the csv-File **has** to be exactly: "PtID,East,North,Height,Attribut1" in the first row, and corresponding coordinates in the rows below (see examples). The decimal separator is "**.**". Currently, the height value has to exist or there will be redundant commata and the geometry will not work. Set to 0 if necessary. For example, the csv-File may look like this: 

|PtID|East|North|Height|Attribut1
|----|---:|---:|---:|
|TE33_01|10.000765844571617|53.564714308986836|0|TE22.A1
|TE33_02|10.003275866953757|53.566722326892553|0|TE22.A1
|TE33_03|10.003777871430186|53.571575036831355|0|TE22.A1
| etc. | etc. | ... | ... |
|TE33_16|9.998925161491382|53.562204286604697|0|TE22.A2
|TE33_17|10.000765844571617|53.564714308986836|0|TE22.A2

And the resulting geojson-file will contain this: 

```
[
    [
        [
            10.000765844571617,
            53.564714308986836,
            0
        ],
        [
            10.003275866953757,
            53.566722326892553,
            0
        ],
        ... etc.
    ]
]
```

And the resulting polygon is this:

```geojson
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": 1,
      "properties": {
        "ID": 0
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
              [
            10.000765844571617,
            53.564714308986836,
            0
        ],
        [
            10.003275866953757,
            53.566722326892553,
            0
        ],
        [
            10.003777871430186,
            53.571575036831355,
            0
        ],
        [
            10.003108532128282,
            53.575256402991826,
            0
        ],
        [
            10.000765844571617,
            53.57877043432682,
            0
        ],
        [
            10.002439192826378,
            53.578435764675866,
            0
        ],
        [
            10.004949215208518,
            53.575256402991826,
            0
        ],
        [
            10.006957233114228,
            53.572077041307779,
            0
        ],
        [
            10.008965251019941,
            53.569567018925639,
            0
        ],
        [
            10.011977277878508,
            53.568228340321831,
            0
        ],
        [
            10.01398529578422,
            53.566220322416122,
            0
        ],
        [
            10.013315956482316,
            53.563040960732081,
            0
        ],
        [
            10.008630581368989,
            53.560028933873511,
            0
        ],
        [
            10.000933179397094,
            53.558188250793272,
            0
        ],
        [
            9.998255822189478,
            53.559024924920656,
            0
        ],
        [
            9.998925161491382,
            53.562204286604697,
            0
        ],
        [
            10.000765844571617,
            53.564714308986836,
            0
        ]
          ]
        ]
      }
    }
  ]
}
```

## Context
The first version of this script was produced during @lsteinmann-s work for the [Miletus Excavation](https://www.miletgrabung.uni-hamburg.de/) in the course of the DFG/ANR-funded project ["Life Forms in the Megapolis: Miletus in the Longue Durée"](https://www.kulturwissenschaften.uni-hamburg.de/ka/forschung/lebensformen-megapolis.html).
