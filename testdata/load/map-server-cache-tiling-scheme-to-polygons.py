# Name: MapServerCacheTilingSchemeToPolygons_Example2.py
# Description: Create a tile feature class and use those tiles to create annotation.

# Import system modules
import arcpy
import os

# Set environment settings
arcpy.env.workspace = "C:/data/data.gdb"

# Set local variables
inMapDocument = "C:/data/Annotation.mxd"
# Change path below to match your system
inTilingScheme = os.path.join(arcpy.GetInstallInfo()['InstallDir'], 
                              'Resources\\TilingSchemes\\ArcGIS_Online_Bing_Maps_Google_Maps.xml')
outFeatureClass = "C:/data/data.gdb/Tiles"
inTileExtent = "USE_MAP_EXTENT"
inClipping = "CLIP_TO_HORIZON"
inAntialiasing = "NONE"
inScales = ""

# Run MapServerCacheTilingSchemeToPolygons
arcpy.cartography.MapServerCacheTilingSchemeToPolygons(
    inMapDocument, inTilingScheme, outFeatureClass, 
    inTileExtent, inClipping, inAntialiasing, inScales)

# Set local variables
inMapDocument = "C:/data/Annotation.mxd"
inPolygonIndexLayer = "Tiles"
inOutGeodatabase = "C:/data/data.gdb"
outOutLayer = "GroupAnno"
inAnnoSuffix = "Anno"
inRefScaleValue = ""
inRefScaleField = "Tile_Scale"
inTileIDField = "OID"
inCoordSysField = ""
inMapRotationField = ""
inFeatureLinked = "STANDARD"
inGenerateUnplaced = "GENERATE_UNPLACED_ANNOTATION"

# Run TiledLabelsToAnnotation
arcpy.cartography.TiledLabelsToAnnotation(
    inMapDocument, inPolygonIndexLayer, inOutGeodatabase, 
    outOutLayer, inAnnoSuffix, inRefScaleValue, inRefScaleField, 
    inTileIDField, inCoordSysField, inMapRotationField,inFeatureLinked, 
    inGenerateUnplaced)