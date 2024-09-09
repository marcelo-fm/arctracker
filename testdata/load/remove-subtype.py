#Name: RemoveSubtype.py
# Purpose: Remove subtypes from a subtype definition

# Import system modules
import arcpy
 
# Set the workspace (to avoid having to type in the full path to the data every time)
arcpy.env.workspace =  "C:/data/Montgomery.gdb"
  
# Set local parameters
inFeatures = "water/fittings"
stypeList = ["5", "6", "7"]
 
# Process: Remove Subtype Codes...
arcpy.RemoveSubtype_management(inFeatures, stypeList)