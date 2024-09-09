# Name: exportToShapefile.py
# Purpose: Export a geodatabase feature class to a shapefile, include domain and subtype descriptions

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"
arcpy.env.transferDomains = True

# The equivalent with a keyword is
# arcpy.env.transferDomains = "TRANSFER_DOMAINS"

# Set local variables    
inFeatures = "Habitat_Analysis.gdb/vegtype"
outLocation = "Shapefiles"
outName = "Vegetation.shp"

arcpy.conversion.FeatureClassToFeatureClass(inFeatures, outLocation, outName)