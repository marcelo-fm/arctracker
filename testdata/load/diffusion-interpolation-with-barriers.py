# Name: DiffusionInterpolationWithBarriers_Example_02.py
# Description: Diffusion Interpolation with Barriers uses a kernel which is 
#              based upon the heat equation and describes the variation in 
#              temperature with time in a homogeneous medium.
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
zField = "ozone"
outLayer = "outDIWB"
outRaster = "C:/gapyexamples/output/diwbout"
cellSize = 2000.0
power = 2
inBarrier = "ca_outline.shp"
bandwidth = ""
iterations = 10
weightField = ""
addBarrier = ""
cumuBarrier = ""
flowBarrier = ""

# Execute DiffusionInterpolationWithBarriers
arcpy.DiffusionInterpolationWithBarriers_ga(inPointFeatures, zField, outLayer,
                                            outRaster, cellSize, inBarrier,
                                            bandwidth, iterations, weightField,
                                            addBarrier, cumuBarrier, flowBarrier)