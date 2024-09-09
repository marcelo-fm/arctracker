# Name: CreateRandomRaster_Ex_02.py
# Description: Creates a random raster dataset based on a 
#              user-specified distribution and extent.
# Requirements: None

# Import system modules
import arcpy

# Set local variables
outPath = "c:/output"
outFile = "randrast02"
distribution = "POISSON 6.4"
outExtent = "250 250 750 750"
cellSize = 25

# Execute CreateRandomRaster
arcpy.CreateRandomRaster_management(outPath, outFile, distribution, 
                                    outExtent, cellSize)