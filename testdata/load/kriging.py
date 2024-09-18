# Name: Kriging_Ex_02.py
# Description: Interpolates a surface from points using kriging.
# Requirements: Spatial Analyst Extension
# Import system modules

import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inFeatures = "ca_ozone_pts.shp"
field = "OZONE"
cellSize = 2000
outVarRaster = "C:/sapyexamples/output/outvariance"
lagSize = 2000
majorRange = 2.6
partialSill = 542
nugget = 0

# Set complex variables
kModelOrdinary = KrigingModelOrdinary("CIRCULAR", lagSize,
                                majorRange, partialSill, nugget)
kRadius = RadiusFixed(20000, 1)



# Execute Kriging
outKriging = Kriging(inFeatures, field, kModelOrdinary, cellSize,
                     kRadius, outVarRaster)

# Save the output 
outKriging.save("C:/sapyexamples/output/krigoutput02")