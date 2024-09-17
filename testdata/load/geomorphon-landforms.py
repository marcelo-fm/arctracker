# Name: GeomorphonLandforms_standalone.py
# Description: Calculates geomorphons over a search distance of 50 meters, skipping cells within 2 meters
# of the target cell. Terrain is considered flat if the difference between elevation angles is less or equal to 2 degrees.
# The calculated geomorphons are classified into landforms and saved as a raster. 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy.sa import *

# Set environment settings
arcpy.env.workspace = "C:/sapyexamples/data"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set local variables
inRaster = "elevation_1m.tif"
inAngleThreshold = 2
inDistanceUnits = "METERS"
inSearchDistance = 50
inSkipDistance = 2
inZunit = "METER"

# Execute the tool
outGeomorphonLandforms = GeomorphonLandforms(inRaster, "", inAngleThreshold, inDistanceUnits,
                                         inSearchDistance, inSkipDistance, inZunit)

# Save the output 
outGeomorphonLandforms.save("C:/sapyexamples/output/outgeomorphonlandforms02.tif")