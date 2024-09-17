import arcpy
import json
mdpath = "c:/omproject/dronecollection.gdb/droneimgs"
initpointset = [
    {
        "x": -117.21684675264804,
        "y": 34.052400694386705,
        "z": 123,
        "pointId": 1,
        "imagePoints": [
            {
                "imageID": 7,
                "x": -5635883367.549803,
                "y": -26485513430.170017,
                "u": -5635883367.549803,
                "v": -26485513430.170017
            }
        ]
    }
]
arcpy.MatchControlPoints_rm(
        mdpath, in_control_points=json.dumps(initpointset), out_control_points="c:/omproject/matchedpointsets.shp", similarity="HIGH")