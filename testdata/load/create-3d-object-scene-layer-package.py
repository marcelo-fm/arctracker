import arcpy
arcpy.management.Create3DObjectSceneLayerPackage(
    r'c:\temp\buildings.lyrx', None, arcpy.SpatialReference(4326), None, 
    'DESKTOP', r'c:\cloudConnections\AWS.acs')