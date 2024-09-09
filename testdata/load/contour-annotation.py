# Description: Create a contour with barriers feature class and then create 
#              annotation for the contours.
# Requirements: ArcGIS Spatial Analyst extension 

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data/data.gdb"

# Set local variables
inRaster = "elevation"
inBarrier = "ridges"
inTextFile = ""
explicitValues = "NO_EXPLICIT_VALUES_ONLY"
contourInterval = 200
indexInterval = 1000
contourList = [1500, 3000]
baseContour = 0
outContours = "C:/data/data.gdb/outcontourwithbarriers"

# Check out the ArcGIS ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Run ContourWithBarriers
arcpy.sa.ContourWithBarriers(inRaster, outContours, inBarrier, "POLYLINES", 
                             inTextFile, explicitValues, baseContour, 
                             contourInterval, indexInterval, contourList)

# Set local variables
inFeatures = "C:/data/data.gdb/outcontourwithbarriers"
inWorkspace = "C:/data/data.gdb"
LabelField = "Contour"
RefScaleValue = 50000
outLayer = "Contours"
Color = "BROWN"
TypeField = "Type"
Alignment = "PAGE"
Laddering = "NOT_ENABLE_LADDERING"

# Run ContourAnnotation
arcpy.cartography.ContourAnnotation(inFeatures, inWorkspace, LabelField, 
                                    RefScaleValue, outLayer, Color, TypeField, 
                                    Alignment, Laddering)