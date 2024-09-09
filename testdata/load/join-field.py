# PermanentJoin.py
# Purpose: Join two fields from a table to a feature class 

# Import system modules
import arcpy

# Set the current workspace 
arcpy.env.workspace = "c:/data/data.gdb"

# Set the local parameters
inFeatures = "zion_park"
joinField = "zonecode"
joinTable = "zion_zoning"
fieldList = ["land_use", "land_cover"]

# Join two feature classes by the zonecode field and only carry 
# over the land use and land cover fields
arcpy.management.JoinField(inFeatures, joinField, joinTable, joinField, 
                           fieldList)