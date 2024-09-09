# IdentityWells.py
# Description: Simple example showing use of Identity tool
 
# Import system modules
import arcpy

# Set the workspace
arcpy.env.workspace = "C:/data/data.gdb"

# Set local parameters
inFeatures = "wells"
idFeatures = "counties"
outFeatures = "wells_w_county_info"

# Process: Use the Identity function
arcpy.analysis.Identity(inFeatures, idFeatures, outFeatures)