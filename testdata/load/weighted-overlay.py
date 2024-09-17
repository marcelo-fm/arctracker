# Name: WeightedOverlay_Ex_02.py
# Description: Overlays several rasters using a common scale and weighing 
#    each according to its importance.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = "snow"
inRaster2 = "land"
inRaster3 = "soil"

remapsnow = RemapValue([[0,1],[1,1],[5,5],[9,9],["NODATA","NODATA"]])
remapland = RemapValue([[1,1],[5,5],[6,6],[7,7],[8,8],[9,9],["NODATA","Restricted"]])
remapsoil = RemapValue([[0,1],[1,1],[5,5],[6,6],[7,7],[8,8],[9,9],["NODATA", "NODATA"]])

myWOTable = WOTable([[inRaster1, 50, "VALUE", remapsnow],
                     [inRaster2, 20, "VALUE", remapland], 
                     [inRaster3, 30, "VALUE", remapsoil]
					          ], [1, 9, 1])    

# Execute WeightedOverlay
outWeightedOverlay = WeightedOverlay(myWOTable)

# Save the output
outWeightedOverlay.save("C:/sapyexamples/output/weightover2")