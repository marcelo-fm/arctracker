# Name: GALayerToGrid_Example_02.py
# Description: Exports a geostatistical layer to grid.
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inLayer = "C:/gapyexamples/data/kriging.lyr"
outGrid = "C:/gapyexamples/output/krig_grid"
cellSize = 2000
cellptsHor = 1
cellptsVer = 1

# Execute GALayerToGrid
arcpy.GALayerToGrid_ga(inLayer, outGrid, cellSize, cellptsHor, cellptsVer)