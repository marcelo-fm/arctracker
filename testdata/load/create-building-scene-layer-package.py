import arcpy
arcpy.management.CreateBuildingSceneLayerPackage(
    r'c:\temp\buildings.lyrx', None, arcpy.SpatialReference(4326),
    'DESKTOP', r'c:\cloudConnections\AWS.acs')