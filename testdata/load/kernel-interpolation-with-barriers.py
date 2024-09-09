# Name: KernelInterpolationWithBarriers_Example_02.py
# Description: Kernel Interpolation with Barriers is a moving window predictor
#   that uses non-Euclidean distances.
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
zField = "ozone"
outLayer = "outKIWB"
outRaster = "C:/gapyexamples/output/kiwbout"
cellSize = 2000.0
inBarrier = "ca_outline.shp"
kernelFunction = "QUARTIC"
bandwidth = ""
power = ""
ridgeParam = "50"
outputType = "PREDICTION"

# Execute KernelInterpolationWithBarriers
arcpy.KernelInterpolationWithBarriers_ga(inPointFeatures, zField, outLayer, outRaster,
                                         cellSize, inBarrier, kernelFunction, bandwidth,
                                         power, ridgeParam, outputType)