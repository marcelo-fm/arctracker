import arcpy
arcpy.management.CreatePointSceneLayerPackage(
    r'c:\temp\points.lyrx', None, arcpy.SpatialReference(4326), 
    r'c:\cloudConnections\AWS.acs')