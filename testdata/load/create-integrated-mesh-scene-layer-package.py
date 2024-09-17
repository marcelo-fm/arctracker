import arcpy
arcpy.env.workspace = "C:/temp"
arcpy.managementCreateIntegratedMeshSceneLayerPackage(
    ["Tile_+001_+001", "Tile_+001_+002", "Tile_+002_+001"], "mesh.slpk", 
    "anchor.shp", "OSGB", arcpy.SpatialReference(4326), 2048, "DESKTOP",
    'AWS.acs', 'mySceneLayer.i3srest')