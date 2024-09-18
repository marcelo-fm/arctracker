# Name: LocateRegions_Ex_02.py
# Description: Selects the best specified number of regions
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
InRaster1 = "suitsurface"
InTotalArea2 = 13.5
InAreaUnits3 = "SQUARE_MILES"
InNumberofRegions4 = 5
InRegionShape5 = "CIRCLE"
InRegionOrientation6 = 0
InShapeTradeoff7 = 50
InEvaluationMethod8 = "HIGHEST_AVERAGE_VALUE"
InMinimumArea9 = 2
InMaximumArea10 = 5
InMinimumDistance11 = 1
InMaximumDistance12 = 3
InDistanceUnits13 = "MILES"
InExistingRegions14 = "existingreg.shp"
InRegionofNeighbors15 = "EIGHT"
InRegionNoIslands16 = "NO_ISLANDS"
InRegionSeeds17 = "SMALL"
InRegionResolution18 = "LOW"
InCombinatorialThreshold19 = "COMBINATORIAL"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute Locate Regions
outRegions = LocateRegions(InRaster1, InTotalArea2, InAreaUnits3, InNumberofRegions4,
                           InRegionShape5, InRegionOrientation6, InShapeTradeoff7,
                           InEvaluationMethod8, InMinimumArea9, InMaximumArea10,
                           InMinimumDistance11, InMaximumDistance12, InDistanceUnits13,
                           InExistingRegions14, InRegionofNeighbors15, InRegionNoIslands16,
                           InRegionSeeds17, InRegionResolution18, InCombinatorialThreshold19)

# Save the output
outRegions.save("C:/sapyexamples/output/outregions")