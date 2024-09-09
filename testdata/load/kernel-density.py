# Name: KernelDensity_Ex_02.py
# Description: Calculates the ozone concentration pattern divided by
#              Sierra Nevada Mountain in California
#              based on the point samples using a kernel function to
#              fit a smoothly tapered surface.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inFeatures = "ozone_california.shp"
populationField = "OZONE"
cellSize = 60
searchRadius = 2500
inBarriers = "SierraNevada.shp"

# Execute KernelDensity
outKernelDensity = KernelDensity(inFeatures, populationField, cellSize, searchRadius,
                                 "SQUARE_KILOMETERS", "DENSITIES", "PLANAR", inBarriers)

# Save the output 
outKernelDensity.save("C:/sapyexamples/output/KD_ozone_california.tif")