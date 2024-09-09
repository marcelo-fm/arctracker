# Name: Split.py
# Description: Split vegetation layer into separate feature classes 
# for each climate zone

# import system modules 
import arcpy 

# Set environment settings
arcpy.env.workspace = "C:/data"

# Split vegetation layer by climate zones, write to Output.gdb
veg = "Habitat_Analysis.gdb/vegtype"
splitFeatures = "climate.shp"
splitField = "Zone"
outWorkspace = "C:/output/Output.gdb"
clusterTol = "1 Meters"

arcpy.analysis.Split(veg, splitFeatures, splitField, outWorkspace, 
                     clusterTol)